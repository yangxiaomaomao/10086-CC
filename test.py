import threading
import time
import random
import json
import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import custom, pmonitor
from mininet.log import setLogLevel, info

testtime = 60
congestion = 'bbrplus4'
#congestion = 'cubic'

def perfTest():
    'Create network and run simple performance test'
    n = 2
    topo = Topo()
    h1 = topo.addHost('h1', ip="10.1.0.0/8", cpu=.5 / n)
    h2 = topo.addHost('h2', ip="10.2.0.0/8", cpu=.5 / n)
    s1 = topo.addSwitch('s1')
    topo.addLink(h1, s1)
    topo.addLink(h2, s1)
    net = Mininet(topo=topo, link=TCLink)
    net.start()

    h1, h2, s1 = net.get('h1', 'h2', 's1')
    h2.cmd('tc qdisc add dev h2-eth0 root fq pacing')
    h2.cmd('ip route change 10.0.0.0/8 dev h2-eth0 congctl {0}'.format(congestion))
    s1.cmd('tc qdisc add dev s1-eth1 root handle 1: tbf rate 200Mbit latency 20ms buffer 81920') # 16384
    s1.cmd('tc qdisc add dev s1-eth1 parent 1: handle 2: netem delay 0ms loss 0.1%')

    print()
    print("——开始进行带宽测试——")
    threading.Thread(target=change, args=(net,)).start()
    popens = dict()
    popens[h1] = h1.popen('iperf3 -s -p 5566', shell=True)
    popens[h2] = h2.popen(
        'iperf3 -c 10.1.0.0 -p 5566 -t {0} -J -i 0 -Z -P 1 > iperfResult.json'.format(testtime), shell=True)
    # netperf
    # popens[h1] = h1.popen('netserver -4 -L 0.0.0.0', shell=True)
    # popens[h2] = h2.popen('netperf -t TCP_STREAM -H 10.0.0.1 -l 60 -n 4', shell=True)
    popens[h2].wait()
    popens[h1].terminate()
    popens[h1].wait()
    time.sleep(2)
    outjson = json.load(open('iperfResult.json', 'r'))
    finish = int(outjson.get('end').get('sum_received').get('bytes')) / 1048576.0
    print '总带宽容纳数据量：{0}MBytes'.format(finishResult)
    print '实际传输总数据量：{0}MBytes'.format(finish)
    print '测试时长{0}秒内的带宽利用率为：{1}%'.format(testtime, finish * 100 / finishResult)
    net.stop()


def change(net):
    global finishResult
    starttime = int(round(time.time() * 1000))
    test_time = testtime * 1000
    nowtime = starttime
    allNum = 0
    s1 = net.get('s1')
    interrupt = True
    while nowtime <= starttime + test_time:
        addtime = random.randint(10000, 17000)
        if addtime > 15000:
            if interrupt:
                continue
            addtime = random.randint(100, 1000)
            if nowtime + addtime - starttime > test_time:
                continue
            else:
                addtime = addtime / 1000.0
            s1.cmd(
                'tc qdisc change dev s1-eth1 parent 1: handle 2: netem delay 20ms loss 100%')
            print '当前网络暂时中断 持续时间：{0}s'.format(addtime)
            interrupt = True
        else:
            randombw = random.randint(100, 200)
            delaynum = random.randint(0, 80)
            lossnum = random.uniform(0.1, 1)
            s1.cmd(
                'tc qdisc change dev s1-eth1 root handle 1: tbf rate {0}Mbit latency 20ms buffer 81920'.format(randombw))
            s1.cmd(
                'tc qdisc change dev s1-eth1 parent 1: handle 2: netem delay {0}ms loss {1}%'.format(delaynum, lossnum))
            if nowtime + addtime - starttime <= test_time:
                addtime = addtime / 1000.0
                allNum += addtime * randombw
            else:
                addtime = (test_time + starttime - nowtime) / 1000.0
                allNum += addtime * randombw
            print '当前带宽：{0}Mbps 当前延迟：{1}ms 当前丢包率：{2}% 持续时间：{3}s'.format(
                randombw, delaynum + 20, lossnum, addtime)
            interrupt = False
        time.sleep(addtime)
        nowtime = int(round(time.time() * 1000))
    finishResult = allNum / 8


if __name__ == '__main__':
    os.popen('fuser -k 6653/tcp')
    os.popen('mn -c')
    setLogLevel('info')
    perfTest()
