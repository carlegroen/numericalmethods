#4: Bi-linear Interpolation on a Rectilinear Grid in Two Dimensions

Bi-linear interpolation is done by constructing a function that passes through given points. The n<sub>x</sub> * n<sub>y</sub> vectors are tabulated in the function F<sub>i,j</sub>, which denotes all points within the matrix.

A rectilinear grid is a set of rectangles that aren't all congruent to eachother. The cells can still be indexed in vectors, however, the spacing between points are not regular. Logarithmic scales are examples of non-cartesian grids, and it is often used as an example of rectilinear grids.

##Part A

For exercise A, a four-point system with one F-value given at a corner is plotted.

The non-interpolated picture for part A is given as the contourplot below:

![alt tag](https://github.com/carlegroen/numericalmethods/raw/master/exam/noninterpolated.png)

With the bi-linear interpolation algorithm constructed applied:

![alt tag](https://github.com/carlegroen/numericalmethods/raw/master/exam/interpolated.png)

##Part B

For a rectilinear grid with a given F matrix as a function, the non-interpolated grid is seen below:

![alt tag](https://github.com/carlegroen/numericalmethods/raw/master/exam/noninterpolatedPartB.png)

And with the interpolation algorithm applied:
![alt tag](https://github.com/carlegroen/numericalmethods/raw/master/exam/interpolatedPartB.png)
