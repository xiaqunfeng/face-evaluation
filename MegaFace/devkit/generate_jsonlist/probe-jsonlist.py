import os
import re
import json
import codecs
#import argparse
#
#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--path", required=True, help="path of image")
#args = vars(ap.parse_args())

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
#print(dict_res)

dic = {}
lst_path = []
#path = args["path"]
path_scene = 'scene/'
path_idcard = 'id_card/'
for img_num in range(scene_num):
    name = path_scene + str(img_num) + '.jpg'
    lst_path.append(name)
for img_num in range(scene_num):
    corr_num = dict_res[img_num]
    name = path_idcard + corr_num + '.jpg'
    lst_path.append(name)
dic["path"] = lst_path
        
lst_id = []
for i in range(scene_num):
    lst_id.append(dict_scene[str(i)])
for i in range(scene_num):
    lst_id.append(dict_scene[str(i)])
dic["id"] = lst_id

#probe_jsonlist = json.dumps(dic)
with codecs.open('idProbe_features_list.json', 'w') as f:
    json.dump(dic, f)

