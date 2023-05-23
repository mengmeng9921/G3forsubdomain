#!/usr/local/bin/python
import requests
import json
import time
import datetime
import argparse
from colorama import Fore
import csv

# 登陆 https://securitytrails.com/
# 输入你申请的Apikey
apikey = "b14lDrfpiVQz6KNWRE59ja27J2dtQFVD"

Yellow = Fore.YELLOW
Reset = Fore.RESET


# 核心查询功能，输入域名，输出子域名列表
def get_sub_domains(domain):
    url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains"
    querystring = {"children_only": "true"}
    headers = {
        'accept': "application/json",
        'apikey': apikey
    }
    resp = requests.get(url, headers=headers, params=querystring)
    result_json = json.loads(resp.text)
    sub_domains = [i + '.' + domain for i in result_json['subdomains']]
    return sub_domains


def save_txt(sub_domains, filepath):
    f = open(filepath+".txt", 'w+')
    for i in sub_domains:
        f.write(i + '\n')
    f.close()


def save_csv(urlfile, filepath):
    with open(urlfile, 'r', encoding='utf-8') as f:
        line = f.readlines()
        try:
            for url in line:
                url = url.replace('\n', '')
                print(f"开始查询{url}的子域名")
                try:
                    sub_domains = get_sub_domains(url.replace('\n', ''))
                except :
                    print('多任务查询功能处出错')
                    pass
                with open(filepath+".csv", mode="a+") as rf:
                    csvwriter = csv.writer(rf)
                    for sub_domain in sub_domains:
                        print(sub_domain.replace('\n', ''))
                        csvwriter.writerow([sub_domain])
                print(f"查询{url}子域名任务结束,单一目标查询间隔时间为2s")
                time.sleep(2)
            print('全部任务结束')
        except:
            print('多任务循环处出错')
            pass

# banner显示
def display_banner():
    banne_text = rbanne_text = r"""
  ▄████  ██▀███   ███▄ ▄███▓
 ██▒ ▀█▒▓██ ▒ ██▒▓██▒▀█▀ ██▒    子域名API接口批量提取工具
▒██░▄▄▄░▓██ ░▄█ ▒▓██    ▓██░    
░▓█  ██▓▒██▀▀█▄  ▒██    ▒██     Coded By G3RM4
░▒▓███▀▒░██▓ ▒██▒▒██▒   ░██▒    
 ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░   ░  ░    Ice technology
  ░   ░   ░▒ ░ ▒░░  ░      ░
░ ░   ░   ░░   ░ ░      ░       https[:]//github.com/mengmeng9921/
      ░    ░            ░                                       
"""
    print(f"{Yellow}{banne_text}{Reset}")


# 命令行输入
def cmdline(known=False):
    parser = argparse.ArgumentParser(description=display_banner())
    parser.add_argument(
        '-u',
        '--url',
        help='-u baidu.com',
        type=str
    )
    parser.add_argument(
        '-uf',
        '--urlfile',
        help='-uf domain.txt',
        default='',
        type=str
    )
    parser.add_argument(
        '-p',
        '--path',
        help='-p result.txt',
        type=str,
        default=f'{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}_domain_result'
    )
    parser.add_argument(
        '-k',
        '--apikey',
        help='-k apikey',
        type=str,
        default=apikey
    )
    opt = parser.parse_args()
    return opt


# 主函数
def main():
    opt = cmdline()
    # 多目标
    if opt.urlfile:
        save_csv(opt.urlfile, opt.path)
    # 单一目标
    elif opt.url:
        save_txt(get_sub_domains(opt.url), opt.path)
    # 无目标
    else:
        print("输入参数错误，请使用-h查看使用方法")


if __name__ == '__main__':
    main()
