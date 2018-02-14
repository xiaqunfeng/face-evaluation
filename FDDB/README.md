## FDDB evaluation 评测方法

完整评测方法参看 README.txt ，这里记录自己的使用过程。

### 生成ROC曲线

> 在文件夹 evaluation 下操作

#### 1、编译

使用opencv的话，修改 common.hpp，将.ppm注释掉

```
#GE_FORMAT ".ppm"
#define CVLOADIMAGE_WORKING
```

进入 evaluation 目录，执行make

```
make
```

生成一个可执行文件 evaluate 和 runEvaluate.pl 脚本

#### 2、修改 runEvaluate.pl

- $GNUPLOT gnuplot路径
- $evaluateBin 编译生成的evaluate可执行文件
- $imDir FDDB数据库图片文件目录（注意最后要加一个斜杠"/"）
- $fddbDir FDDB folds目录
- $detDir 人脸检测输出10个txt的目录
- $detFormat 人脸框的形式，如果是矩形则是0，椭圆是1，默认是0

gnuplot路径的获取

```
▶ where gnuplot
/Users/xiaqunfeng/anaconda2/envs/python27/bin/gnuplot
```

imDir 最后要跟一个斜杠，不会自动加

detDir 里10个txt文件的命名格式是

```
fold-01-out.txt
```

如果你的结果不是这样命名的，注意去修改配置文件，改成自己的格式

```
my $foldFile = sprintf("%s/fold-%02d-out.txt", $detDir, $fi);
```

**范例**

```
#### VARIABLES TO EDIT ####
# where gnuplot is
my $GNUPLOT = "/Users/xiaqunfeng/anaconda2/envs/python27/bin/gnuplot";
#my $GNUPLOT = "/sw/bin/gnuplot";
# where the binary is
my $evaluateBin = "/Users/xiaqunfeng/ATLAB/face/FDDB/evaluation/evaluate";
# where the images are
my $imDir = "/Users/xiaqunfeng/ATLAB/face/FDDB/originalPics/";
#my $imDir = "facesInTheWild/";
# where the folds are
my $fddbDir = "/Users/xiaqunfeng/ATLAB/face/FDDB/FDDB-folds";
# where the detections are
my $detDir = "/Users/xiaqunfeng/ATLAB/face/FDDB/result/FDDB_output_mtcnn";
###########################

my $detFormat = 0; # 0: rectangle, 1: ellipse 2: pixels
```

#### 3、生成ROC曲线

```
perl runEvaluate.pl
```

就可以在 $detDir 下生成连续和离散的ROC曲线图（ContROC.png，ContROC.txt，DiscROC.png，DiscROC.txt）

### 生成 compare_ROC曲线

> 在文件夹 compareROC 下操作

- 将上一步生成的 ContROC.txt 和 DiscROC.txt 拷贝到 rocCurves 目录下
- 对应添加和修改 contROC.p 和 discROC.p 里  ContROC.txt、DiscROC.txt 的路径和title
- 运行 contROC.p 和 discROC.p， 分别得到 contROC-compare.png 和discROC-compare.png 两个 compare_ROC 曲线图

运行命令：

```
gnuplot contROC.p
```



参考资料：http://kingback1.github.io/2015/10/24/how-to-draw-ROC-by-FDDB-perl/