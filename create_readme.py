import requests
from bs4 import BeautifulSoup
try: 
	from pipreqs import pipreqs
	import os
	os.chdir(os.getcwd()+'\\Code\\')
	pipreqs.main()
	requirements_file = True

except :
	requirements_file = False


######

url = 'https://algotrading101.com/learn/alpaca-trading-api-guide/'

######

def callsite(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    if resp.status_code is 200:
        return BeautifulSoup(resp.content, 'html.parser')

soup = callsite(url)

toc = []
for item in soup.findAll('h2'):
    if item.get('id'):
        toc.append([item.get_text(), item.get('id')])

mlist = []
mlist.append('=' * len(soup.title.text))
mlist.append(soup.title.text)
mlist.append('=' * len(soup.title.text))
mlist.append('')
title = soup.title.text.split('-')[0]
mlist.append(f'This is the code used in `{title}<{url}>`_ published on the Algotrading101 Blog') 
mlist.append('')

toc_string = 'Table of Contents'
mlist.append('-'*len(toc_string))
mlist.append(toc_string)
mlist.append('-'*len(toc_string))   
mlist.append('')
for toc_line in toc:
    mlist.append(f'* `{toc_line[0]}  <{url}#{toc_line[1]}>`_')
mlist.append('')

dependencies = 'Requirements'
mlist.append('-'*len(dependencies))
mlist.append(dependencies)
mlist.append('-'*len(dependencies))
mlist.append('')
mlist.append('* `python <https://www.python.org>`_ >= 2.7, 3.4+')

if requirements_file:
	#try to automatically fill from requirements.txt
	try:
		with open('requirements.txt', 'r', encoding='utf-8') as e:
			reqs = e.readlines()
		for req_line in reqs:
			req_split = (req_line.split('=='))
			mlist.append(f'* `{req_split[0]} <url_goes_here>`_ (tested to work with >= {req_split[1][:-1]} )')
	except:
		requirements_file = False
else:
	for _ in range(5):
	    mlist.append('* `Library_name_goes_here <url_goes_here>`_ (tested to work with >= version_number_here )')

mlist.append('')
author = 'Author Info'
mlist.append('-'*len(author))
mlist.append(author)
mlist.append('-'*len(author))
mlist.append('')
author_info = soup.find('a',{'class':'text-capitalize link-dark'})
pub_time = soup.find('meta',{'property':'article:published_time'}).get('content')
pub_time = pub_time.split('T')[0]
mlist.append(f':author: {author_info.contents[0][1:]}')
mlist.append(f':author page: {author_info["href"]}')
mlist.append(f':published: {pub_time}')

with open('readme.rst', 'w', encoding='utf-8') as f:
    for line in mlist:
        f.write(line+'\n')
