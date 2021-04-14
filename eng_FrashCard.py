import random
import csv
from pprint import pprint

from termcolor import colored

with open(r'C:\Users\hachimi\python\EnglishWord\language.csv', encoding="utf-8") as f:
  reader = csv.reader(f)
  dict_from_csv = {rows[0]: rows[1] for rows in reader}

template = '*'*15 + '\n英単語:{}\n' + '*'*15

while True:
  # 英単語表示
  word = random.choice(list(dict_from_csv.keys()))
  print(colored(template.format(word), 'yellow'))
  # 日本語入力
  ans = input("日本語を入力：")
  print()
  # 答え合わせ
  if ans == '0':
    print("お疲れさまでした！")
    print()
    break
  elif ans == dict_from_csv[word]:
    print(colored("正解!", "green"))
    print()
  else:
    print(colored("不正解。","red"))
    print("正解は：",dict_from_csv[word])
    print()