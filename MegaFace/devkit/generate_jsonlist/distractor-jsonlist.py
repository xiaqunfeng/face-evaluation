import random
import re
import json
import codecs
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path of groudtruth txt file")
ap.add_argument("-n", "--num", required=True, help="num of distractor image")
args = vars(ap.parse_args())

# create a list with member 0~999999
lst = range(1000000)

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

# remove scene in idcard
dict_res = {} # scene_index : idcard_index
for i in lst_scene_idx:
    dict_res[i] = dict_idcard[dict_scene[str(i)]]
    # remove from lst
    #del lst[int(dict_res[i])]
    lst.remove(int(dict_res[i]))

print 'len(lst) =',len(lst)

#slice = random.sample(lst, args["num"])

# add path field to dic
dic = {}
lst_path = []
path_idcard = 'id_card/'
nums = int(args["num"])
print 'nums =',nums
#for img_num in slice:
for img_num in range(nums):
    name = path_idcard + str(lst[int(img_num)]) + '.jpg'
    lst_path.append(name)
dic["path"] = lst_path

# write dic to json file
#probe_jsonlist = json.dumps(dic)
save_name = 'idDistractor_features_list.json_' + str(nums) + '_1'
with codecs.open(save_name, 'w') as f:
    json.dump(dic, f)
