from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://stats.espncricinfo.com/ci/engine/records/averages/batting.html?class=1;id=2;type=team'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


data1 = page_soup.findAll("tr",{"class":"data1"})

filename = "australia_test_batting.csv"
f = open(filename, "w")

headers = "span", "matches","innings", "NO", "runs", "HS", "ave", "century", "half_century", "duck\n"

f.write("headers")
for el in data1:
  span = el.td.next_sibling.next_sibling.next_element

  matches = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  innings = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  NO = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  runs = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  HS = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  ave = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  century = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  half_century = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  duck = el.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_element

  print("span: " + span)
  print("matches: " + matches)
  print("innings: " + innings)
  print("NO's: " + NO)
  print("runs: " + runs)
  print("High Score: " + HS)
  print("average: " + ave)
  print("100s: " + century)
  print("50s: " + half_century)
  print("0s: " + duck)

  f.write(span + "," + matches + "," + innings + "," + NO + "," + runs + "," + HS + "," + ave + "," + century + "," + half_century + "," + duck + "\n")

f.close()
