from scipy import ndimage, misc
import numpy as np
import matplotlib.pyplot as plt
import timeit


def to_grayscale(img, weights = np.c_[0.2989, 0.5870, 0.1140]):
  tile = np.tile(weights, reps=(img.shape[0], img.shape[1], 1))
  return np.sum(tile*img, axis=2)

def simple_threshold(img, threshold):
  return ((img > threshold) * 255).astype("uint8")

# time it
start = timeit.timeit()


img = misc.imread('image1.jpg')
#result = ndimage.sobel(img)
#result = ndimage.gaussian_filter()
#result = ndimage.median_filter(img, 2)

# Segmentation
#mask = (img > img.mean()).astype(np.float)
#mask += 0.1 * img
img_grey = to_grayscale(img)
img_bin = simple_threshold(img_grey, 30)
#img_bin_open = ndimage.binary_opening(img_bin, iterations=3)
#img_bin_close = ndimage.binary_closing(img_bin_open, iterations=3)
img_bin_dil = ndimage.binary_dilation(img_bin, iterations=3)
img_bin_ero = ndimage.binary_erosion(img_bin_dil)
result = img_bin_ero

end = timeit.timeit()
print(end - start)

plt.imshow(result, cmap='binary')
plt.show()