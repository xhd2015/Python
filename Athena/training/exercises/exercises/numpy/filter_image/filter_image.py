"""
Filter Image
------------

Read in the "dc_metro" image and use an averaging filter
to "smooth" the image.  Use a "5 point stencil" where
you average the current pixel with its neighboring pixels::

              0 0 0 0 0 0 0
              0 0 0 x 0 0 0
              0 0 x x x 0 0
              0 0 0 x 0 0 0 
              0 0 0 0 0 0 0

Plot the image, the smoothed image, and the difference between the
two.

x_5pa = ( x_(i,j) + x_(i+1,j) + x_(i-1,j) + x_(i,j+1) + x_(i,j-1)) / 5

Bonus
~~~~~

Re-filter the image by passing the result image through the filter again. Do
this 50 times and plot the resulting image. 

See :ref:`filter-image-solution`.
"""

from scipy.misc.pilutil import imread
from matplotlib.pyplot import figure, subplot, imshow, title, show, gray, cm

# 'flatten' creates a 2D array from a JPEG.
img = imread('dc_metro.JPG', flatten=True)

def filtering(img):
    f_img =(  img[1:-1,1:-1]  # c
              + img[ :-2,1:-1]  #t
              + img[2:  ,1:-1]  # b
              + img[1:-1, :-2]  # l
              + img[1:-1,2:  ]  # r
             ) / 5.0
    return f_img

av_img = filtering(img)

figure()

gray()
# image
subplot(1,4,1)
imshow(img)
title('original image')

# the smoothed image
subplot(1,4,2)
imshow(av_img)
title('smoothed image')

# the difference between the two
subplot(1,4,3)
imshow(img[1:-1,1:-1] - av_img)
title('difference b/n images')

re_img = img
for num in range(50):
    re_img = filtering(re_img)

# the fifty times refiltered image
subplot(1,4,4)
imshow(re_img)
title('Re-filtered 50 times image')

show()





show()