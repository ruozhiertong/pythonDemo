#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import os
import json
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from urllib.request import urlopen

import re

from selenium.webdriver.chrome.options import Options

import sys

sys.path.append('../email')
import sendmail
sys.path.append('../log')
import log




#Python命名规范。
#除了类名使用首字母大写的驼峰(单词首字母大写)=》帕斯卡命名法
#其他如 变量，函数，属性，方法全部下划线命名法（全部小写，单词之间用下划线）。 常量全部大写，单词之间下划线。

log_file= 'price.log'
config_file = 'config.json'
cofig_lastDate = 0.0
config_dict={}


'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def timeStampToTime(timestamp):
	#localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst)
	#timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))


'''加载配置文件'''
def loadConfig():
	#获取文件最后修改时间戳 float
	try:
		modify_t = os.path.getmtime(config_file)
	except FileNotFoundError as e:
		log.logInfo(config_file + "FileNotFound")
		exit(1)

	#修改时间没有变动，表明不需要重新读取配置
	if cofig_lastDate == modify_t:
		print("配置文件未改变")
		return config_dict
	else:
		try:
			with open(config_file,'r') as f:
				#read() 读取全部。返回类型str
				config_str = f.read()
				# 注意json标准语法中是不支持单引号。所以配置文件中的字符串应该都是双引号而不是单引号。 https://blog.csdn.net/u012063507/article/details/71554775
				config_dict = json.loads(config_str)
				return config_dict
		except:
			log.logInfo('读取配置文件 json数据异常')
			exit(1)

def getJDFinalRequest(text):
	# https://c0.3.cn/stock?skuId=1592448&cat=670,677,11303&venderId=1000000328&area=19_1607_3155_0&buyNum=1&callback=jQuery3990626
	skuIdStr = 'skuid:'
	index = text.find(skuIdStr) + len(skuIdStr)
	skuId = text[index:index + 20].split(',')[0]
	#print(skuId)
	catStr = 'cat: ['
	index = text.find(catStr) + len(catStr)
	cat = text[index:index + 20].split(']')[0]
	#print(cat)
	venderIdStr = 'venderId:'
	index = text.find(venderIdStr) + len(venderIdStr)
	venderId = text[index:index + 20].split(',')[0]
	#print(venderId)
	#log.logInfo("sku:" + skuId + ",cat:" + cat + ",venderId:" + venderId)
	httpRequest = ('https://c0.3.cn/stock?skuId=' + skuId + '&cat=' + cat + '&venderId=' + venderId + '&area=19_1607_3155_0&buyNum=1&callback=jQuery3990626').replace(' ','')
	log.logInfo(httpRequest,log_file)
	return httpRequest			

def getSuningFinalRequest(text):
	#分析得知，参数都存储在一段js中。所以从js中提取. 而且是一个json字符串，因此可以将其转成json的dict进行获取。
	##转成json 更方便快捷，访问获取更简单。不要直接操作字符串，用find从字符串中提取。
	index = text.find("var sn = sn || {") + len("var sn = sn || {") - 1
	json_text = text[index:].split(';')[0]

	#去除 "itemDomain":"//"+document.location.hostname, 
	json_text = json_text.replace('"itemDomain":"//"+document.location.hostname, ', '')
	#去除/* */ 注释
	pattern  = re.compile(r"/\*.*?\*/")
	json_text = pattern.sub("",json_text)
	#json.loads(str) 中的json字符串的key只能为字符串形式，否则解析出错。 这里cuxiaoSeq":{voucherTitle:1,lhvou，key并不是一个字符串
	json_text = re.sub(r'"cuxiaoSeq":{.*?},', "",json_text)

	json_param = json.loads(json_text)

	#注意使用贪婪和非贪婪方式。 贪婪方式，会一直到最后一个*/. 非贪婪方式，值找到第一个。
	# pattern = re.compile(r'/\*.*\*/')
	# result1 = pattern.findall(json_text)
	# result1
	# ['/*默认关闭，true为打开*/ "hasBottomFixed":false, /*默认关闭，true为打开*/ "hasTopFixed":false, /*默认关闭，true为打开*/']
	# pattern = re.compile(r'/\*.*?\*/')
	# result1 = pattern.findall(json_text)
	# result1
	# ['/*默认关闭，true为打开*/', '/*默认关闭，true为打开*/', '/*默认关闭，true为打开*/']

	partNumber = json_param.get("partNumber")
	vendorCode = json_param.get("vendorCode")
	category1 = json_param.get("category1")
	catenIds = json_param.get("catenIds")
	weight = json_param.get("weight")
	brandId = json_param.get("brandId")

	#https://pas.suning.com/nspcsale_0_000000010606656239_000000010606656239_0000000000_190_755_7550101_20089_1000051_9051_10346_Z001___R1901001_0.463_0___000060021__.html?callback=pcData
	# "partNumber":"000000010606656239"
	# "vendorCode":"0000000000"
	# _190_755_7550101  固定
	# "category1":"20089"
	# _1000051_9051_10346_Z001 固定
	# "catenIds":"R1901001"
	# "weight":"0.463"
	# 后面这个0 不影响。
	# "brandId":"000060021"
	httpRequest = ('https://pas.suning.com/nspcsale_0_' + partNumber + '_' + partNumber + '_' + vendorCode + '_190_755_7550101_' + category1 + '_1000051_9051_10346_Z001___' +  catenIds + '_' + weight + '_0___' + brandId + '__.html?callback=pcData').replace(' ','')
	log.logInfo(httpRequest,log_file)
	return httpRequest	


def getJDPrice(priceText):
	#其实返回的内容也是json格式的字符串，也可以使用转成json的dict进行访问。
	index = priceText.find('"p":') + len('"p":')
	#提取价格数字
	#price = priceText[index:index + 15].split('}')[0]
	price = re.findall('\d+',priceText[index:index + 15])[0]
	return price

def getSuningPrice(priceText):
	#注意，苏宁的一个网页可能包含商品的多个规格，因此不同规格不同价钱。对于这种情况比较坑爹。暂时不处理。
	matchObj = re.search(r'pcData\((.*?)\)',priceText)
	# print(matchObj.group(1))
	price_json = json.loads(matchObj.group(1))

	#read 获取到的是含有转义字符的。进行json.loads 要特别注意。
	#"policySellPoint":"{\\"returnCode\\":0,\\"returnMsg\\":\\"success\\",\\"sellPointInfo\\":\\"19元\\\\u003d100GB流量+300分钟\\\\u003ca href\\\\u003d https:\\/\\/cuxiao.suning.com\\/yyshc.html target\\\\u003d_blank\\\\u003e点击抢购。\\",\\"sendCityId\\":\\"9051\\"}"
	#如这里的字符串。
	#将其中多余的转义\去除。 似乎也不需要。
	# price_json = price_json.replace('\\\\', '\\')

	# saleInfo是一个数组.多个规格价格信息组成的数组。
	price = price_json.get("data").get("price").get("saleInfo")[0].get("promotionPrice")
	return price


'''直接从网页源码文件获取价格'''
def getPriceBySource():
	price_httprequest = {}
	history_price = {}
	goods_title = {}
	while True:
		config_dict = loadConfig()
		#dict 的迭代. item ->key.
		for item in config_dict:
			#text 二进制  b'xxxx'
			# 网页 <meta http-equiv="Content-Type" content="text/html; charset=gbk">
			# 明明是gbk，但是有些网页死活decode出问题，所以只能暂时ingore方式。
			if(price_httprequest.get(item) == None):
				fUrl = urlopen(config_dict[item].get("URL"))
				if fUrl.getcode() != 200:
					log.logInfo(config_dict[item].get("URL") + ' urlopen status code not 200')
					fUrl.close()
					continue

				text_b = fUrl.read()
				index = text_b.find("charset".encode())
				if "GBK".encode() in text_b[index:index + 30] or "gbk".encode() in text_b[index:index + 30]:
					charset = 'gbk'
				elif "utf-8".encode() in text_b[index:index + 30] or "UTF-8".encode() in text_b[index:index + 30]:
					charset = 'utf-8'

				text = text_b.decode(charset,'ignore')
				if("jd.com" in config_dict[item].get("URL")):
					#<meta http-equiv="Content-Type" content="text/html; charset=gbk">
					httpRequest = getJDFinalRequest(text)
				elif("suning.com" in config_dict[item].get("URL")):
					#<meta charset="UTF-8" />
					httpRequest = getSuningFinalRequest(text)
				fUrl.close() #注意关闭，不然太多的链接会导致Connection问题
				
				price_httprequest[item] = httpRequest
				
				index = text.find('<title>')
				title = text[index:index + 20] #含中文
				goods_title[item] = title


			#如果每个商品的skuid，cat ，verderId不会改变，那么完全不用每次都发送上面的请求，可以在第一次发送然后，然后下次直接下面的请求。
			#一般来说是不会变动的。
			try:
				fRequest = urlopen(price_httprequest.get(item))
				if fRequest.getcode() != 200:
					log.logInfo(price_httprequest.get(item) + " status not 200")
					fRequest.close()
					continue

				if("jd.com" in config_dict[item].get("URL")):
					priceText = fRequest.read().decode('gbk')
					price = getJDPrice(priceText)
				elif("suning.com" in config_dict[item].get("URL")):
					#会将转义字符decode之后又多了\.
					priceText = fRequest.read().decode()
					price = getSuningPrice(priceText)
				fRequest.close()

				log.logInfo(goods_title[item] + ": " + price, log_file)

		
				#为避免一天内发送多次请求，做一个历史低价策略。当出现低于历史低价时，才再发送。
				low_price = history_price.get(config_dict[item].get("URL"),1000000.0)

				if float(price.strip('"')) < config_dict[item].get("ExpectedPrice") and float(price.strip('"')) < low_price:
					#记录在历史价格文件中
					with open("history_p.txt","a+") as f:
						f.write(timeStampToTime(time.time()) +"\t" +  config_dict[item].get("URL") +" " + goods_title[item] + ": " + price+"\n")
					history_price[config_dict[item].get("URL")] = float(price.strip('"'))
					print(price)
					#发送邮件提醒
					#sendmail.sendEmail(config_dict[item].get("Email"), config_dict[item].get("URL") +" " + title + ": " + price)
					sendmail.sendEmailBylocal(config_dict[item].get("Email","1043096262@qq.com"),goods_title[item],config_dict[item].get("URL") +" " + goods_title[item] + ": " + price)
			except Exception as e:
				print(e)
				log.logInfo("urlopen Error" + price_httprequest.get(item))
		time.sleep(30*60)#30minutes



def getPriceByDriver():

	#注意驱动问题。一般最好和chrome版本一致。否则会出现莫名其妙的问题。
    #这里用chrome已经是最新版本了。所以更新驱动。放置在当前目录。或者覆盖掉/usr/local/bin/chromedriver
    #webdriver.Chrome('./chromedriver')  具体路径，从具体路径去加载驱动。
    #webdriver.Chrome("chromedriver") 会从默认的路径顺序去加载。 /usr/local/bin/chromedriver
    #webdriver.Chrome()<===> webdriver.Chrome("chromedriver") 看构造函数就清楚了
	driver = webdriver.Chrome("/usr/local/bin/chromedriver")   # open with Chrome
	#driver.implicitly_wait(5) #设置等待时间都不起作用。什么显示 隐式时间都不行。
	#因为driver.get 加载页面是同步阻塞的。因此有时候元素已经出来，但是还要完全等待完，没有必要，因此做超时处理。
	driver.set_page_load_timeout(20) #(5)

	while True:
		config_dict = loadConfig()

		#dict 的迭代
		for item in config_dict:
			# print(config_dict[item])
			
			#locator = (By.XPATH, '//div[@class="dd"]/span[@class="p-price"]/span[contains(@class,"price")]')
			#locator = (By.ID,"banner-miaosha")


			#由于css中有多个属性，因此直接使用css selector 来获取
			#使用xpath 也可以，要将带有空格也填入，不能只填入部分，否则找不到。
			#但是基于jd网页上的class是根据商品的id合成的。因此直接填入不会通用。
			# driver.find_element_by_xpath('//div[@class="dd"]/span[@class="p-price"]/span[@class="price J-p-6287165"]')
			#因此先找到父节点(缩小范围)，再找下面那个带有price class 的节点。
			#<span class="price J-p-6287165">329.00</span>
			#ele_p = driver.find_element_by_xpath('//div[@class="dd"]/span[@class="p-price"]') # ele_p.text ￥329.00
			#ele = ele_p.find_element_by_css_selector('.price') #ele.text 329

			try:
				print("open...")
				print(timeStampToTime(time.time()),config_dict[item].get("URL"))
				driver.get(config_dict[item].get("URL"))

				#不起作用
				#WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(locator))
				print("open done") #driver.get() 是同步阻塞的。要等网页完全打开才进行下一步。
				print(timeStampToTime(time.time()))
			except Exception as e:
				print("Except:",e)
				print("加载页面太慢，直接停止加载，继续下一步操作")
				print(timeStampToTime(time.time()),config_dict[item].get("URL"))
				#不需要做，timeout后自动停止加载了。
				#下面对chrome都不起作用
				#driver.execute_script('window.stop ? window.stop() : document.execCommand("Stop");')
				#driver.execute_script("window.stop()")
    # 		finally:
				# pass
				# driver.close()

			try:
				# 更好的方式
				ele = driver.find_element_by_xpath('//div[@class="dd"]/span[@class="p-price"]/span[contains(@class,"price")]')
				#print(ele)
				log.logInfo(driver.title + ": " + ele.text,log_file)

				if float(ele.text) < config_dict[item].get("ExpectedPrice"):
					#发送邮件提醒
					print(driver.title)
					print(ele.text)
					sendmail.sendEmail(config_dict[item].get("Email","1043096262@qq.com"), config_dict[item].get("URL") +" " +driver.title + ":" + ele.text)
			except Exception as e:
				print(e)
				log.logInfo("find_element_by_xpath error")


		time.sleep(30)


def getPriceByDriverHeadless():
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	driver = webdriver.Chrome("chromedriver",chrome_options=chrome_options)   # open with Chrome
	driver.set_page_load_timeout(20) #(5)
	while True:
		config_dict = loadConfig()
		#dict 的迭代
		for item in config_dict:
			try:
				print(timeStampToTime(time.time()),"open...",config_dict[item].get("URL"))
				driver.get(config_dict[item].get("URL"))
				print(timeStampToTime(time.time()),"open done")
			except Exception as e:
				print("Except:",e)
				print("加载页面太慢，直接停止加载，继续下一步操作")
				print(timeStampToTime(time.time()),config_dict[item].get("URL"))
			try:
				# 更好的方式
				ele = driver.find_element_by_xpath('//div[@class="dd"]/span[@class="p-price"]/span[contains(@class,"price")]')
				#print(ele)
				log.logInfo(driver.title + ": " + ele.text,log_file)

				if float(ele.text) < config_dict[item].get("ExpectedPrice"):
					#发送邮件提醒
					print(driver.title)
					print(ele.text)
					sendmail.sendEmail(config_dict[item].get("Email","1043096262@qq.com"), config_dict[item].get("URL") +" " +driver.title + ":" + ele.text)
			except Exception as e:
				print(e)
				log.logInfo("find_element_by_xpath error")


		time.sleep(30)

#AWS上执行： 后台一直执行。因为在终端里启动该脚本后，关掉终端，远程该脚本程序就退出了，使用nohup（忽略所有挂断信号）
#nohup命令：如果你正在运行一个进程，而且你觉得在退出帐户时该进程还不会结束，那么可以使用nohup命令。该命令可以在你退出帐户/关闭终端之后继续运行相应的进程。
#nohup python3 demo.py &

if __name__ == '__main__':	
	getPriceBySource()
	#getPriceByDriverHeadless()