from urllib import request
import urllib
import time
import random

# 构建请求头信息 伪装 user agent
agent1="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"

agent2="Mozilla/5.0 (Linux; Android 8.1; PAR-AL00 Build/HUAWEIPAR-AL00; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools"

agent3="Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools"

agent4="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 UWS/2.11.1.50 Mobile Safari/537.36 AliApp(DingTalk/4.5.8) com.alibaba.android.rimet/10380049 Channel/227200 language/zh-CN"

agent5="Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI MT1-U06 Build/HuaweiMT1-U06)AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_2.7.3_diordna_8021_027/IEWAUH_61_2.1.4_60U-1TM+IEWAUH/7300001a/91E050E40679F078E51FD06CD5BF0A43%7C5441760104729681"

list1=[agent1,agent2,agent3,agent4,agent5]
agent=random.choice(list1)

header={"User-Agent":agent}


'''#  分析过程 分析 url 的规律 （很重要）
https://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5&traceid=	# 第一页	(1-1)*50

https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50		#第二页  (2-1)*50

https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100		#第三页	(3-1)*50

https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150		#第四页	(4-1)*50'''

'''for i in range(1,4):
	print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50))	#str()  将 数字转换为 str 型'''

# 构建贴吧 Spider（蜘蛛，爬虫）方法

def loadpage(fullurl,filename):
	print("正在下载：",filename)
	req=request.Request(fullurl,headers=header)
	reponse=request.urlopen(req).read()
	return reponse


def writepage(html,filename):
	print("正在保存：",filename)

	# 将获取到的网页信息（html）以二进制形式写入本地（filename）
	with open(filename,"wb") as f:
		f.write(html)

		print("-------------------------------")




def tiebaSpider(url,begin,end):
	for page in range(begin,end+1):
		pn=(page-1)*50	
		fullurl=url+"&pn="+str(pn)	# 每次请求的完整的 url
		filename=r"C:\Users\Administrator\Desktop\Python\python爬虫结果/第"+str(page)+"页.html"		# 每次请求后保存到本地的文件名

		html=loadpage(fullurl,filename)		#调用爬虫，爬取网页 load: 负载
		writepage(html,filename)		#把获取到的网页信息写入本地



if __name__ == '__main__':
	kw=input("请输入要爬取的贴吧名：")
	begin=int(input("请输入起始页："))
	end=int(input("请输入结束页："))

	# 构建 url 编码
	url="http://tieba.baidu.com/f?"
	key=urllib.parse.urlencode({"kw":kw})
	url=url+key

	tiebaSpider(url,begin,end)

	time.sleep(10)