from urllib import request
import urllib
import random
import re

'''有道翻译的可用url (目标网址的可用的url 要自己去试出来，或者去网上找)
http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
删掉 _o'''
url=r"http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 伪装成浏览器
agent1="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"

agent2="Mozilla/5.0 (Linux; Android 8.1; PAR-AL00 Build/HUAWEIPAR-AL00; wv)AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools"

agent3="Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools"

agent4="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 UWS/2.11.1.50 Mobile Safari/537.36 AliApp(DingTalk/4.5.8) com.alibaba.android.rimet/10380049 Channel/227200 language/zh-CN"

agent5="Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI MT1-U06 Build/HuaweiMT1-U06)AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_2.7.3_diordna_8021_027/IEWAUH_61_2.1.4_60U-1TM+IEWAUH/7300001a/91E050E40679F078E51FD06CD5BF0A43%7C5441760104729681"

list1=[agent1,agent2,agent3,agent4,agent5]
agent=random.choice(list1)


header={"User-Agent":agent}




key="累得一塌糊涂的时候我首先想到的是跑步，跑完以后，累的是腿和脚，但心和脑子都缓过来了"
#post 请求需要提交的数据
fromdata={
	"i":key,
	"from":"AUTO",
	"to":"AUTO",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"15865727408392",
	"sign":"a6ab4cd2a7fb6cc953fe30150d60a3eb",
	"ts":"1586572740839",
	"bv":"cada6a23622e509aaf65f7d7561e2c33",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_REALTlME"
}
#转码
data=urllib.parse.urlencode(fromdata).encode(encoding='utf-8')	# 用utf-8的形式进行编码


# 构造请求对象
req=request.Request(url,data=data,headers=header)

# 接收响应
response=request.urlopen(req).read().decode()

# 正则表达式（提取"tgt": 和 }]]}中间的任意内容）
pat=r'"tgt":"(.*?)"}]]}'
result=re.findall(pat,response)		# result 是一个列表


print(result[0])