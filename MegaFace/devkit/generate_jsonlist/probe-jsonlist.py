import os
import re
import json
import codecs
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path of groudtruth txt file")
args = vars(ap.parse_args())

# get relationship of scene and idcard
path_gt = args["path"]
scene = path_gt + "/scene_file.txt"
idcard = path_gt + "/id_card_file.txt"
lst_scene_idx = []
dict_scene = {}
with open(scene, 'rt') as f:
    for line in f:
        img_name = line.split(' ')[0]
        img_index = re.split(r'[\s]', line)[1]
        dict_scene[img_index] = img_name
        lst_scene_idx.append(int(img_index))

dict_idcard = {}
with open(idcard, 'rt') as f:
    for line in f:
        img_name = line.split(' ')[0]
        img_index = re.split(r'[\s]', line)[1]
        dict_idcard[img_name] = img_index

dict_res = {} # scene_index : idcard_index
for i in lst_scene_idx:
    dict_res[i] = dict_idcard[dict_scene[str(i)]]

# add path field to dic
dic = {}
lst_path = []
path_scene = 'scene/'       # subdir of 3836 scene pic
path_idcard = 'id_card/'    # subdir of 1M id_card pic
for img_num in lst_scene_idx:
    name = path_scene + str(img_num) + '.jpg'
    lst_path.append(name)
for img_num in lst_scene_idx:
    corr_num = dict_res[img_num]
    name = path_idcard + corr_num + '.jpg'
    lst_path.append(name)
dic["path"] = lst_path
        
# add id field to dic
dic = {}
lst_id = []
for i in lst_scene_idx:
    lst_id.append(dict_scene[str(i)])
for i in lst_scene_idx:
    lst_id.append(dict_scene[str(i)])
dic["id"] = lst_id

# write dic to json file
#probe_jsonlist = json.dumps(dic)
with codecs.open('idProbe_features_list.json', 'w') as f:
    json.dump(dic, f)

