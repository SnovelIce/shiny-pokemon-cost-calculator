import requests
from bs4 import BeautifulSoup
import re
# /html/body/div[4]/div[4]/div[2]/div[1]/div[2]/ul
# //*[@id="srp-river-results"]/ul
pokeName = input('The shiny pokemon:')
EbURL = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=pokemon+go+shiny+{pokeName}&_sacat=0&LH_TitleDesc=0&_odkw=pokemon+go+shiny+mew&_osacat=0'

EHtml = str(requests.get(EbURL).content)
contX = BeautifulSoup(EHtml,features="lxml")
contXSells = contX.find_all("ul", {"class": "srp-results srp-list clearfix"})

costList = []

def AllTogetter(CL):
  CAll = 0
  for i in CL:
   CAll = i + CAll
  return(CAll)

def printCost(i):
 if len(i.find_all("span", {"class": "s-item__price"})) != 0:
    Cost = str(i.find_all("span", {"class": "s-item__price"})[0])
    Cost = Cost.replace('<span class="s-item__price"><!--F#f_0--><!--F#f_0-->',' ')
    Cost = Cost.replace('<!--F/--><!--F/--></span>',' ')
    Cost = Cost.replace('<span class="DEFAULT">',' ')
    Cost = Cost.replace('</span><!--F/--><!--F#f_0-->',' ')
    Cost = Cost.replace('<!--F/--><!--F#f_0-->',' ')
    p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'
    if re.search(p, Cost) is not None:
     for catch in re.finditer(p, Cost):
       if ',' not in catch[0]:
        costList.append(float(catch[0]))
        break
         

    


for i in contXSells[0]:
 if len(i.find_all("span", {"role": "heading"})) != 0:
  if 'lv' not in pokeName:
   if  'lv' not in str(i.find_all("span", {"role": "heading"})[0]) or 'level' not in str(i.find_all("span", {"role": "heading"})[0]):
    printCost(i)
  else:
   if  str(i.find_all("span", {"role": "heading"})[0]).count('lv') < 2 or str(i.find_all("span", {"role": "heading"})[0]).count('level') < 2:
    printCost(i)
print(costList)
print('In avr of: ' + str(AllTogetter(costList)/len(costList)) + ' Shekels')
#print(BeautifulSoup.prettify())
#print(contXSells)

