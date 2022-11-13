import requests,re,os,random
import socket
def main(link):
 res = requests.get(link).content.decode()
 exec(res)
#main("https://raw.githubusercontent.com/bokxud/zone-h-notify/main/zoneh.py")
main("your tools raw link")