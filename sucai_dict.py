#coding: utf-8

import os
import os.path as osp
from xpinyin import Pinyin
import pypinyin
from pypinyin.style import (  # noqa
        initials,
        finals
    )
pconverter = finals.FinalsConverter();
# pinyin = Pinyin()
# ret = pinyin.get_pinyin(u"还钱还有",' ', tone_marks=None)
# print(ret)

attrs2 = [
    'train','evaluation','test'
]

with open("./word_index_dict.txt", 'r' ) as f:
    text_list = f.readlines()

_data_list = [l[:-1].split(',') for l in text_list]
i = 0
for data in _data_list:
    print(data[0]+","+str(i))
    i=i+1


exit()
