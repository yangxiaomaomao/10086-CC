cmd_/home/yangxiaomao/10086/bbr/tcp_bbr.mod := printf '%s\n'   tcp_bbr.o | awk '!x[$$0]++ { print("/home/yangxiaomao/10086/bbr/"$$0) }' > /home/yangxiaomao/10086/bbr/tcp_bbr.mod
