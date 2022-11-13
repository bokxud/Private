def ipdorker(dork):
    headers = {'user-agent': random.choice(user_agent_list)+str(random.choice(range(1000)))}
    okkk = dork
    first = 0
    try:
        for i in range(int(page2)):
            first = first+50
            url = "http://www.bing.com/search?q=ip%3A%22"+okkk+"%22&count=1000&first="+str(first)
            result = requests.get(url,headers=headers,timeout=50)
            result = result.content.decode('utf-8')
            patern = r'<a href="(.*?)"'
            ok = re.findall(patern,result)
            for i in ok:
                i = i.replace("<strong>","")
                i = i.replace("</strong>","")
                i = i+"/"
                if "http://" in i:
                    i = "http://"+re.findall("http://(.*?)/",i)[0]
                elif "https://" in i:
                    i = "https://"+re.findall("https://(.*?)/",i)[0]
                else:
                    i = "http://"+re.findall("http://(.*?)/",'http://'+i)[0]
                if "go.microsoft.com" in i or "javascript:" in i or i == "\n":
                    pass
                else:
                    if "." in i:
                        check(i)                        
    except Exception as e:
        print(e)
        ipdorker(dork)
