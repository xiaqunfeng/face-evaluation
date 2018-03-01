## Megaface百万人脸评测

### jsonlist的生成

1、进入评测工具 devkit

2、参考devkit/templatelists目录下的list文件生成我们内部测试需要用的 jsonlist

**probe**

- Megaface的jsonlist

示例如下：

```
facescrub_features_list.json           
facescrub_uncropped_features_list.json
fgnet_feature_list.json
```

probe set，评测时会从该集合中挑取特征，与干扰集进行比对，文件内容格式包括path和id两个字段，path为原图的相对路径，id为图片对应的真实人名或者真实id

摘取facescrub_features_list.json部分内容如下：

```
{
"path": [
"Michael_Landes/Michael_Landes_43667.png",
"Michael_Landes/Michael_Landes_43618.png,
"Martin_Henderson/Martin_Henderson_40591.png",
"Martin_Henderson/Martin_Henderson_40467.png",
...
], 
"id": [
"Michael_Landes", 
"Michael_Landes",
"Martin_Henderson", 
"Martin_Henderson"
,
...
]
}
```

- 我们需要生成的jsonlist

该jsonlist需要包括scene图片（3836个）和他们分别一一对应的idcard图片（3836个），总计7672个图片，path字段为7672个图片的相对路径，id字段为他们一一对应的真实id。

生成的json文件：idProbe_features_list.json

**干扰集**

- Megaface的jsonlist

示例如下：

```
megaface_features_list.json_1000000_1 
megaface_features_list.json_100000_1
megaface_features_list.json_10000_1
megaface_features_list.json_1000_1
megaface_features_list.json_100_1
megaface_features_list.json_10_1
```

含有不同数量的干扰集的list，文件内容格式包括path一个字段，path为原图的相对路径摘取megaface_features_list.json_10_1内容如下:

```
{
"path": [
"534/53415754@N00/37731000_1.jpg",
"389/38989502@N07/4767491946_13.jpg",
"388/38811680@N06/3837159123_2.jpg", 
"485/48588937@N00/12693002755_3.jpg", 
...
]
}
```

- 我们需要生成的jsonlist

从我们的100w身份证集合去掉上面提到的3836个，还剩下996164个，这部分当做干扰集。从996164个干扰集中分别随机挑选10,100,1000,10000,100000和全部集合（`idDistractor_features_list.json_1000000_1`），生成6个list文件。每个list文件只有一个path字段。

生成的json文件：

```
idDistractor_features_list.json_10_1
idDistractor_features_list.json_100_1
idDistractor_features_list.json_1000_1
idDistractor_features_list.json_10000_1
idDistractor_features_list.json_100000_1
idDistractor_features_list.json_1000000_1(实际应该是idDistractor_features_list.json_996164_1)
```

3、将上一步生成的 `idProbe_features_list.json` 和6个干扰集文件（`idDistractor_features_list.json_*`）放到 `devkit/templatelists` 目录下

### 评测

1、进入目录 `devkit/experiments`

2、修改 `run_idcard_exp.sh` 中的特征路径和特征文件后缀

```
▶ cat run_idcard_exp.sh
nohup python run_idcard_experiment.py \
    {path/to/distracotr/features} \
    {path/to/probe/features} \
    {features file ending} \
    ../eval-results-idcard1M/{algo_sub_dir} \
    > nohup-idcard-exp.txt &
#   -s 1000000 > nohup-idcard-exp.txt &
```

- -s 可以指定只跑某一个干扰集文件

3、运行脚本

```
sh run_idcard_exp.sh
```

4、执行之后会在 `devkit/eval-results-idcard1M/` 目录生成评测结果

```
▶ ls eval-results-idcard1M
cmc_idProbe_idDistractor_feat_1000000_1.json
cmc_idProbe_idDistractor_feat_100000_1.json
cmc_idProbe_idDistractor_feat_10000_1.json
cmc_idProbe_idDistractor_feat_1000_1.json
cmc_idProbe_idDistractor_feat_100_1.json
cmc_idProbe_idDistractor_feat_10_1.json
matches_idProbe_idDistractor_feat_1000000_1.json
matches_idProbe_idDistractor_feat_100000_1.json
matches_idProbe_idDistractor_feat_10000_1.json
matches_idProbe_idDistractor_feat_1000_1.json
matches_idProbe_idDistractor_feat_100_1.json
matches_idProbe_idDistractor_feat_10_1.json
otherFiles
```

- 以cmc开头的json文件里面包括了ROC曲线和描述top-N的CMC曲线
- 以matches开头的文件为每个probe的匹配结果
- otherFiles为中间文件，可以删除

> 更多评测方法详阅 devkit/readme.txt

### 绘图ROC和CMC曲线

1、进入` plot_results` 文件夹

2、修改文件 `plot_idcard_results.py`

```
   my_method_dirs = [
 		r'../eval-results-idcard1M/sphereface-1220',
 		r'../eval-results-idcard1M/insightface',
    ]

   my_method_labels = [
        'sphereface-1220',
        'insightface',
    ]
```

- my_method_dirs: cmc*.json在本地的文件夹路径
- my_method_labels: 标记测试的算法的名字

3、运行脚本

```
python plot_idcard_results.py
```

结果存放目录在 plot_idcard_results.py 中的 `save_dir` 指定。

4、结果解释

运行了单个算法 sphereface-1220 的结果如下：

```
TPRs-at-FPR_1e-06_sphereface-1220.txt
TPRs-at-FPR_1e-06_summary_all.txt
cmc_under_diff_distractors_sphereface-1220.png
identification_rank_1_vs_distractors.png
identification_recall_vs_rank_100k.png
identification_recall_vs_rank_10k.png
identification_recall_vs_rank_1M.png
rank_vs_distractors_sphereface-1220.txt
rank_vs_distractors_summary_all.txt
roc_under_diff_distractors_sphereface-1220.png
verification_roc_100k.png
verification_roc_10k.png
verification_roc_1M.png
```

- cmc_*: 每个算法模型 cmc 曲线图
- roc_*: 每个算法模型 roc 曲线图
- rank_*: 每个算法在不同大小干扰集下的 top-1 和 top-10 结果
- `rank_*_summer_all.txt`: 所有算法模型在不同大小干扰集下的 top-1 和 top-10 结果
- identification*: 所有算法模型在不同大小干扰集下 top-N 结果曲线图
- verfication*: 所有模型在不同大小干扰集下的 ROC 曲线图
- TPR*: 计算了FPR 1e-6 的TPR
- roc开头的图片和TPR开头的txt是相互对应的