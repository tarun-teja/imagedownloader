from urllib.request import urlopen
import re
from bs4 import BeautifulSoup



resp=urlopen("http://ipecomics.net/xxx-apartments-episode-10-the-cure-for-writers-block/");

page=resp.read()
soup=BeautifulSoup(page)

tgg=soup.find_all('img')
opener = urllib.request.FancyURLopener({})
headers = { 'User-Agent' : 'Mozilla/5.0' }
#opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
j=0;
for line in tgg :
	#print(line)
	opener.retrieve(line,str(j)+".jpg")
	j=j+1;
