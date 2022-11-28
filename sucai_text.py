#coding: utf-8

import os
import os.path as osp

attrs = {
    '惊喜':'Surprise',
    '中立':'Neutral',
    '生气':'Angry',
    '快乐':'Happy',
    '伤心':'Sad'
}

attrs2 = [
    'train','evaluation','test'
]

with open("../sucai/0008/0008.txt", 'r' ,encoding='utf16') as f:
    text_list = f.readlines()

_data_list = [l[:-1].split('\t') for l in text_list]
for data in _data_list:
    if len(data) == 3:
        for p in attrs2:
            wave_path = '../sucai/0008/'+attrs[data[2]]+'/'+p+'/'+data[0]+'.wav'
            if os.path.exists(wave_path):
                # print(wave_path)
                data[0] = wave_path;
                break
# print(_data_list)    
_data_list = [data[0]+'|'+data[1]+'|'+'8' for data in _data_list if len(data) == 3 ]
print(_data_list)
with open("../sucai/train_list.txt", 'a' ,encoding='utf8') as f:
    f.write('\n'.join(_data_list)+'\n')