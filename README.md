# MySpider #

----------
> 完成了前两项，并且还在优化

1. 爬取页面
2. 数据分析
3. 代理
4. 多进程
5. 验证识别
6. 分布式

## Usage ##
**-e method n1 n2**<br/>
method:*screen* 和 *file* 是method的两种方法.*screen* 意思是输出到屏幕,*file* 意思是输出到文件.<br/>
n1,n2:在第n1个url到第n2个url上应用method<br/>
eg. -e screen 1 13 意思是输出第1个到第13个url的结果到屏幕<br/>
**默认method是screen,并且输出所有组**<br/><br/>


**-c n1 n2 n3**<br/>
n1,n2,n3:获取第n1个url返回的cookies并传递给第n2个url到第n3个url
eg. -c 3 14 16 意思是将第3个url获取的cookies作为headers参数传给第14，15，16个url<br/><br/>


**-x name_of_xls, name_of_sheet, column, title[]**<br/>
nameofxls:xls文件名<br/>
nameofsheet:表单名<br/>
column:列数<br/>
title:一个list，存放每一列开头的title<br/>
eg. -x student_score.xls score 4 name,age,gender,score



