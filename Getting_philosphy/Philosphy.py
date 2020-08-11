'''''this program is used to web scraped Wikipedia to prove 
that all wikipedia articles are connected to philposphy '''

import urllib
import requests
from bs4 import BeautifulSoup
import time



urlpath = " https://en.wikipedia.org/wiki/Special:Random "
target="https://en.wikipedia.org/wiki/Philosophy"
#urlpath="https://en.wikipedia.org/wiki/"


def get_first_link(urlpath):
  html_text = requests.get(urlpath).text
  soup = BeautifulSoup(html_text, 'html.parser')
  print(soup.title)
  txt=soup
  new_link = None
  temp =txt.body.find_all('p')[0]
  start_count = 0
  started = False
  found = False
  #print(temp)
  if temp.find('a', recursive=False):
      new_link = temp.find('a', recursive=False).get('href')

  if not new_link:
   return
  #print(new_link)
  first_link_to_go=urllib.parse.urljoin('https://en.wikipedia.org',new_link)
  #print(first_link_to_go)
  return first_link_to_go



def trace_philosophy(visited_links,target,max_step=25):
    if visited_links[-1]==target:
      print('We found Philosphy article')
      return False
    elif visited_links[-1] in visited_links[:-1]:
        print('Had be vistird soon , End searching')
        return False
    elif len(visited_links)>max_step:
        print('It takes to much time to search ')
        return False
    else:
        return True

article_chain=[urlpath]
while trace_philosophy(article_chain,target):
    print(article_chain[-1])
    first_link=get_first_link(article_chain[-1])
    if not first_link:
        print('No Found Link ,End searching')
        break
    article_chain.append(first_link)


time.sleep(0.5)
