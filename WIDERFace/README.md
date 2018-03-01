## WIDERFace evaluation 评测方法

### 目录文件

```
WIDERFace/eval_tools
▶ ls
boxoverlap.m ground_truth norm_score.m pred         wider_eval.m
evaluation.m nms.m        plot         read_pred.m
```

### 结果存放的格式

每张图片对应生成一个以图片名称命名的 txt 文件，结果存放的目录结构和图片存放的结构一致。

txt 内容如 Submission_example 中所示：

```
▶ cat Submission_example/0--Parade/0_Parade_marchingband_1_20.txt
0_Parade_marchingband_1_20
1
541 354 36 46 1.000
```

- 第一行：图片名（不带后缀）
- 第二行：检测出的人脸个数
- 后续行：行数 = 人脸个数，根据 score 从高到低依次排列

五个参数依次为：人脸框的左上角坐标（x,y），框的宽和高（w,h），score

### 生成图表方法

打开matlab，程序入口 **wider_eval.m**

1、在eval_tools目录下新建pred目录，然后将结果拷贝到pred目录下（或者修改代码，指定结果存放的目录）

```
%Please specify your prediction directory.
pred_dir = './pred';
```

2、修改模型的名称

```
%Please specify your algorithm name.
legend_name = 'Res18-Refinedet-20180207';
```

3、在matlab中直接运行即可。

此时在目录 `plot/baselines/Val/setting_int` 下生成命名的文件夹和 .mat 文件

```
face/WIDERFace/eval_tools
▶ ls plot/baselines/Val/setting_int
Qiniu-SSD-Mobilenet      Res18-Refinedet-20180207
▶ ls plot/baselines/Val/setting_int/Res18-Refinedet-20180207
wider_pr_info_Res18-Refinedet-20180207_easy_val.mat
wider_pr_info_Res18-Refinedet-20180207_hard_val.mat
wider_pr_info_Res18-Refinedet-20180207_medium_val.mat
```

4、将需要绘在同一张图上 .mat 文件拷贝到目录 `plot/baselines/Val/setting_int` 下即可。

5、生成的图片存放在目录 `eval_tools/plot/figure/Val` 下。

注意，生成 .mat 的命名是严格按照 `wider_pr_info_文件夹名_easy_val.mat` 来命名的。生成曲线的名称也是该名称。如果想改变生成曲线的名称，可以在matlab 中加载 .mat 文件，然后修改其 lend_name ，保存即可。