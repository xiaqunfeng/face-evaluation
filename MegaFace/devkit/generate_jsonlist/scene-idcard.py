import re
#import argparse
#
#ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--scene", required=True,
#        help="path to input scene.txt")
#ap.add_argument("-i", "--idcard", required=True,
#        help="path to input id_card.txt")
#args = vars(ap.parse_args())

scene_num = 0
dict_scene = {}
scene = "../../xqf/face_code_book/scene_file.txt"
idcard = "../../xqf/face_code_book/id_card_file.txt"
#with open(args["scene"], 'rt') as f:
with open(scene, 'rt') as f:
    for line in f:
        img_name = line.split(' ')[0]
        img_index = re.split(r'[\s]', line)[1]
        #img_index = line.split(' ')[1] # with '/n' in the end
        dict_scene[img_index] = img_name
        scene_num += 1
    #print(dict_scene)

dict_idcard = {}
#with open(args["idcard"], 'rt') as f:
with open(idcard, 'rt') as f:
    for line in f:
        img_name = line.split(' ')[0]
        img_index = re.split(r'[\s]', line)[1]
        dict_idcard[img_name] = img_index
    #print(dict_idcard)

dict_res = {} # scene_index : idcard_index
for i in range(scene_num):
    #print(dict_scene[str(i)])
    dict_res[i] = dict_idcard[dict_scene[str(i)]]
print(dict_res)
