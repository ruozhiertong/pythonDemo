#!/usr/bin/python
# -*- encoding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import json



#可以获得免费代理ip的网站
urls = ['https://www.xicidaili.com/nn/' ,'https://lab.crossincode.com/proxy/']
result_file = 'ip_port.txt'


#num 获得代理ip数目
def get_ips(url,num):

	headers = {
				'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
				'Accept-Encoding': 'gzip, deflate, br',
				'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
				}
	req = requests.get(url, headers = headers)
	text = req.content.decode(req.apparent_encoding)
	#print(text)

	soup = BeautifulSoup(text,'html.parser')

	tbody = soup.find('table')


	trs = tbody.findChildren(recursive = False)

	ip_idx = 0
	port_idx = 1

	ip_port = []

	for idx, tr in enumerate(trs):
		if idx == num + 1:
			break
		cols = tr.findChildren(recursive = False)
		if idx == 0: # 表头 
			for col_idx, col in enumerate(cols):
					if('ip' in col.text.lower() or 'addr' in col.text.lower()):
						ip_idx = col_idx
					if('端口' in col.text or  'port' in col.text.lower()):
						port_idx = col_idx
		else:
			ipstr = cols[ip_idx].text
			portstr = cols[port_idx].text

			ip_port.append([ipstr,portstr])


	return ip_port

def validate_ips(ip_port):

	#urllib.urlopen('http://www.xxx.com', proxies={"http":'http://122.72.32.74:80'})
	valided_ip = []
	for x in ip_port:
		proxy_url = 'http://{}:{}'.format(x[0],x[1])
		proxies = {'http':proxy_url, 'https':proxy_url}
		print(proxies)
		start_time = time.time()
		try:
			req = requests.get('http://www.sina.com.cn',proxies = proxies, timeout = 5)
			print(req.status_code)
			end_time = time.time()
			print('cost', end_time - start_time)

			if end_time - start_time < 10:
				valided_ip.append(x)
		except Exception as e:
			print(e)
		# finally:
		# 	req.close()

	return valided_ip

def main():
	ip_ports = []
	for url in urls:
		print(url)
		ip_port = get_ips(url, 40)
		print(ip_port)
		ip_port = validate_ips(ip_port)
		print(ip_port)
		ip_ports.extend(ip_port)
		print(ip_ports)
	with open(result_file,'a+') as f:
			print(ip_ports)
			f.write(json.dumps(ip_ports))

if __name__ == '__main__':
	main()