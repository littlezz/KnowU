To DO
=============

- use django-ajax  --------------done
- finish algorithm to get a article  -----------done
- complete the tag manage, form or ajax? --------done
- 测试ajax是否有上下文变量 ------------------------ done
- 使用 django compress
- 测试接受ajax的post ------done
- 使用through  ----------done
- form ajax
- 收藏--=>+ --------done
- favour ------done
- 收藏页面 ----------done
- 去除看过的页面在AlgorithmX中


优化
---------
- 用select cache 住article的attr  
- 重构数据库,整合book和favour到intermediate model

记录
=============
django-ajax 提供的ajaxPost方法自带了csrf, 但是使用的时候在view中接受的函数必须@ajax,不然出错.  
对于get, 因为没有csrf的要求,所以jquery 或ajaxGet都可以.  
使用了提供的ajax函数时后端必须有对应的@ajax, 不然出错.

through  
> The only way to create this type of relationship is to create instances of the intermediate model.  

对已有数据的m2m添加through 时要清空数据,应为基础的add和remove已经失效了.  

利用filter().first 决定是否存在. 不存在会返回None