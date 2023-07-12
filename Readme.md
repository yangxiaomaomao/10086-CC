# Linux内核拥塞控制策略的优化

## 1 实验目标

1. 学习在Linux下编译内核模块并嵌入系统的方法
2. 复现使用`BBR`拥塞控制算法时候的拥塞窗口大小变化
3. 在网络链路剧烈变化的场景下优化`BBR`算法

## 2 实验准备

1. 系统：`ubuntu 22.04`

2. 如果`uname -r`显示内核版本为`5.19.0-38-generic`，则直接使用提供的`tcp_bbr.c`即可，否则去[kernel archive](https://mirrors.edge.kernel.org/pub/linux/kernel/)下载对应内核的源码，并从使用其中的`linux-x.xx/net/ipv4/tcp_bbr.c`作为BBR基础实现。
3. 安装`iperf3`，使用命令`sudo apt install iperf3`

## 3 实验过程

### 3.1 编译`bbr`拥塞控制模块并嵌入系统

1. 在`bbr`目录下执行`make`命令，生成中间文件以及`tcp_bbr.ko`文件，即BBR拥塞控制模块。

2. `sudo insmod tcp_bbr.ko`将`bbr`模块嵌入到内核中。

3. `cat /proc/sys/net/ipv4/tcp_available_congestion_control `，显示结果中包含`bbr`即嵌入成功。

### 3.2 复现使用BBR时的拥塞窗口变化-
在`delay = 20ms，bandwidth = 20->60->100->70->50Mbps`时，

- 使用命令生成`bbr-cwnd.txt`，`sudo python3 cc_test.py --algo bbr -d 50 -bc 1 -j 10`
- 复现下图中拥塞窗口变化情况
- 分析原因

![image-20230711225157204](F:\Desktop\江苏移动\BBR\figure\bbr-cwnd.png)

### 3.3 在链路状态高速变化时优化`BBR`，将新的拥塞控制方法命名为`bbr_plus`，并嵌入系统

#### 优化原理

- `bbr`的`PROBE_BW`阶段，2个周期probe可用带宽，6个周期保持现有发送速率，保持现有速率时不能及时探测**已经变化**的可用带宽，下图见`tcp_bbr.c`

  ![image-20230711232832594](F:\Desktop\江苏移动\BBR\figure\bbr-gain.png "BBR中PROBE_BW的gain向量")

- `bbr_plus`的`PROBE_BW`阶段，一直在probe可用带宽，可以**更及时地**探测到当前的可用带宽，从而对链路的利用率更高。下图见`tcp_bbr_plus.c`

<img src="F:\Desktop\江苏移动\BBR\figure\bbr-plus-gain.png" alt="image-20230711232332812" style="zoom:80%;" />

#### 实验过程

- 在`bbr_plus`目录下，参考3.1中的嵌入`bbr`模块的步骤，将优化后的`bbr_plus`拥塞控制方法嵌入到系统中

- 使用下面命令分别测试在高速变化的链路中，四种拥塞控制（`reno,cubic,bbr,bbr_plus`）的链路利用率，对于同种拥塞控制算法，多次测量取链路利用率的平均值

  - `sudo python3 cc_test.py --algo ALGO_NAME`
  - 根据`iperf_result/ALGO.json`和`bw_change.csv`计算各自的链路利用率
  - 根据利用率大小对比结果，分析原因

  

## 结果展示