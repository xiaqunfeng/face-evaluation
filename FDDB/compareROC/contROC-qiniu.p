# Compare your discrete ROC curves with other methods
# At terminal: gnuplot contROC.p
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
# Compare your discrete ROC curves with other methods
# At terminal: gnuplot discROC.p
set key below
set output "Qiniu-contROC-compare.png"
plot  "rocCurves/Qiniu-ssd_0.01ContROC.txt" using 2:1 title 'Qiniu ssd_0.01' with lines lw 2 , \
"rocCurves/Qiniu-refinedetContROC.txt" using 2:1 title 'Qiniu Refinedet' with lines lw 2 , \
"rocCurves/Qiniu-mtcnnContROC.txt" using 2:1 title 'Qiniu mtcnn' with lines lw 2


 
