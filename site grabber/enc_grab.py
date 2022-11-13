import requests,re,os,random
import socket
def cls():
	os.system(['clear', 'cls'][(os.name == 'nt')])
cls()
try:
	import concurrent.futures
	#xxx = True
except:
	from multiprocessing.pool import ThreadPool
	#xxx = False
red = '\x1b[31m'
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
RIPON = False
def Ret(x):
	try:
		return raw_input(x)
	except:
		return input(x)
logo = """ 
  __  __        ____  _____  _  _______  ___   ___  
 |  \/  |      |  _ \|  __ \| |/ /  __ \|__ \ / _ \ 
 | \  / |_ __  | |_) | |  | | ' /| |__) |  ) | (_) |
 | |\/| | '__| |  _ <| |  | |  < |  _  /  / / > _ < 
 | |  | | |_   | |_) | |__| | . \| | \ \ / /_| (_) |
 |_|  |_|_(_)  |____/|_____/|_|\_\_|  \_\____|\___/ 
                                                    
                                                                                                             
 """
print(r+logo+"""\n    {}I Don't Aspect Any Responsibility For Bad Ussage!{}\n\n Author: {}The Mr. BDKR28{}\n Name: {}The Bing BOT{}\n Application: {}Python 2.7 & 3.9 Supported{}\n Chose a Tool:{}\n  1. Bing Weblist Grabber Tool\n  2. Bing Reversip Tool (Unlimited)\n  3. Live IP Check + IP From Domain\n  4. Bing Normal Dorking\n  5. IP Ranger + Ip Live
 """.format(g,y,c,y,c,y,c,m,w))
user_agent_list = [
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.95',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36']
try:
	domain = open("domain.txt","r").read().splitlines()
except:
	domain = ["ac","ad","ae","af","ag","ai","al",
"am","an","ao","aq","ar","as","at","au","aw","ax","az","ba","bb","com"
"bd","be","bf","bg","bh","bi","bj","bm","bn","bo",
"br","bs","bt","bv","bw","by","bz","ca","cc","cd",
"cf","cg","ch","ci","ck","cl","cm","cn","co","cr",
"cu","cv","cx","cy","cz","de","dj","dk","dm","do",
"dz","ec","ee","eg","eh","er","es","et","eu","fi",
"fj","fk","fm","fo","fr","ga","gb","gd","ge","gf",
"gg","gh","gi","gl","gm","gn","gp","gq","gr","gs",
"gt","gu","gw","gy","hk","hm","hn","hr","ht","hu",
"id","ie","il","im","in","io","iq","is","it",
"je","jm","jo","jp","ke","kg","kh","ki","km","kn",
"kp","kr","kw","ky","kz","la","lb","lc","li","lk",
"lr","ls","lt","lu","lv","ly","ma","mc","md","me",
"mg","mh","mk","ml","mm","mn","mo","mp","mq","mr",
"ms","mt","mu","mv","mw","mx","my","mz","na","nc",
"ne","nf","ng","ni","nl","no","np","nr","nu","nz",
"om","pa","pe","pf","pg","ph","pk","pl","pm","pn",
"pr","ps","pt","pw","py","qa","re","ro","rs","ru",
"rw","sa","sb","sc","sd","se","sg","sh","si","sj",
"sk","sl","sm","sn","so","sr","st","su","sv","sy",
"sz","tc","td","tf","tg","th","tj","tk","tl","tm",
"tn","to","tp","tr","tt","tv","tw","tz","ua","ug",
"uk","um","us","uy","uz","va","vc","ve","vg","vi",
"vn","vu","wf","ws","ye","yt","za","zm","zw","com",
"net","org","biz","gov","mil","edu","info","int","tel",
"name","aero","asia","cat","coop","jobs","mobi","museum",
"pro","travel"]
def rez(url,exploit,n):
	if "|" in exploit:
		arr = exploit.split("|")
		if n == "1":
			print(w+" ["+g+"+"+w+"] "+g+arr[0]+": "+w+url+y+" | "+arr[1].strip()+" | "+arr[2].strip()+g+" [YES]")
		else:
			print(w+" ["+r+"+"+w+"] "+r+arr[0]+": "+w+url+y+" | "+arr[1].strip()+" | "+arr[2].strip()+r+" [NO]")
	else:
		if n == "1":
			print(w+" ["+g+"+"+w+"] "+g+exploit+": "+w+url+g+" [YES]")
		else:
			print(w+" ["+r+"+"+w+"] "+r+exploit+": "+w+url+r+" [NO]")
def SpeedX(check,list,th):
	if x == True:
		try:
			with concurrent.futures.ThreadPoolExecutor(int(th)) as executor:
				executor.map(check,list)
		except Exception as e:
			print(e)
	else:
		pool = ThreadPool(int(th))
		pool.map(check,list)
		pool.close()
		pool.join()
def saved(x,y):
	i = x
	i = i.replace("http://","")
	i = i.replace("https://","")
	i = i.replace("www.","")
	i = i.split("/")
	i = i[0]
	try:
		m = open(y,"r").read()
	except:
		open(y,"w")
		m = open(y,"r").read()
	if i in m:
		if "." in i:
			rez(x,"Added","1h")
		pass
	else:
		if "." in x:
			rez(x,"Added","1")
			open(y,"a").write(x+"\n")
def check(url):
	pdf = ".pdf"
	string = "." in url
	try:
		file = open(filename,"r").read()
	except:
		open(filename,"w")
		file = open(filename,"r").read()
	if url in file or pdf in url or string == False:
		if "." in url:
			rez(url,"Added","41")
	else:
		file = open(filename,"a")
		file.write(url+"\n")
		file.close()
		rez(url,"Added","1")
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
