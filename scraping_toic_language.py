from bs4 import BeautifulSoup

import requests
import pandas as pd
from pprint import pprint

url = 'https://toiguru.jp/toeic-vocabulary-list#smoothplay{}'

target_url = url.format(1)
#print(target_url)

r = requests.get(target_url)

soup = BeautifulSoup(r.text)

contents = soup.find_all('table', class_='wp-block-table has-fixed-layout')

content = contents[0]

words = content.find('tbody')

word_two = words.find_all('tr')

word_ones = word_two[0]

word = word_ones.find('td')

lang = (word.get_text(',').split(','))
eng = lang[0]
japa = lang[1]
#print(eng, japa)

d = {
  'English': eng,
  'Japanese': japa
}
# print(d)

d_list = []
contents = soup.find_all('table', class_='wp-block-table has-fixed-layout')
for content in contents:
  words = content.find('tbody')
  word_two = words.find_all('tr')
  for word_ones in word_two:
    word_one = word_ones.find_all('td')
    # print(word_one)
    try:
      for word in word_one:
        # print(word)
        lang = word.get_text(',').split(',')
        # print(lang)
        eng = lang[0]
        japa = lang[1]
        # print(japa)
        d = {
          'English': eng,
          'Japanese': japa
        }
        d_list.append(d)
    except IndexError as e:
      continue
    
df = pd.DataFrame(d_list)
# print(df.head())
df.to_csv('language.csv', index=None, encoding='utf-8-sig')