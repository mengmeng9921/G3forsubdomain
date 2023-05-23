# G3forsubdomain
子域名API接口批量提取工具

  ▄████  ██▀███   ███▄ ▄███▓
 ██▒ ▀█▒▓██ ▒ ██▒▓██▒▀█▀ ██▒    子域名API接口批量提取工具
▒██░▄▄▄░▓██ ░▄█ ▒▓██    ▓██░    
░▓█  ██▓▒██▀▀█▄  ▒██    ▒██     Coded By G3RM4
░▒▓███▀▒░██▓ ▒██▒▒██▒   ░██▒    
 ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░   ░  ░    Ice technology
  ░   ░   ░▒ ░ ▒░░  ░      ░
░ ░   ░   ░░   ░ ░      ░       https[:]//github.com/mengmeng9921/
      ░    ░            ░                                       

usage: G3forsubdomain.py [-h] [-u URL] [-uf URLFILE] [-p PATH] [-k APIKEY]

options:
  -h,   --help      show this help message and exit
  -u    URL,        --url     URL           -u    baidu.com
  -uf   URLFILE,    --urlfile URLFILE       -uf    domain.txt
  -p    PATH,       --path    PATH          -p    result.txt
  -k    APIKEY,     --apikey  APIKEY        -k    apikey


简单使用样例：
python G3forsubdomain.py -u   baidu.com     -k APIKEY
python G3forsubdomain.py -uf  domains.txt   -k APIKEY

固定APIKEY：
打开G3forsubdomain.py，将第十二行的apikey = "b14lDrfpiVQz6KNWRE59ja27J2dtQFVD"，替换为自己的key。
然后就可以直接使用简单命令查询了
python G3forsubdomain.py -u   baidu.com
python G3forsubdomain.py -uf  domains.txt

指定文件名,会根据单一查询或批量查询，添加文件后缀，默认单一查询输出txt文件，批量查询输出csv文件：
python G3forsubdomain.py -u   baidu.com     -p test
python G3forsubdomain.py -uf  domains.txt   -p /tmp/test
