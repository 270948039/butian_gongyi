#coding=utf-8
#write by D12ea1v1
#headers:cookie处要改成登陆后的cookie
import json
import requests
import re
import time
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
headers={'Host': 'butian.360.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://butian.360.cn/Reward/pub//Message/send',
        'Cookie': 'test_cookie_enable=null; __huid=11Zcl/1/lKmx6PbXQGBJYVayCgnJpLkxgXg8KxHRlXlng=; __guid=91251416.891213319892077700.1510305171079.742; UM_distinctid=1637162aad14dd-0376416945c0e4-737356c-144000-1637162aad3747; __gid=156009789.54661236.1530255275644.1539307026296.49; Q=u%3D360H1454736369%26n%3D%26le%3DZwpjBGD4ZQZ5WGDjpKRhL29g%26m%3DZGH2WGWOWGWOWGWOWGWOWGWOAGZm%26qid%3D1454736369%26im%3D1_t01102aee3bcb96d1c2%26src%3Dpcw_webscan%26t%3D1; __utmz=138613664.1539371446.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=138613664.1705114460.1539371446.1539371446.1539390330.2; T=s%3Dae51b9ab49d7dff669efc63c9cbd9b29%26t%3D1539852129%26lm%3D%26lf%3D2%26sk%3D1c6dd91953322b3251f450fa7e3a545d%26mt%3D1539852129%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=eopkaas3r8bdf2grka4gef8067; __DC_sid=138613664.1205322143018757000.1540467244637.9763; ccpassport=2356f143ccbc47a08ce9ac3342470008; wzwsconfirm=bf7fe7a87398ebf054b7771433bb783f; wzwstemplate=Mg==; test_cookie_enable=null; wzwschallenge=-1; wzwsvtime=1540471781; __DC_monitor_count=130; __DC_gid=156009789.54661236.1530255275644.1540471794973.3011; __q__=1540471801572',
        'Connection': 'keep-alive'
        }
        #共74页
company_id_list=[]
target_list=[]
for i in range(1,74):
    #time.sleep(3)#防止过快
    data={'p':i,'s':1}
    res = requests.post('http://butian.360.cn/Reward/pub', data=data,headers=headers,timeout=(4,20))
    allResult = {}
    allResult = json.loads(res.text)
    #获取每一页的个数
    pagenum=len(allResult['data']['list'])
    #print pagenum
    for ii in range(pagenum):
        company_id = allResult['data']['list'][ii]['company_id']#遍历每个厂商id
        company_id_list.append(company_id)
        #print company_id

#提交漏洞页面，获取url
list_len=len(company_id_list)
file=r'd:\target_url.txt'
with open(file,'a+') as f:
    for i in company_id_list:
        time.sleep(2)
        res = requests.get('https://butian.360.cn/Loo/submit?cid='+i,headers=headers,timeout=(4,20))
        soup = BeautifulSoup(res.text,from_encoding='utf-8')
        url=soup.find('input',{'name':'host'}).get('value')
        print soup.find('input',{'name':'host'}).get('value')
        target_list.append(url)
        f.write(url.encode('utf-8')+'\n')
        #print soup.find('input',{'name':'host'}).get('value')
        #zz=r'<input class="input-xlarge" type="text" name="host".*?value="(.*?)">'
        #mm=re.findall(zz,res.text,re.S|re.M)
        #print mm
#write file target_url.txt
f.close()