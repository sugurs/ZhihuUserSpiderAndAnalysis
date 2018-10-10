爬取得到的数据文件：data.json data.csv 爬取的知乎用户（56658个用户，每位用户一共43个字段的数据）数据文件，2种格式；
代码，包括爬虫代码和数据分析代码，内含注释；
分析结果图像；
分析结果数据文件；
一共爬取了43个字段的数据

scrapy命令：
scrapy startproject zhihuuser
cd zhihuuser
scrapy genspider zhihu www.zhihu.com
scrapy crawl zhihu

mongodb命令：
启动mongodb，指定数据库地址
mongod --dbpath e:\mongo_data\db
连接数据库
mongo
mongoexport --host 127.0.0.1:27017 -f _id,url_token,allow_message,answer_count,articles_count,avatar_url,avatar_url_template,badge,business,columns_count,educations,employments,favorite_count,favorited_count,follower_count,following_columns_count,following_count,following_favlists_count,following_question_count,following_topic_count,gender,headline,hosted_live_count,id,is_advertiser,is_blocking,is_followed,is_following,is_org,locations,name,participated_live_count,pins_count,question_count,thank_from_count,thank_to_count,thanked_count,type,url,user_type,vote_from_count,vote_to_count,voteup_count  --db zhihu --collection user --type=csv --out e:\data.csv

简介：
目前爬虫可以对于单个用户达到可以爬取43个相关的信息，只用设定起点用户。爬虫自动在全网进行爬取，并将所爬取到信息保存在mongodb的zhihu数据库user表的43个字段中：
{"_id":"5ad776c99dd2652f022570d1"
"url_token":"miloyip"
"allow_message":false
"answer_count":1597
"articles_count":52
"avatar_url":"https://pic2.zhimg.com/v2-2b63868f49fae3e47f5d65ce0951b38b_is.jpg"
"avatar_url_template":"https://pic2.zhimg.com/v2-2b63868f49fae3e47f5d65ce0951b38b_{size}.jpg"
"badge":[{"topics":[{"introduction":"计算机图形学（英语：computer graphics，缩写为CG）是研究计算机在硬件和软件的帮助下创建计算机图形的科学学科，是计算机科学的一个分支领域，主要关注数位合成与操作视觉的图形内容。"
"avatar_url":"https://pic1.zhimg.com/95b86ea8b502d9aef1b13f621bba2ef3_is.jpg"
"name":"计算机图形学"
"url":"http://www.zhihu.com/api/v4/topics/19613730"
"type":"topic"
"excerpt":"计算机图形学（英语：computer graphics，缩写为CG）是研究计算机在硬件和软件的帮助下创建计算机图形的科学学科，是计算机科学的一个分支领域，主要关注数位合成与操作视觉的图形内容。"
"id":"19613730"}
{"introduction":"游戏开发(Game Development)是将一系列关于娱乐体验上带有创造性的想法，以可运行的电子游戏为载体所实现的过程。传统电子游戏由开发商制作后交由发行商进行发行工作，而独立游戏则往往由规模较小的团队或个人进行开发工作。<br><br>游戏开发涉及了多个领域的知识，其团队通常也具有明确的分工，如游戏美术、游戏程序员、游戏策划、游戏测试等。开发游戏的过程通常会以阶段划分。在早期阶段主要确立游戏概念与游戏原型，在随后的开发过程中再将上述部分以工业化的高标准交予各个职责部门一一细化实现。在开发阶段完成以后，游戏还要经历市场推广和运营维护等必不可少的步骤，直到其生命周期结束。"
"avatar_url":"https://pic4.zhimg.com/130887c7689dc9631634a26a5f3df106_is.jpg"
"name":"游戏开发"
"url":"http://www.zhihu.com/api/v4/topics/19553361"
"type":"topic"
"excerpt":"游戏开发(Game Development)是将一系列关于娱乐体验上带有创造性的想法，以可运行的电子游戏为载体所实现的过程。传统电子游戏由开发商制作后交由发行商进行发行工作，而独立游戏则往往由规模较小的团队或个人进行开发工作。 游戏开发涉及了多个领域的知识，其团队通常也具有明确的分工，如游戏美术、游戏程序员、游戏策划、游戏测试等。开发游戏的过程通常会以阶段划分。在早期阶段主要确立游戏概念与游戏原型，在随后的开发过…"
"id":"19553361"}
{"introduction":"人们为了让计算机解决各种棘手的问题，使用编程语言<b>编写程序代码</b>并通过计算机运算得到最终结果的过程。"
"avatar_url":"https://pic1.zhimg.com/v2-4030982b9aed71d12b350a4c3ba5078d_is.jpg"
"name":"编程"
"url":"http://www.zhihu.com/api/v4/topics/19554298"
"type":"topic"
"excerpt":"人们为了让计算机解决各种棘手的问题，使用编程语言编写程序代码并通过计算机运算得到最终结果的过程。"
"id":"19554298"}
{"introduction":"C++是一种使用非常广泛的计算机程序设计语言。它是一种静态数据类型（static data type）检查的，支持多范式（multi-paradigm）的通用程序设计语言。C++支持面向过程编程（Procedures Programming）、数据抽象化（Data Abstraction）、面向对象程序设计（Object-Oriented Programming）、泛型程序设计（Generic-Type Programming）、基于原则设计（Policy-Based Class Design）等多种程序设计风格。 (from Wikipedia)"
"avatar_url":"https://pic1.zhimg.com/9db7191dc_is.jpg"
"name":"C++"
"url":"http://www.zhihu.com/api/v4/topics/19584970"
"type":"topic"
"excerpt":"C++是一种使用非常广泛的计算机程序设计语言。它是一种静态数据类型（static data type）检查的，支持多范式（multi-paradigm）的通用程序设计语言。C++支持面向过程编程（Procedures Programming）、数据抽象化（Data Abstraction）、面向对象程序设计（Object-Oriented Programming）、泛型程序设计（Generic-Type Programming）、基于原则设计（Policy-Based Class Design）等多种程序设计风格。 (from Wikipedia)"
"id":"19584970"}
{"introduction":"<b>计算机科学</b>（Computer Science
 CS）是系统性研究信息与计算的理论基础以及它们在计算机系统中如何实现与应用的实用技术的学科。<br> 它通常被形容为对那些创造、描述以及转换信息的算法处理的系统研究。计算机科学包含很多分支领域；其中一些，比如计算机图形学强调特定结果的计算，而另外一些，比如计算复杂性理论是学习计算问题的性质。还有一些领域专注于挑战怎样实现计算。比如程序设计语言理论学习描述计算的方法，而程序设计是应用特定的程序设计语言解决特定的计算问题，人机交互则是专注于挑战怎样使计算机和计算变得有用、可用，以及随时随地为<a href=\"http://zh.wikipedia.org/wiki/%E4%BA%BA\" data-editable=\"true\" data-title=\"人\">人</a>所用。<br><b>现代计算机科学( Computer Science)包含理论计算机科学和应用计算机科学两大分支。</b>"
"avatar_url":"https://pic2.zhimg.com/v2-2425584cf56e7caae35080a03010a30a_is.jpg"
"name":"计算机科学"
"url":"http://www.zhihu.com/api/v4/topics/19580349"
"type":"topic"
"excerpt":"计算机科学（Computer Science
 CS）是系统性研究信息与计算的理论基础以及它们在计算机系统中如何实现与应用的实用技术的学科。 它通常被形容为对那些创造、描述以及转换信息的算法处理的系统研究。计算机科学包含很多分支领域；其中一些，比如计算机图形学强调特定结果的计算，而另外一些，比如计算复杂性理论是学习计算问题的性质。还有一些领域专注于挑战怎样实现计算。比如程序设计语言理论学习描述计算的方法，而程序设计…"
"id":"19580349"}
{"introduction":""
"avatar_url":"https://pic4.zhimg.com/389f27418bb3b6e5baddb06b00d98f36_is.jpg"
"name":"游戏引擎"
"url":"http://www.zhihu.com/api/v4/topics/19556258"
"type":"topic"
"excerpt":""
"id":"19556258"}
{"introduction":"在数学和计算机科学之中，算法（Algorithm）为一个计算的具体步骤，常用于计算、数据处理和自动推理。精确而言，算法是一个表示为有限长列表的有效方法。算法应包含清晰定义的指令用于计算函数。<br><br>来自维基百科：<a href=\"http://zh.wikipedia.org/zh-cn/%E7%AE%97%E6%B3%95\" data-editable=\"true\" data-title=\"算法\" class=\"\">算法</a>"
"avatar_url":"https://pic1.zhimg.com/2e6276881_is.jpg"
"name":"算法"
"url":"http://www.zhihu.com/api/v4/topics/19553510"
"type":"topic"
"excerpt":"在数学和计算机科学之中，算法（Algorithm）为一个计算的具体步骤，常用于计算、数据处理和自动推理。精确而言，算法是一个表示为有限长列表的有效方法。算法应包含清晰定义的指令用于计算函数。 来自维基百科：算法 "
"id":"19553510"}]
"type":"best_answerer"
"description":"优秀回答者"}]
"business":{"introduction":""
"avatar_url":"https://pic3.zhimg.com/d74afc7906aa5209503de78978777997_is.jpg"
"name":"电子游戏"
"url":"http://www.zhihu.com/api/v4/topics/19554169"
"type":"topic"
"excerpt":""
"id":"19554169"}
"columns_count":2
"educations":[{"major":{"introduction":"是指探究人脑或心智工作机制的前沿性尖端学科，是20世纪世界科学标志性的新兴研究门类。"
"avatar_url":"https://pic4.zhimg.com/v2-a4c6a100b26256fc63a5e20d1141392a_is.jpg"
"name":"认知科学"
"url":"http://www.zhihu.com/api/v4/topics/19571430"
"type":"topic"
"excerpt":"是指探究人脑或心智工作机制的前沿性尖端学科，是20世纪世界科学标志性的新兴研究门类。"
"id":"19571430"}
"school":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"香港大学 (The University of Hong Kong)"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}}
{"major":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"系统工程及工程管理"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}
"school":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"香港中文大学 (Chinese University of Hong Kong)"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}}]
"employments":[{"company":{"introduction":"中国最大的互联网综合服务提供公司，主营以腾讯网、QQ、微信、腾讯微博、《英雄联盟》等为代表的互联网产品与网络游戏。主要依靠在线游戏、移动及电信增值服务、网络广告和电子商务交易创收。目前，QQ月活跃用户数7.8亿，移动及电信增值服务付费用户数超过3000万，腾讯微博注册用户数4.6亿。<br><br>2011年1月，腾讯推出手机应用「微信」进军移动互联网，并于2012年9月获得2亿用户，2013年1月15号用户数突破3亿。作为中国服务用户最多的互联网企业，实力强大的腾讯因对中小创业公司造成的竞争压力而常受诟病。<br><br>2004年6月，公司以「0700」为代码正式登陆香港股市。"
"avatar_url":"https://pic2.zhimg.com/127ee131a4487388e104da2bba7a4df6_is.jpg"
"name":"腾讯"
"url":"http://www.zhihu.com/api/v4/topics/19550757"
"type":"topic"
"excerpt":"中国最大的互联网综合服务提供公司，主营以腾讯网、QQ、微信、腾讯微博、《英雄联盟》等为代表的互联网产品与网络游戏。主要依靠在线游戏、移动及电信增值服务、网络广告和电子商务交易创收。目前，QQ月活跃用户数7.8亿，移动及电信增值服务付费用户数超过3000万，腾讯微博注册用户数4.6亿。 2011年1月，腾讯推出手机应用「微信」进军移动互联网，并于2012年9月获得2亿用户，2013年1月15号用户数突破3亿。作为中国服务用户最多的…"
"id":"19550757"}
"job":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"技术总监／专家工程师"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}}
{"company":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"Ubisoft"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}
"job":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"引擎工程师"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}}
{"company":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"麻辣马"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}
"job":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"资深工程师"
"url":"http://www.zhihu.com/api/v4/topics/19728025"
"type":"topic"
"excerpt":""
"id":"19728025"}}
{"company":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"香港理工大学 (PolyU)"
"url":"http://www.zhihu.com/api/v4/topics/"
"type":"topic"
"excerpt":""
"id":""}
"job":{"introduction":""
"avatar_url":"https://pic4.zhimg.com/e82bab09c_is.jpg"
"name":"项目主任"
"url":"http://www.zhihu.com/api/v4/topics/19749650"
"type":"topic"
"excerpt":""
"id":"19749650"}}]
"favorite_count":0
"favorited_count":145604
"follower_count":146839
"following_columns_count":54
"following_count":247
"following_favlists_count":2
"following_question_count":2094
"following_topic_count":91
"gender":1
"headline":"游戏程序员、《游戏引擎架构》译者"
"hosted_live_count":0
"id":"1e2c9261b85996ccc3c5436850127e33"
"is_advertiser":false
"is_blocking":false
"is_followed":false
"is_following":false
"is_org":false
"locations":[{"introduction":"香港是中华人民共和国两个特别行政区之一，位于南海北岸、以及珠江口东侧，北接广东省深圳市，西隔珠江与澳门及广东省珠海市相望，其余两面与南海邻接。全境由香港岛、九龙、新界、大屿山等4大区域组成，其中香港岛是全港的发展核心；地理环境上则由九龙半岛等大陆土地、以及263个岛屿构成，人口约723万人。 香港是全球重要的国际金融、服务业及航运中心之一，并以优良治安、自由经济、简单税制和健全的法律制度而闻名于世，素有“东方之珠”、“东方曼哈顿”等的美誉。“亚洲国际都会”是香港的官方品牌。"
"avatar_url":"https://pic4.zhimg.com/16bb6e1a3affb759dc37329349ac5258_is.jpg"
"name":"香港"
"url":"http://www.zhihu.com/api/v4/topics/19550842"
"type":"topic"
"excerpt":"香港是中华人民共和国两个特别行政区之一，位于南海北岸、以及珠江口东侧，北接广东省深圳市，西隔珠江与澳门及广东省珠海市相望，其余两面与南海邻接。全境由香港岛、九龙、新界、大屿山等4大区域组成，其中香港岛是全港的发展核心；地理环境上则由九龙半岛等大陆土地、以及263个岛屿构成，人口约723万人。 香港是全球重要的国际金融、服务业及航运中心之一，并以优良治安、自由经济、简单税制和健全的法律制度而闻名于世，素有…"
"id":"19550842"}]
"name":"Milo Yip"
"participated_live_count":2
"pins_count":104
"question_count":26
"thank_from_count":0
"thank_to_count":0
"thanked_count":31344
"type":"people"
"url":"http://www.zhihu.com/api/v4/people/1e2c9261b85996ccc3c5436850127e33"
"user_type":"people"
"vote_from_count":0
"vote_to_count":0
"voteup_count":231008}

