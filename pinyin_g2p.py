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

# ret = pypinyin.slug("hahahuanshi",style=pypinyin.FINALS,separator=' ')
ret = pconverter.to_finals("yong",strict=False)
print(ret,initials.convert("wo",strict=False))



def pinyin_g2p(text):
    print(text)
    plist = text.split(' ')
    list = []
    for p in plist:
        if p in [',','.','"','!',':']:
            list.pop()
            list.append(p)
        else:
            list.extend((i for i in [initials.convert(p,strict=False),pconverter.to_finals(p,strict=False),' '] if i != ''))
    if list[-1] == ' ':
        list.pop()
    print(list)
        

pinyin_g2p('mei cuo , jiu shi che men . ling wai liang ge ren wen ta shuo')