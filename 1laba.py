import requests
import re
urls = ['http://www.csd.tsu.ru/']
mails =[]
startUrl = 'http://www.csd.tsu.ru/'
d=0
def  findEmails (pageUrl):    
    global urls
    global d
    global mails
    d +=1
    response= requests.get(pageUrl)
    if response.status_code == 200: 
        result = re.findall('href="(.*?)"',response.text)
        result2 = re.findall (r"[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}",response.text)
        urlsNew = list(set(result))
        mailsNew = list(set(result2))
        for mail in mailsNew:
            mails.append(mail)
        if len(urlsNew) >0:
            for url in urlsNew:
                if url.find('mail') !=-1:
                    url = url[7:]
                    if url not in urls :
                        urls.append(url)
                elif len(url)>0  and url[0]=='#':
                    url='http://www.csd.tsu.ru/'+url
                    if url not in urls :
                        urls.append(url)
                else:     
                    if url not in urls:
                        urls.append(url)
                        if url[:18]=='http://www.csd.tsu' and dp<=1 and url.find('mode')==-1:
                            findEmails (url)
                            d -=1
findEmails (startUrl)
mails= set(mails)
for u in mails:
    print (u)

