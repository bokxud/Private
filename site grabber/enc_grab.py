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
def ip(x):
	try:
		socket.setdefaulttimeout(10)
		url = socket.gethostbyname(x)
	except Exception as e:
		rez(x,"LIVED","n")
		return 5
	try:
		if RIPON == False:
			savefile = filename
		else:
			savefile = "all-ip.txt"
		file = open(savefile,"r").read()
	except:
		open(savefile,"w")
		file = open(savefile,"r").read()
	if url in file:
		pass
	else:
		file = open(savefile,"a")
		file.write(url+"\n")
		file.close()
		rez(url,"LIVED","1")
		if RIPON == True:
			ipdorker(url)
def liveips(ip):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(5)
		m = s.connect_ex((ip,80))
		if str(m) == "0":
			file = open(filename,"a")
			file.write(ip+"\n")
			file.close()
			rez(ip,"LIVED","1")
		else:
			rez(ip,"LIVED","g1")
	except Exception as e:
		rez(ip,"LIVED","n")
		return 5
def bing(dork):
	headers = {'user-agent': random.choice(user_agent_list)+str(random.choice(range(1000)))}
	for dom in domain:
		okkk = dork.strip()+' "'+dom
		first = 0
		try:
			for i in range(int(page1)):
				first = first+50
				params = {'q': okkk, 'count': '1000','first':first}
				url = "http://www.bing.com/search"
				result = requests.get(url,params=params,headers=headers,timeout=10)
				result = result.content.decode('utf-8')
				patern = r'<a href="(.*?)"'
				ok = re.findall(patern,result)
				for i in ok:
					if "go.microsoft.com" in i or "javascript:" in i or i == "\n":
						pass
					else:
						if RIPON == True:
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
									ip(i.replace("http://","").replace("https://","").split("/")[0])
						else:
							saved(i,filename)
		except Exception as e:
			print(e)
			bing(dork)
def IpRanger(ipx):
	store = ipx.split(".")[0]+"."+ipx.split(".")[1]
	for i in range(1,256):
		for y in range(1,256):
			liveips(str(store+"."+str(i)+"."+str(y)))
try:
	cmd = Ret(g+" [{}root{}@{}Mr. BDKR28{}:{}~{}]{}# {}".format(g,r,y,g,c,g,m,r))
except Exception as e:
	print(e)
	exit()
if cmd == "1":
	RIPON = True
	try:
		cls()
		print(r+logo+"""\n{}	Author:{} Mr. BDKR28\n	{}Name: {}Bing Weblist Grabber\n""".format(y,c,y,c))
		dorks = Ret(g+" DorkList"+w+":"+c+"~"+m+"# "+r)
		page1 = Ret(g+" Page Dork"+w+":"+c+"~"+m+"# "+r)
		page2 = Ret(g+" Page Reversip"+w+":"+c+"~"+m+"# "+r)
		filename = Ret(g+" Save File"+w+":"+c+"~"+m+"# "+r)
		th = Ret(g+" Threads"+w+":"+c+"~"+m+"# "+r)
		dork = open(dorks,"r").read().splitlines()
		cls()
		SpeedX(bing,dork,th)
	except Exception as e:
		print(e)
		exit()
if cmd == "2":
	try:
		cls()
		print(r+logo+"""\n{}	Author:{} Mr. BDKR28\n	{}Name: {}Bing Unlimited Reversip\n""".format(y,c,y,c))
		dorks = Ret(g+" IpList"+w+":"+c+"~"+m+"# "+r)
		page2 = Ret(g+" Page Reversip"+w+":"+c+"~"+m+"# "+r)
		filename = Ret(g+" Save File"+w+":"+c+"~"+m+"# "+r)
		th = Ret(g+" Threads"+w+":"+c+"~"+m+"# "+r)
		dork = open(dorks,"r").read().splitlines()
		cls()
		SpeedX(ipdorker,dork,th)
	except Exception as e:
		print(e)
		exit()
if cmd == "3":
	try:
		cls()
		print(r+logo+"""\n{}	Author:{} Mr. BDKR28\n	{}Name: {}Grab Weblist To Ip\n""".format(y,c,y,c))
		dorks = Ret(g+" EnterList"+w+":"+c+"~"+m+"# "+r)
		filename = Ret(g+" Save File"+w+":"+c+"~"+m+"# "+r)
		th = Ret(g+" Threads"+w+":"+c+"~"+m+"# "+r)
		dork = open(dorks,"r").read().splitlines()
		cls()
		SpeedX(ip,dork,th)		
	except Exception as e:
		print(e)
		exit()
if cmd == "4":
	try:
		cls()
		print(r+logo+"""\n{}	Author:{} Mr. BDKR28\n	{}Name: {}Bing Basic Dorker\n""".format(y,c,y,c))
		dorks = Ret(g+" DorkList"+w+":"+c+"~"+m+"# "+r)
		page1 = Ret(g+" Page Dork"+w+":"+c+"~"+m+"# "+r)
		filename = Ret(g+" Save File"+w+":"+c+"~"+m+"# "+r)
		th = Ret(g+" Threads"+w+":"+c+"~"+m+"# "+r)
		dork = open(dorks,"r").read().splitlines()
		cls()
		SpeedX(bing,dork,th)
	except Exception as e:
		print(e)
		exit()
if cmd == "5":
	try:
		cls()
		print(r+logo+"""\n{}	Author:{} Mr. BDKR28\n	{}Name: {}Ip Ranger + Live Checker\n""".format(y,c,y,c))
		dorks = Ret(g+" IpList"+w+":"+c+"~"+m+"# "+r)
		filename = Ret(g+" Save File"+w+":"+c+"~"+m+"# "+r)
		th = Ret(g+" Threads"+w+":"+c+"~"+m+"# "+r)
		dork = open(dorks,"r").read().splitlines()
		cls()
		SpeedX(IpRanger,dork,th)
	except Exception as e:
		print(e)
		exit()
else:
	cls()
	print(g+" [+] Tool Closed Successfully [+]")
