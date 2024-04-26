import numpy as np
import imageio as io
import tifffile as tiff


image_data = io.volread('Stack.tif')

if np.min(image_data) < 0:
    volMin = np.absolute(np.min(image_data))
else:
    volMin = 0

volMax = np.max(image_data) + volMin

image_data = image_data/volMax
image_data_conv = np.round(image_data * 65535).astype(np.uint16)

conv_name = 'Stack_conv.tif'
tiff.imwrite(conv_name, np.array(image_data_conv), bigtiff=True)