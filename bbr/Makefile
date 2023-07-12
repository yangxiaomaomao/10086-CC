obj-m := tcp_bbr.o
modules-objs := tcp_bbr.o

KDIR := /lib/modules/`uname -r`/build
PWD := $(shell pwd)

default:
	make -C $(KDIR) M=$(PWD) modules
clean:
	rm -rf *.o *.ko *.mod.c *.order *.mod *.symvers