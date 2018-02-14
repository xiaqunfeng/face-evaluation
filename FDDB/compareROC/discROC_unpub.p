set terminal png size 1280, 960 enhanced font 'Verdana,18'
set key font ",12"
set size 1,1
set xtics 500
set ytics 0.1
set grid
set ylabel "True positive rate"
set xlabel "False positive"
set xr [0:2000]
set yr [0:1.0]
set key right bottom
set output "discROC_unpub.png"
plot  "rocCurves/BAIDU-IDL-disc.txt" using 2:1 title 'Baidu-IDL' with lines lw 2 , \
 "rocCurves/Linkface-DiscROC_v1.txt" using 2:1 title 'Linkface' with lines lw 2 , \
 "rocCurves/Uni-Ubi_DiscROC-2.txt" using 2:1 title 'Uni-Ubi-2' with lines lw 2 , \
 "rocCurves/LandmarkbasedDiscROC.txt" using 2:1 title 'IMC Lab' with lines lw 2 , \
 "rocCurves/Uni-Ubi_DiscROC.txt" using 2:1 title 'Uni-Ubi' with lines lw 2 , \
 "rocCurves/Eyedea_DiscROC.txt" using 2:1 title 'EyedeaRecognition' with lines lw 2 , \
 "rocCurves/StradVision-DiscROC.txt" using 2:1 title 'StradVision' with lines lw 2 , \
 "rocCurves/tencent_DiscROC.txt" using 2:1 title 'Tencent-BestImage' with lines lw 2 , \
 "rocCurves/Shenzhen2014-DiscROC.txt" using 2:1 title 'Shenzhen2014' with lines lw 2 , \
 "rocCurves/tvplay.cn-DiscROC.txt" using 2:1 title 'TVplay' with lines lw 2 , \
 "rocCurves/HisignDiscROC.txt" using 2:1 title 'Hisign' with lines lw 2 , \
 "rocCurves/Face++DiscROC.txt" using 2:1 title 'Face++' with lines lw 2 , \
 "rocCurves/shenzenDiscROC.txt" using 2:1 title 'Shenzhen Uni' with lines lw 2 , \
 "rocCurves/OlaworksDiscROC.txt" using 2:1 title 'Olaworks' with lines lw 2 , \
 "rocCurves/illuxtechFrontalFaceDiscROC.txt" using 2:1 title 'Illuxtech Inc.' with lines lw 2


 
