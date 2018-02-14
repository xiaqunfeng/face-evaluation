# Compare your discrete ROC curves with other methods
# At terminal: gnuplot discROC.p
set terminal png size 1280, 960 enhanced font 'Verdana,18'
set size 1,1
set xtics 500
set ytics 0.1
set grid
set ylabel "True positive rate"
set xlabel "False positive"
set xr [0:2000]
set yr [0:1.0]
set key below
set output "discROC-compare.png"
plot  "rocCurves/DDFD_DiscROC.txt" using 2:1 title 'DDFD' with lines lw 2 , \
"rocCurves/CasCNN-DiscROC.txt" using 2:1 title 'CascadeCNN' with lines lw 2 , \
"rocCurves/jjyan_allROC_DiscROC.txt" using 2:1 title 'Yan et al.' with lines lw 2 , \
"rocCurves/AcfDiscROC.txt" using 2:1 title 'ACF-multiscale' with lines lw 2 , \
"rocCurves/pico-DiscROC.txt" using 2:1 title 'Pico' with lines lw 2 , \
"rocCurves/HeadHunter_DiscROC.txt" using 2:1 title 'HeadHunter' with lines lw 2 , \
"rocCurves/JointCascade_DiscROC.txt" using 2:1 title 'Joint Cascade' with lines lw 2 , \
"rocCurves/BoostedExamplerBased-DiscROC.txt" using 2:1 title 'Boosted Exemplar' with lines lw 2 , \
"rocCurves/SURF_GentleBoost_FTDiscROC.txt" using 2:1 title 'SURF-frontal' with lines lw 2 , \
 "rocCurves/SURF_GentleBoost_MVDiscROC.txt" using 2:1 title 'SURF-multiview' with lines lw 2 , \
 "rocCurves/PEPAdapt_DiscROC.txt" using 2:1 title 'PEP-Adapt' with lines lw 2 , \
 "rocCurves/XZJY_DiscROC.txt" using 2:1 title 'XZJY' with lines lw 2 , \
 "rocCurves/dr40DiscROC.txt" using 2:1 title 'Zhu et al.' with lines lw 2 , \
 "rocCurves/santiDiscROC.txt" using 2:1 title 'Segui et al.' with lines lw 2, \
 "rocCurves/koestingerDiscROC.txt" using 2:1 title 'Koestinger et al.' with lines lw 2, \
 "rocCurves/LiIntelDiscROC.txt" using 2:1 title 'Li et al.' with lines lw 2, \
 "rocCurves/jainDiscROC.txt" using 2:1 title 'Jain et al.' with lines lw 2, \
 "rocCurves/subburamanDiscROC.txt" using 2:1 title 'Subburaman et al.' with lines lw 2, \
 "rocCurves/ViolaJonesScore_n0_DiscROC.txt" using 2:1 title 'Viola-Jones' with lines lw 2, \
 "rocCurves/MikolajczykDiscROC.txt" using 2:1 title 'Mikolajczyk et al.' with lines lw 2, \
 "rocCurves/kienzleDiscROC.txt" using 2:1 title 'Kienzle et al.' with lines lw 2


 
