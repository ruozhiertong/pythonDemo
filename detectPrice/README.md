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


