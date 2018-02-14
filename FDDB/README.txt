Face Detection Data Set and Benchmark
University of Massachusetts - Amherst

Contents:
--------------------------------

1. Original set of images (from Faces in the Wild data set)
2. Face annotations
3. Detection output
   4a. Rectangular regions
   4b. Elliptical regions  
4. Additional details

1. Original set of images
--------------------------

The original set of images can be downloaded from 
http://tamaraberg.com/faceDataset/originalPics.tar.gz
Uncompressing this file organizes the images as
originalPics/year/month/day/big/*.jpg


2. Face annotations
--------------------------------

Uncompressing the "FDDB-folds.tgz" file creates a directory
"FDDB-folds", which contains files with names:
FDDB-fold-xx.txt and FDDB-fold-xx-ellipseList.txt,
where xx = {01, 02, ..., 10} represents the fold-index.

Each line in the "FDDB-fold-xx.txt" file specifies a path 
to an image in the above-mentioned data set. For instance, 
the entry "2002/07/19/big/img_130" corresponds to 
"originalPics/2002/07/19/big/img_130.jpg."

The corresponding annotations are included in the file 
"FDDB-fold-xx-ellipseList.txt" in the following 
format:

...
<image name i>
<number of faces in this image =im>
<face i1>
<face i2>
...
<face im>
...

Here, each face is denoted by:
<major_axis_radius minor_axis_radius angle center_x center_y 1>.


3. Detection output
--------------------------------

To be recognized by the evaluation code, the detection
output is expected in the following format:

...
<image name i>
<number of faces in this image =im>
<face i1>
<face i2>
...
<face im>
...

where the representation of a face depends on the specifics
of the shape of the hypothesized image region. The evaluation
code supports the following shapes:
  
  4 a. Rectangular regions
       Each face region is represented as:
       <left_x top_y width height detection_score> 
  
  4 b. Elliptical regions
       Each face region is represented as:
       <major_axis_radius minor_axis_radius angle center_x center_y detection_score>.

Also, the order of images in the output file is expected to be 
the same as the order in the file annotatedList.txt.

4. Additional details
--------------------------------

For additional details on how the database was constructed, as well as
how the configurations were chosen for performance reporting, please
refer to our technical report:

Vidit Jain and Erik Learned-Miller.
FDDB: A Benchmark for Face Detection in Unconstrained Settings. 
University of Massachusetts Amherst, Technical Report , February, 2010.
