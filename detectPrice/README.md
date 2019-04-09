0.功能：监测购物网站商品价格，当低于设定的价格时，向邮箱发送消息。
1.原理：使用selenium抓取网页，监测价格元素。可对京东，苏宁，国美，进行检测。

2.解析html可用selenium中driver 原生的。 也可以用库bs4。 因为只要获得价格信息就可以，没有涉及点击操作等，因此直接urlget获取网页，然后分析其中价格也可以(效率更快)。
使用urlget效率高，但是获取价格信息较困难，需要分析获取价格的请求。
使用selenium 获取价格信息简单方便，直接等待网页加载完成后就能获取价格。缺点就是一个网页会有多个请求，因此要等待时间多久，效率低。

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
邮箱信息：subject， From ，To，正文。
7.避免163 当做垃圾邮件,554, 导致发布出去。 https://www.cnblogs.com/mlp1234/p/9933919.html
8.收邮件提供商 可能会将邮件识别为垃圾邮件，所以可能要去垃圾箱中查看。
9.sendmail 服务： https://www.cnblogs.com/luhouxiang/p/4758403.html


10.git 本地和远程：（远程都要在github上建立，并不能直接从本地一开始建立远程并推送）
a.
…or create a new repository on the command line
echo "# pythonDemo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ruozhiertong/pythonDemo.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/ruozhiertong/pythonDemo.git
git push -u origin master

b.
git clone


11.linux/unix 
	一般静态库 放在      /lib   /lib64   /usr/lib  				/usr/local/lib
	一般程序动态库放在					   /usr/share				/usr/local/share
	一般程序(可执行) 放在 /bin /sbin     /usr/bin  /usr/sbin 		/usr/local/bin /usr/local/sbin
	一般程序源文件  放在     			  /usr/src   				/usr/local/src
	一般程序源文件头文件				  /usr/include				/usr/local/include
	一般程序配置文件		/etc  									/usr/local/etc     ~/.xxx

12.ubuntu Python安装的模块在 ~/.local/lib/python2.7/site-packages/selenium


13.
git remote add origin https://github.com/ruozhiertong/pythonDemo.git
git push origin master //将本地masterpush到远程origin（url）上。 
《==》 git push https://github.com/ruozhiertong/UULP.git master:master 前master为本地分支，后master是remote的分支

git pull origin master  //将远程拉取到本地
《==》git pull https://github.com/ruozhiertong/UULP.git master:master
前master为远程的分支，后master为本地的分支

git branch --set-upstream-to=origin/master master //设置本地分支master默认到远程的url/master分支上
之后在master分支上就可以git pull。 git push

./git/config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = https://github.com/ruozhiertong/UULP.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master

14.
127.0.0.1
localhost  ==>通过hosts文件映射为127.0.0。1
rzet.local ==>这是域名，通过dns 映射为127.0.0.1




15.安装mail 和 postfix(sendmail少用了) sudo apt-get install mailutils. 会安装mail 和postfix等。


16.邮件协议端口 https://blog.csdn.net/my98800/article/details/78592492
常用端口：https://blog.csdn.net/lincnl/article/details/2025769 https://www.cnblogs.com/1666818961-lxj/p/7210021.html https://blog.csdn.net/xin3983/article/details/80692300 https://blog.csdn.net/zhanghuiyu01/article/details/80830045


echo "hello from local to local" | sendmail ubuntu@ip-172-31-29-66.us-east-2.compute.inter

From ubuntu@ip-172-31-29-66.us-east-2.compute.inter  Thu Apr  4 16:53:39 2019
Return-Path: <ubuntu@ip-172-31-29-66.us-east-2.compute.inter>
X-Original-To: ubuntu@ip-172-31-29-66.us-east-2.compute.inter
Delivered-To: ubuntu@ip-172-31-29-66.us-east-2.compute.inter
Received: by ip-172-31-29-66.us-east-2.compute.internal (Postfix, from userid 1000)
	id 176064142C; Thu,  4 Apr 2019 16:53:39 +0000 (UTC)
Message-Id: <20190404165339.176064142C@ip-172-31-29-66.us-east-2.compute.internal>
Date: Thu,  4 Apr 2019 16:53:39 +0000 (UTC)
From: Ubuntu <ubuntu@ip-172-31-29-66.us-east-2.compute.inter>

hello from local to local

echo "hello from local to local" | sendmail ubuntu@ip-172-31-29-66.us-east-2.compute.internal

From ubuntu@ip-172-31-29-66.us-east-2.compute.inter  Thu Apr  4 16:52:18 2019
Return-Path: <ubuntu@ip-172-31-29-66.us-east-2.compute.inter>
X-Original-To: ubuntu@ip-172-31-29-66.us-east-2.compute.internal
Delivered-To: ubuntu@ip-172-31-29-66.us-east-2.compute.internal
Received: by ip-172-31-29-66.us-east-2.compute.internal (Postfix, from userid 1000)
	id 9C3424142C; Thu,  4 Apr 2019 16:52:18 +0000 (UTC)
Message-Id: <20190404165218.9C3424142C@ip-172-31-29-66.us-east-2.compute.internal>
Date: Thu,  4 Apr 2019 16:52:18 +0000 (UTC)
From: Ubuntu <ubuntu@ip-172-31-29-66.us-east-2.compute.inter>

hello from local to local


echo "hello from local to local" | sendmail localhost 无法投递  


 mac 上的
echo '20190403 mac mail' | mail -s '重要会议' linxianri@rzet.localdomain

echo '20190403 mac mail' | mail -s '重要会议' 1043096262@qq.com ==>550. 在aws上都可以。

echo '20190403 mac mail' | mail -s '重要会议' testajctc@gmail.com ==>550-5.7.1。 在aws上可以。

python脚本中使用本地发送，在mac上不可以(提示连接本地smtp服务器失败)，在aws上可以。好像是因为大学城的IP被封了，用电信手机流量当热点可以发送。The IP you're using to send mail is not authorized to 550-5.7.1 send email directly to our servers

smtpd服务器上一般也有smtp(客户端)，因为服务器也要用这个smtp转发送邮件的。 
一般用的foxmail客户端写信， mail软件等，这些也都是smtp(客户端软件)。

aws服务器上postfix就是stmpd，postfix中的sendmail就是smtp。 mail也是smtp(客户端软件)。
以前的sendmail既是stmpd，也是smtp。现在基本都是postfix取代了。

一开始mac上没有smtpd(postfix 25端口)，aws上有启动smtpd。 
为什么Mac上没有启动smtpd，也能用mail或者sendmail 给自己(或其他邮箱，并不是因为设置三方的stmp)发信，自己也能收到信？
.mailrc作用？
似乎.mailrc在Mac和Ubuntu上不起作用，mail命令都是利用本地的smtpd进行发送个，并没有按照.mailrc上指定的stmp进行发送。why？
python3 API可以利用本地，也可以利用指定的smtp服务器进行发送的。

如何回信？给postfix服务器回信？


/var/mail/linxianri ===> mailbox 相当于邮箱。

netstat -tplun

lsof -i tcp: 

ps -aux

ps -ef

nmap localhost


urllib 获取的网页是二进制的b。 f = urlopen(xxx) f.read(), 要想解码成相应的字符串要知道相应的编码信息。一般获取的网页的编码信息是由其网页上的meta指定，可以通过f.info()查看编码信息。 
有可能因为网页压缩导致编解码出现问题，因此要先解压网页，再处理。
也有部分网页明明编码信息都对，但是decode还是出错，目前没有好的解决方法，只能将ignore掉 decode(xxx, 'ignore')


Python中字符串 有str形式，也有bytes类型形式。 
bytes是字符串的二进制形式(字符串到二进制有编码，具体哪种编码看具体语境的形式)（就同其在内存中表示形式一样的，即内存中的二进制形式）。 两种形式之间的转换，编码解码，注意编码解码格式。
a ='hello'  b=b'hello'  #python3默认是utf-8
a.encode() == b ==> TRUE
a == b.encode()  ==>TRUE

字符在内存中存的是二进制的。当然有多种的编解码格式的二进制，具体应该看具体语境。

Python3字符串前缀u、b、r
https://blog.csdn.net/weixin_42165585/article/details/80980739
https://blog.csdn.net/u010496169/article/details/70045895
https://www.cnblogs.com/liangmingshen/p/9274021.html
python2中加u和不加u，是为了明确其字符串在内存中存储是unicode，避免在不同机器，因为其解释器因不同系统环境导致存储在内存中的格式不一样导致编解码时出错。加u明确声明以unicode。
python3中默认都是unicode，因此加不加都一样的。


urllib urlopen 太多链接等待关闭，会出现urllib2.URLError'(<urlopen error [Errno -3] Temporary failure in name resolution>。 用完要及时关闭。
https://stackoverflow.com/questions/14560507/urllib2-urlerrorurlopen-error-errno-3-temporary-failure-in-name-resolutio
https://stackoverflow.com/questions/8356517/permanent-temporary-failure-in-name-resolution-after-running-for-a-number-of-h



urlopen :https://www.cnblogs.com/sysu-blackbear/p/3629420.html
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000/

python 学习 廖雪峰 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000


命名方法：匈牙利命名法，驼峰式命名法(小驼峰式命名法)，帕斯卡命名法(大驼峰式命名法)，下划线命名法。
https://blog.csdn.net/example440982/article/details/69524347

#Python命名规范。（python等脚本式语言用的较多的是下划线命名法， java用的较多的是驼峰式命名法）
#https://blog.csdn.net/weixin_39723544/article/details/82144280
#除了类名使用首字母大写的驼峰(单词首字母大写)=》帕斯卡命名法
#其他如 变量，函数，属性，方法全部下划线命名法（全部小写，单词之间用下划线）。 常量全部大写，单词之间下划线。

