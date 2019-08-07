0.功能：监测购物网站商品价格，当低于设定的价格时，向邮箱发送消息。
1.原理：使用selenium抓取网页，监测价格元素。可对京东，苏宁，国美，进行检测。

2.解析html可用selenium中driver 原生的。 也可以用库bs4。 因为只要获得价格信息就可以，没有涉及点击操作等，因此直接urlget获取网页，然后分析其中价格也可以(效率更快)。
使用urlget效率高，但是获取价格信息较困难，需要分析获取价格的请求。
使用selenium 获取价格信息简单方便，直接等待网页加载完成后就能获取价格。缺点就是一个网页会有多个请求，因此要等待时间多久，效率低。

3.在使用selenium时，打开商品页面要很久，一直阻塞在打开阶段效率低。 使用等待机制。

4.selenium 等待机制不起作用。



link:
0.xpath: XPath即为XML路径语言（XML Path Language），它是一种用来确定XML文档中某部分位置的语言.(百科)
https://blog.csdn.net/weixin_43430036/article/details/84836516#_112
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
json 验证和格式化：https://www.json.cn/
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



git push时忽略文件。  pull 指定文件，忽略文件。 
https://www.jianshu.com/p/b67318c3433d 
https://www.jianshu.com/p/e82c89e187c5 
https://blog.csdn.net/u014259503/article/details/82775651

git设置忽略已提交过但本地已修改的文件：
https://www.cnblogs.com/qq917937712/p/5761970.html

AWS git上只拉取detectPrice目录，并且排除了detectPrice目录下的 *.txt和README.md。
	见AWS .git/info/sparse-chekout 配置文件。

AWS 上做的修改，复原成gitHub上的： https://blog.csdn.net/haoaiqian/article/details/78284337

11.linux/unix
https://blog.csdn.net/sweetfather/article/details/79625482
https://zhidao.baidu.com/question/263911682.html
	一般静态库，动态库 放在      /lib   /lib64   /usr/lib  				/usr/local/lib
	一般共享文件
    (Architecture independent data files.不是动态库)
                                            /usr/share				/usr/local/share
	一般程序(二进制，可执行) 放在 /bin /sbin     /usr/bin  /usr/sbin 	/usr/local/bin /usr/local/sbin
	一般程序源文件  放在     			  /usr/src   				/usr/local/src
	一般程序源文件头文件				  /usr/include				/usr/local/include
	一般程序配置文件		/etc  									/usr/local/etc     ~/.xxx

查看一个命令/可执行程序的库 ldd chromedriver：
https://blog.csdn.net/xiejinfeng850414/article/details/7843929


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


Python中字符串 有str形式 和 bytes类型形式。 
bytes是字符串的二进制形式(字符串到二进制有编码，具体哪种编码看具体语境的形式)（就同其在内存中表示形式一样的，即内存中的二进制形式）。 两种形式之间的转换，编码解码，注意编码解码格式。
a ='hello'  b=b'hello'  #python3默认是utf-8
a.encode() == b ==> TRUE
a == b.encode()  ==>TRUE

字符在内存中存的是二进制的。当然有多种的编解码格式的二进制，具体应该看具体语境。

python字符串：单引号，双引号，三引号(三单引号三双引号)，单/双引号前的前缀(r ,b u).
其中三引号，前缀r 的字符串，不处理其中的转义\ (除非遇到冲突的开始结束的分割符如r'' 或r"" 中的字符串有单引号 /双引号，那么需要对单引号/双引号 转义。),直接按照原样输出。其余形式的字符串遇到转义字符会进行转义处理，输出时按照转义后的输出。

如果字符串有转义，而且要进行转义处理(不是三引号，r)， 那么利用到的字符串都是转义处理后的。
一般处理字符串的程序，函数等都是按照其转义后的结果进行处理的。

python3 的交互界面中, stest='\\"hello\\"', 直接stest输出 和print(stest)输出区别： stest直接输出是按照字符串原样输出 结果：'\\"hello\\"' (而且保留stest前后' 表明是字符串)。 print输出是会按照其中的转义字符转义处理之后输出 结果：\"hello\"。(并没有保留赋值时的前后')

Python3字符串前缀u、b、r
https://blog.csdn.net/weixin_42165585/article/details/80980739
https://blog.csdn.net/u010496169/article/details/70045895
https://www.cnblogs.com/liangmingshen/p/9274021.html
python2中加u和不加u，是为了明确其字符串在内存中存储是unicode，避免在不同机器，因为其解释器因不同系统环境导致存储在内存中的格式不一样导致编解码时出错。加u明确声明以unicode。
python3中默认都是unicode，因此加不加都一样的。


st = '{"policySellPoint":"{\\"returnCode\\":0}"}'
json.loads(st) ==> 解析正确。

st = '{"policySellPoint":"{\"returnCode\":0}"}'
json.loads(st) ==> 解析错误。

分析: 如果没有两个\，那么就会被解析成'{"policySellPoint":"{"returnCode":0}"}'，而此时在解析"{" 双引号结束时，并不是遇到冒号，因此不能解析成一个key，而且还多了returnCode未知的变量。
同理，有两个\, 会变成 '{"policySellPoint":"{\"returnCode\":0}"}',解析到"{\" 并不会代表着结束，而是一直解析到最后，遇到0}" 后的" 才是这个值的结束。

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


#python 是解释型脚本语言。 很多脚本语言如python定义变量时无需指定变量类型，直接 变量 = 值。 不像java c等 需要指定变量类型 int a = 10。



python使用selenium

正常情况下(先有了chrome/其他浏览器)：
1.安装 python的selenium模块。 pip3 install selenium
2.下载 安装驱动如chromedriver(和你的浏览器版本相匹配)。 到官网或镜像点下载相匹配的驱动 安装到/usr/bin （环境变量可以访问到的路径下，即命令行下直接使用chromedriver命令可用）. 
3.使用 selenium 操作浏览器(可有头模式，也可无头模式)。 有头模式是显示浏览器界面的，无头模式是不显示浏览器界面的。


在服务器Ubuntu python selenium 无头模式：
https://blog.csdn.net/qq_29303759/article/details/83719285
ubuntu selenium 使用无头模式：
1.安装chromeDriver 在/usr/bin 下
sudo wget http://npm.taobao.org/mirrors/chromedriver/73.0.3683.68/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip

2. .py 代码中设置为无头模式。 除了这些设置外，其他和有头模式下的操作都一样。

3. 仅仅有驱动还不够，可能还需要一些依赖。发现chromedriver: error while loading shared libraries: libnss3.so: cannot open shared object file。  
安装libnss3 sudo apt-get install libnss3-dev

4.以为只要安装驱动就能使用无头模式。 想当然了， 发现还是要安装chrome 程序 才行。selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary。 驱动还是要配合着浏览器使用才行。

这个无界面的服务器使用selenium 也是一样的，只是只能使用的是无头模式,使用正常的有头会报错的。 比如在无界面的服务器中使用google chrome浏览器 ，(google-chrome:9450): Gtk-WARNING **: 04:14:05.978: cannot open display。 因为没有X server进行处理显示图形，仅仅只有x client(浏览器)是不行的。
linux下图形界面是X Window， 因此仅仅有client(浏览器)是不行的，还需要Xserver。

至于无头模式 能否做一些点击，扫码等相关的界面操作？ 
无头模式可以做点击等和有头模式一样的操作。唯一不能实现的是需要手动操作界面的行为，因为无头模式下没有界面，所以无法进行任何的手动操作，如手动扫码，点击验证图片等。除此之外，任何在有头模式上的操作都可以用在无头模式上(如点击 填表单等)。

在无界面的服务器运行selenium除了无头模式，也可以使用Xvfb (sudo apt-get install xvfb) + pyvirtualdisplay(pip3 install pyvirtualdisplay) 虚拟的GUI去执行selenium的有头模式
https://www.cnblogs.com/bestruggle/p/8080983.html
不过虚拟GUI缺点也和无头模式一样，对于界面的手动操作无能为力。

至于远程服务器其实也是可以安装图形界面的。 而且也能通过远程访问到服务器端图形界面。你所需要做的就是在远程服务器上面安装X Window服务端和桌面环境，在客户机上安装X Window的客户端。 当我们访问远程时，界面由服务器的X服务端处理完后发送到客户机的客户端上显示。(可能会有疑问，远程服务器上有显卡吗？可以处理图形相关的操作吗？一般都是有显卡的，可以处理图形。就算没有显卡，cpu也是可以充当处理图形的作用的)

