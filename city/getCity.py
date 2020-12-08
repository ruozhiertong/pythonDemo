#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from urllib import request
from urllib.request import urlopen
import gzip
from bs4 import BeautifulSoup
import threading
import json
import random
import sys

sys.path.append('../log')
import log






year = 2018
origin_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/' + str(year) +'/index.html'

result_file = 'china.txt'

proxy_file = 'ip_port.dat'

end_level = 3 # 默认只要到县/区

china = []


def get_html(url,proxies=None):
	print(url)
	#有的网站会反爬。 尽量模拟构造成浏览器的header， User-Agent等。 关键还是在User-Agent
	# headers = {}
	# headers['Host'] = 'www.stats.gov.cn'
	# headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
	# headers['Accept']= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
	# headers['Accept-Encoding'] = 'gzip, deflate' #如果是压缩的，这个header不可少
	# headers['Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8'
	# headers['Cache-Control'] = 'max-age=0'

	headers = {
				'Host':'www.stats.gov.cn',
				'Connection':'keep-alive',
				'Cache-Control':'max-age=0',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
				'If-None-Match':'1c98-580baa54b4840-gzip',
				'If-Modified-Since': 'Thu, 31 Jan 2019 05:53:29 GMT'
				}
	req = request.Request(url,headers = headers)
	#也可以req = request.Request(url） 然后再通过req.add_header()去添加

	if proxies is not None:
		proxy_handler = request.ProxyHandler(proxies)
		opener = request.build_opener(proxy_handler,request.HTTPHandler)
		request.install_opener(opener)

	flag = True
	count = 0
	furl = {}
	while flag and count < 3:
		try:
			furl = urlopen(req,timeout = 15)
			flag = False
		except Exception as e:
			print(str(e) + ',' + url)
			log.logInfo(str(e) + ',' + url)
			count += 1
			#return None
	if flag:
		return None

	# furl = urlopen(req)
	if furl.code != 200:
		print('get '+ url + '  code:' + str(furl.code))
		return None

	text_b = furl.read()
	furl.close()


	#print(text_b[:6])

	#压缩过的。http://www.01happy.com/python-request-url-gbk-decode/
	# gzip 压缩 解压缩 https://blog.csdn.net/qq_35899407/article/details/91383983
	if text_b[:6] == b'\x1f\x8b\x08\x00\x00\x00':
		#print('gzip')
		text_b = gzip.decompress(text_b)
	#print(text_b)
	charset = 'utf-8'
	index = text_b.find("charset".encode())
	if "GBK".encode() in text_b[index:index + 30] or "gbk".encode() in text_b[index:index + 30]:
		charset = 'gbk'
	elif "utf-8".encode() in text_b[index:index + 30] or "UTF-8".encode() in text_b[index:index + 30]:
		charset = 'utf-8'
	elif 'gb2312'.encode() in text_b[index:index + 30] or 'GB2312'.encode() in text_b[index:index + 30]:
		charset ='gb2312'
	#https://bbs.csdn.net/topics/390632652?page=1
	#对于响应的编码问题，requests会从两方面去获取编码信息。 (其实我们自己处理的话也应该这样的方式)
	#1.首先从包的头部中的 Content-Type获取编码信息，将获取到编码信息放在req.encoding. 如果Content-Type没法得到编码信息，
	#encoding置为默认的ISO-8859-1。
	#2.其次会从获取到的html中获取编码信息。 一般html中的meta元素中会有页面编码的声明。requests会放在apparent_encoding中。
	#requests 的text 和 content 。 text实际上是由req2.content.decode(req2.encoding,'ignore')得来的。


	#对于统计局官网真是坑。
	#首先其请求的回应包中的头部的Content-type中也没有表明是什么编码，导致requests库也识别不到编码信息，req.encoding用默认的’ISO-8859-1‘，这也导致
	#requests库解码出现问题。
	#其次其网页真正的编码时GBK，但是其网页内声明的是gb2312，所以用gb2312进行解码 有些字符是由乱码的。req.apparent_encoding成了GB2312。用这个解码也成问题。
	#所以只能手动写死GBK。 坑。
	#print(charset)
	charset = 'GBK' # 对于统计局官网，写死。

	text = text_b.decode(charset,'ignore')
	#print(text)

	time.sleep(2) #不要频繁. 避免服务器作妖，尽量每次请求后sleep
	return text




#class_name 表元素的class属性
def parse_province(url,level,proxies):

	if level > end_level:
		return None


	text = get_html(url,proxies)

	if text is None:
		return None

	soup = BeautifulSoup(text,'html.parser')

	class_value = ''
	if level == 2:
		class_value = 'citytr'
	elif level == 3:
		class_value = 'countytr'
	elif level == 4:
		class_value = 'towntr'
	elif level == 5:
		class_value = 'villagetr'


	#海南省 好奇怪。 居然有的市下面直接是镇，而不是县。
	#所以改造。
	# headtr = soup.find(name = 'tr' , attrs = {'class': class_value[:-2] + 'head'})
	# if headtr is None:
	# 	print(headtr)
	# 	print(url ,level)
	# 	print(class_value[:-2] + 'head')
	# 	print(text)
	# else:
	# 	headtds = headtr.findChildren(recursive = False)
	# 	code_idx = 0
	# 	name_idx = 1
	# 	for idx , td in enumerate(headtds):
	# 		if td.text == '统计用区划代码':
	# 			code_idx = idx
	# 		if td.txt == '名称':
	# 			name_idx = idx
	key_class = ['city','county','town','village']

	for x in key_class:
		headtr = soup.find(name = 'tr' , attrs = {'class': x + 'head'})
		if headtr is not None:
			class_value = x + 'tr'
			break

	if headtr is None:
		return None

	#根据便签判别地区的行政级别。省， 市， 县/区， 乡/镇 ，村
	level = key_class.index(class_value[:-2]) + 2

	headtds = headtr.findChildren(recursive = False)
	code_idx = 0
	name_idx = 1
	for idx , td in enumerate(headtds):
		if td.text == '统计用区划代码':
			code_idx = idx
		if td.txt == '名称':
			name_idx = idx

	trs = soup.findAll(name = 'tr', attrs={'class': class_value})
	city = []
	for tr in trs:
		one = {}
		nodes = tr.findChildren(recursive=False)
		one['code'] = nodes[code_idx].text
		one['name'] = nodes[name_idx].text
		one['level'] = level

		if tr.find('a') is not None:
			child_url = tr.find('a').get('href')
			one['child'] = parse_province(url[:url.rfind('/')+1]+ child_url,level + 1,proxies)
		else:
			one['child'] = None
		city.append(one)

	return city


def process_thread(threadName, idx, url,proxies):
	china[idx]['child'] = parse_province(url,china[idx]['level'] + 1,proxies)


def parse_html(url):

	text = get_html(url)

	if text is None :
		print('text is None')
		return

	soup = BeautifulSoup(text,'html.parser')
	#print(soup)

	#result_bf = result_soup.prettify()

	#name 标签名称。 attrs 标签属性。
	provincetrs = soup.findAll(name = 'tr', attrs={'class':'provincetr'})

	all_urls = []


	for provincetr in provincetrs:
		provincetds = provincetr.findChildren(recursive=False) # 没有False 还会搜索到孙子
		for td in provincetds: #td-><td><a href="11.html">北京市<br/></a></td>, <a href="11.html">北京市<br/></a>, <br/>
			node = {}
			#print(td.text) # 北京市
			node['name'] = td.text
			node['level'] = 1
			node['code'] = ''

			# td_link = td.findChild() #td_link <a href="11.html">北京市<br/></a>
			# print(td_link.name) #a
			# print(td_link.attrs) # {'href':'11.html'}
			td_link = td.find('a').get('href')
			all_urls.append(url[:url.rfind('/')+1] + td_link)
			#node['child'] = parse_province(url[:url.rfind('/')+1] + td_link , node['level'] + 1)
			china.append(node)
	#print(china)
	#print(all_urls)
	
	proxy_urls = []
	with open(proxy_file,'r') as f:
		proxy_urls = f.read()
		proxy_urls = json.loads(proxy_urls)

	proxy_len = len(proxy_urls)
	#开多线程去处理
	threads = []
	for idx,p in enumerate(china):
		
		proxy_idx = random.randint(0,proxy_len -1) # 前后闭合[0,proxy_len-1]
		proxies = {'http':'http://{}:{}'.format(proxy_urls[proxy_idx][0],proxy_urls[proxy_idx][1])}
		print(proxies)
		proxies = None # 如果需要代理IP，注释这行。 
		t = threading.Thread(target=process_thread, args=("Thread-"+str(idx),idx,all_urls[idx],proxies))
		t.start()
		threads.append(t)

	#print(len(threads))

	for t in threads:
		t.join()

#获取行政区编码。
def simpleGetData():
	# 这个知道县为止。
	simpleData_url = "http://www.mca.gov.cn/article/sj/xzqh/2020/2020/2020112010001.html"
	response = urlopen(simpleData_url)
	print("code:" + str(response.code))
	if response.code == 200:
		text_b = response.read() 
		with open("simpleData_raw.dat", "wb") as code:
			code.write(text_b)
		#print(data)
		#process raw data
		charset = 'utf-8'
		index = text_b.find("charset".encode())
		if "GBK".encode() in text_b[index:index + 30] or "gbk".encode() in text_b[index:index + 30]:
			charset = 'gbk'
		elif "utf-8".encode() in text_b[index:index + 30] or "UTF-8".encode() in text_b[index:index + 30]:
			charset = 'utf-8'
		elif 'gb2312'.encode() in text_b[index:index + 30] or 'GB2312'.encode() in text_b[index:index + 30]:
			charset ='gb2312'
		city_dict = {}
		text = text_b.decode(charset,'ignore')
		soup = BeautifulSoup(text,'html.parser')
		trs = soup.findAll(name = 'tr')
		for tr_idx, tr in enumerate(trs):
			if tr_idx == 0 or tr_idx == 1 or tr_idx == 2:
				continue;
			tds = tr.findChildren(recursive=False) # 没有False 还会搜索到孙子
			if(len(tds) < 3):
				continue
			#只取 第2 3 个td。 
			# print(tds[1])
			# print(tds[2])
			# print(tds[1].text)
			# print(tds[2].text)
			#soup会将<span>标签的内容也作为父标签<td>的内容.所以删除它。
			span_tag = tds[1].find() #有的没有span
			if(span_tag != None):
				key = tds[1].text.lstrip(span_tag.text)
			else:
				key = tds[1].text
			span_tag = tds[2].find()
			if(span_tag != None):
				value = tds[2].text.lstrip(span_tag.text)
			else:
				value = tds[2].text

			if key != '':
				city_dict[key] = value

		with open("simpleData.dat","w") as f:
			#f.write(str(city_dict)) #格式不好看。
			f.write(json.dumps(city_dict,ensure_ascii=False, indent=4, separators=(',', ': ')))
	response.close()

#获取天气预报 的城市编码。
# 在 http://www.weather.com.cn/ 首页的 源码中可以找到相关的数据。 
#<script type="text/javascript" src="https://j.i8tq.com/weather2020/search/city.js"></script>
#也可以在开发者工具的sources中j.i8tq.com->weather2020->search->city.js 查看具体内容。
def getWeatherCityCode():
	weather_city_url = "https://j.i8tq.com/weather2020/search/city.js"
	response = urlopen(weather_city_url)
	print("code:" + str(response.code))
	if response.code == 200:
		text_b = response.read() # 是js 形式的 var city_data = {...},只要json格式
		index = text_b.find("{".encode())
		with open("weather_city_code.dat", "wb") as code:
			code.write(text_b[index:])
	response.close()

def main():
	parse_html(origin_url)

	with open(result_file,'w+') as f:
		f.write(json.dumps(china,ensure_ascii=False, indent=4, separators=(',', ': ')))
		#f.writ(china)

	# simpleGetData()

	# getWeatherCityCode()


if __name__ == '__main__':
	main()


