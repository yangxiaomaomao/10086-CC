import threading
import time
import random
import json
import os
import sys
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import custom, pmonitor
from mininet.log import setLogLevel, info
from argparse import ArgumentParser
from subprocess import Popen, PIPE
from multiprocessing import Process

parser = ArgumentParser(description='Args for Congestion Control Algorithm')
parser.add_argument('--algo', '-a', help='Congestion Control Algorithm ', required=True)
parser.add_argument('--duration', '-d', help='test duration(s)', required=False, default=30)
parser.add_argument('--bbr-cwnd', '-bc', help='whether to test bbr cwnd(False/True)', required=False, default=0)
parser.add_argument('--jitter', '-j', help='bandwidth change frequency/s', required=False, default=1)
args = parser.parse_args()

PYVER = sys.version_info.major

# TO DELETE
DEBUG = 0

class CCTopo(Topo):
    def build(self):
        h1 = self.addHost('h1', cpu=.25)
        h2 = self.addHost('h2', cpu=.25)
        s1 = self.addSwitch('s1')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        
def config_net(net,algo):
    h1, h2, s1 = net.get('h1', 'h2', 's1')
    h1.cmd('ifconfig h1-eth0 10.0.0.1/24')
    h2.cmd('ifconfig h2-eth0 10.0.0.2/24')
    
    h2.cmd(
        'tc qdisc add dev h2-eth0 root fq pacing')
    s1.cmd(
        'tc qdisc add dev s1-eth1 root handle 1: tbf rate 200Mbit latency 20ms buffer 81920') # 16384
    s1.cmd(
        'tc qdisc add dev s1-eth1 parent 1: handle 2: netem delay 0ms loss 0.1%')

def start_iperf(net,duration,algo):
    h1,h2 = net.get("h1","h2")
    print('Start iperf ...')
    #CLI(net)
    popen1 = h1.popen(
        'iperf3 -s', shell=True)
    popen2 = h2.popen(
        'iperf3 -c 10.0.0.1 -t %d -J -i 0 -Z -P 1 -C %s > iperf_result/%s.json' % (int(duration), algo, algo), shell=True)
    return popen1,popen2

def stop_iperf(popen1,popen2):
    popen2.wait()
    popen1.terminate()
    popen1.wait()
    print('Kill iperf ...\n')
    #Popen('pgrep -f iperf3 | xargs kill -9', shell=True).wait()
    
def cwnd_monitor(net, fname):
    #return
    h1, h2 = net.get('h1', 'h2')
    #cmd = 'ss -i | grep %s:5201 -A 1 | grep cwnd' % (h2.IP())
    cmd = 'ss -i | grep %s:5201 -A 1 | grep cwnd | grep %s' % (h1.IP(), args.algo)
    with open(fname, 'w') as ofile:
        while 1:
            t = time.time()
            p = h2.popen(cmd, shell=True, stdout=PIPE)
            output = p.stdout.read()
            #print("cd",output)
            if PYVER == 3:
                output = output.decode('utf-8')
            if output != '':
                ofile.write('%f %s' % (t, output))
            time.sleep(0.01)
def dynamic_bw(net, duration, jitter):
    s1 = net.get("s1")

    start_time = time.time()
    
    if args.bbr_cwnd:
        print("*" * 10 + "开始测量bbr下的cwnd变化" + "*" * 10)
        bw_list    = [20,60,100,70,50]
        loss_list  = [0 for _ in range(len(bw_list))]
        delay_list = [10 for _ in range(len(bw_list))]
    else:
        print("*" * 10 + "开始测量测试%s算法下的带宽利用率" % args.algo + "*" * 10)
        bw_list    = [100,200,30,50,150,70,10,180] # Mbps
        loss_list  = [0.95,0.15,0.05,0.32,0.68,0.23,0.30,0.16] # %
        delay_list = [10,20,3,5,15,7,10,70]#[20,23,56,9,23,36,78,14] # ms

    idx = 0
    cap = 0
    f = open("bw_change.csv","w")
    f.write("bandwidth/Mbps,elapse/s\n")
    while True:             
        now = time.time()
        delta = now - start_time
        if delta > duration:
            break
        if idx % len(bw_list) == 0:
            print("remaining time-%.2fs" % (duration - delta))
            
        bw    = bw_list[idx % len(bw_list)]
        loss  = loss_list[idx % len(loss_list)]
        delay = delay_list[idx % len(delay_list)]
        
        f.write("%d,%d\n" % (bw,jitter))
        
        idx += 1
        cap += (bw * jitter)
        s1.cmd(
            'tc qdisc change dev s1-eth1 root handle 1: tbf rate {0}Mbit latency 20ms buffer 81920'.format(bw))
        s1.cmd(
            'tc qdisc change dev s1-eth1 parent 1: handle 2: netem delay {0}ms loss {1}%'.format(delay, loss))
        
        time.sleep(jitter)
        
    f.close()
    return cap / 8

def iperf_test():
    'Create network and run simple performance test'
    
    dname = args.algo
    algo  = args.algo
    duration = int(args.duration)
    jitter = int(args.jitter)
    
    iperf_dir = "iperf_result"
    
    if not os.path.exists(iperf_dir):
        os.mkdir(iperf_dir)
    
    topo = CCTopo()
    net = Mininet(topo=topo, link=TCLink)
    
    net.start()
    
    config_net(net,algo)
    
    if args.bbr_cwnd:
        monitor = Process(target=cwnd_monitor, args=(net, "bbr-cwnd.txt"))
        monitor.start()
        
    
    p1,p2 = start_iperf(net,duration,algo)
    
    cap_byte = dynamic_bw(net,duration,jitter)

    stop_iperf(p1,p2)
    
    if args.bbr_cwnd:
        monitor.terminate()
        print("拥塞窗口变化已保存至bbr-cwnd.txt")
    
    time.sleep(1)
    
    if DEBUG:
        outjson = json.load(open('iperf_result/%s.json' % algo, 'r'))
        finish = round(int(outjson.get('end').get('sum_received').get('bytes')) / 1048576.0)
        print('总带宽容纳数据量：{0}MBytes'.format(cap_byte))
        print('实际传输总数据量：{0}MBytes'.format(finish))
        print('测试时长{0}秒内的带宽利用率为：{1}%'.format(duration, finish * 100 / cap_byte))
    else:
        print("iperf结果已保存至iperf_result/%s.txt" % algo)
        print("带宽变化结果已保存至bw_change.csv，每行代表带宽和持续的时间")
    net.stop()

if __name__ == '__main__':
    if args.algo not in ["bbr","reno","cubic","bbr_plus"]:
        print("not suport congestion control algorithm, supports reno/bbr/cubic/bbr_plus")
        sys.exit(0)
        
    os.system('fuser -k 6653/tcp')
    os.system('mn -c')
    # setLogLevel('info')
    
    iperf_test()
