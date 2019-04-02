0.功能：监测购物网站商品价格，当低于设定的价格时，向邮箱发送消息。
1.原理：使用selenium抓取网页，监测价格元素。可对京东，苏宁，国美，进行检测。

2.解析html可用selenium中driver 原生的。 也可以用库bs4。 因为只要获得价格信息就可以，没有涉及点击操作等，因此直接urlget获取网页，然后分析其中价格也可以(效率更快)。

3.在使用selenium时，打开商品页面要很久，一直阻塞在打开阶段效率低。 使用等待机制。

4.selenium 等待机制不起作用。



link:
0.xpath: https://blog.csdn.net/weixin_43430036/article/details/84836516#_112
1.xpath 选取包含多个class的元素，即class中含空格：
		xpath=//div[@class='J-Ajax num ico-tag']
		或者你也可以使用contains，像这样：xpath=//div[contains(@class , 'ico-tag')]
2.class 含空格，是表明该元素有多个class样式：https://blog.csdn.net/test_soy/article/details/80914677  https://blog.csdn.net/u013440574/article/details/81979311
3.selenium 抓取元素方式：https://www.cnblogs.com/zhaof/p/6953241.html
		find_element_by_name
		find_element_by_id
		find_element_by_xpath
		find_element_by_link_text
		find_element_by_partial_link_text
		find_element_by_tag_name
		find_element_by_class_name
		find_element_by_css_selector
4.注意json标准语法中是不支持单引号。所以配置文件中的字符串应该都是双引号而不是单引号。 https://blog.csdn.net/u012063507/article/details/71554775
5.python获取文件创建时间，修改时间： https://www.cnblogs.com/shaosks/p/5614630.html  https://blog.csdn.net/w122079514/article/details/16864403
6.发送邮件。http://www.runoob.com/python/python-email.html  https://www.cnblogs.com/yufeihlf/p/5726619.html
7.避免163 当做垃圾邮件,554, 导致发布出去。 https://www.cnblogs.com/mlp1234/p/9933919.html
8.收邮件提供商 可能会将邮件识别为垃圾邮件，所以可能要去垃圾箱中查看。
9.sendmail 服务： https://www.cnblogs.com/luhouxiang/p/4758403.html


