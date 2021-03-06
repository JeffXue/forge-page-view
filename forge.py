# -*- coding: utf-8 -*-
import requests
import random
import time


def get_proxies():
    proxies = []
    # 运行前请设置对应的Cookie以及一致的User-Agent（可先通过浏览器访问一次后获取）
    header = {'Cookie': '',
              'User-Agent': ''}

    for i in xrange(10):
        try:
            proxy_url = 'http://www.kuaidaili.com/proxylist/%s/' % str(i+1)
            print proxy_url
            r = requests.get(proxy_url, headers=header)
            for j in xrange(10):
                ip = r.text.split('<td data-title="IP">')[j + 1].split('</td>')[0]
                port = r.text.split('<td data-title="PORT">')[j + 1].split('</td>')[0]
                proxies.append('http://' + ip + ':' + port)
        except Exception:
            print 'get proxies error'
            return None

    print proxies
    return proxies


def forge_page_view(target_url, proxies):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    if proxies is not None:
        for proxy in proxies:
            try:
                requests.get(target_url, headers=header, proxies={'http': proxy}, timeout=5)
                print 'send request in %s success' % proxy
                break
            except Exception:
                print 'send request in %s error' % proxy
    # 可灵活调整请求频率
    time.sleep(random.randint(5, 10))


if __name__ == '__main__':
    # 运行前请修改请求的url以及获取代理方法中的cookie
    url = 'http://www.chevroletfans.com/website/postlinkjump/?articleid=17608'
    proxies = get_proxies()
    while True:
        forge_page_view(url, proxies)
