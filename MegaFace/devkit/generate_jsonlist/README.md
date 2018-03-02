### groundtruth

id_card_file.txt

```
1214898841.jpg 0
42048479478.jpg 1
42030361429.jpg 2
42030335718.jpg 3
xj20160813_73656.jpg 4
1207135420.jpg 5
...
```

Scene_file.txt

```
30000905.jpg 0
331082198802048099.jpg 1
360122197912010656.jpg 2
43070319890110045X.jpg 3
330326198407256757.jpg 4
513826199004253410.jpg 5
...
```

### probe-jsonlist.py

功能：产生probe图片的jsonlist

```
usage: probe-jsonlist.py [-h] -p PATH

optional arguments:
  -p PATH, --path PATH  path of groundtruth txt file
```

生成结果：

```
idProbe_features_list.json
```

### distractor-jsonlist.py

功能：产生distractor jsonlist

```
usage: distractor-jsonlist.py [-h] -p PATH -n NUM

optional arguments:
  -p PATH, --path PATH  path of groudtruth txt file
  -n NUM, --num NUM     num of distractor image
```

NUM 分别为 10，100，1000，10000，100000，1000000

生成结果:

```
idDistractor_features_list.json_1000000_1(实际为idDistractor_features_list.json_996164_1)
idDistractor_features_list.json_100000_1
idDistractor_features_list.json_10000_1
idDistractor_features_list.json_1000_1
idDistractor_features_list.json_100_1  
idDistractor_features_list.json_10_1
```