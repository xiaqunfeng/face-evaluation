import random
import re
import json
import codecs

# create a list with member 0~999999
lst = range(1000000)

# get relationship of scene and idcard
scene_num = 0
dict_scene = {}
scene = "../../xqf/face_code_book/scene_file.txt"
idcard = "../../xqf/face_code_book/id_card_file.txt"
with open(scene, 'rt') as f:
    for line in f:
        img_name = line.split(' ')[0]
        img_index = re.split(r'[\s]', line)[1]
        dict_scene[img_index] = img_name
        scene_num += 1

dict_idcard = {}
with open(idcard, 'rt') as f:
    for line in f:
        img_name = line.split(' ')[0]
        img_index = re.split(r'[\s]', line)[1]
        dict_idcard[img_name] = img_index

dict_res = {} # scene_index : idcard_index
for i in range(scene_num):
    dict_res[i] = dict_idcard[dict_scene[str(i)]]
    # remove from lst
    #del lst[int(dict_res[i])]
    lst.remove(int(dict_res[i]))

print len(lst)

with open('list-996164.txt', 'w') as f:
    f.write(str(lst))

