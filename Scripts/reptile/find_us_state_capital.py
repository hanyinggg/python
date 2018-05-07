# coding : utf-8

import re

with open('E:\\Scripts\\US_state_capital.txt') as fp:
    us_text = fp.read()
fp.close()

RE_words = re.compile(r'[A-Z][a-z]+\.?\s?')
us_list = re.findall(RE_words, us_text)
state_list = [us_list[i] for i in range(0, len(us_list), 2)]
capital_list = [us_list[i] for i in range(1, len(us_list), 2)]

if __name__ == '__main__':
    print(state_list)
    print(capital_list)
    print(len(state_list))
    print(len(capital_list))