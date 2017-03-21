import requests
import random
import time


def get_proxies():
    proxies = []
    try:
        url = 'http://www.kuaidaili.com/proxylist/1/'
        # 运行前请设置对应的cookie
        header = {'Cookie': '',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(url, headers=header)
        url = 'http://www.chevroletfans.com/website/postlinkjump/?articleid=17608'
        for i in xrange(10):
            ip = r.text.split('<td data-title="IP">')[i+1].split('</td>')[0]
            port = r.text.split('<td data-title="PORT">')[i+1].split('</td>')[0]
            proxies.append('http://'+ip+':'+port)
    except Exception:
        print 'get proxies error'
        return None
    print proxies
    return proxies


def forge_page_view(url):
    while True:
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    proxies = get_proxies()
    if proxies is not None:
        for proxy in proxies:
            try:
                requests.get(url, headers=header, proxies={'http': proxy}, timeout=10)
                print 'send request in %s success' % proxy
                break
            except Exception:
                print 'send request in %s error' % proxy
    # 可灵活调整请求频率
    time.sleep(random.randint(30, 60))

if __name__ == '__main__':
    # 运行前请修改请求的url以及获取代理方法中的cookie
    url = 'http://www.chevroletfans.com/website/postlinkjump/?articleid=17608'
    forge_page_view(url)
