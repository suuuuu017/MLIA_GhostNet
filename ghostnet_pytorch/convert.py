import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

# for file in os.listdir("/mydir"):
#     if file.endswith(".txt"):
#         print(os.path.join("/mydir", file))

#rootdir = '/Users/suuuuu017/PycharmProjects/Efficient-AI-Backbones-master/ghostnet_pytorch/Classification_data'
rootdir = '/home/bt3qzd/MLIA_GhostNet/ghostnet_pytorch/Classification_data'

#datadir = '/Users/suuuuu017/PycharmProjects/Efficient-AI-Backbones-master/ghostnet_pytorch/data'
datadir = '/home/bt3qzd/MLIA_GhostNet/ghostnet_pytorch/data/'
subdirarr = ['train/', 'val/']
subsubdir = ['Diseased/', 'Healthy/']

subI = 0
subsubI = 0

i = 0
j = 0
k = 0

for subdir, dirs, files in os.walk(rootdir):
    if dirs:
        continue
    if str(files[0]) == '.DS_Store':
        continue
    print(subdir, " ", dirs, " ", files)
    input()
    for file in files:
        if file.endswith(".mhd"):
            # print(os.path.join(subdir, file))
            itk_image = sitk.ReadImage(os.path.join(subdir, file))
            image_array = np.array(sitk.GetArrayFromImage(itk_image))
            path = datadir+subdirarr[i]+''+subsubdir[j]+'file'+str(k)+'.jpeg'
            print(image_array.shape)
            if len(image_array.shape) > 2:
                image_array = image_array[0, :]
            im = Image.fromarray(image_array*255)
            im = im.convert("L")
            im.save(path)
            k += 1
            # if not (os.path.exists(path)):
            #     np.save(path, image_array)
    subI = (subI + 1) % 2
    subsubI = (subsubI + 1) % 2
    if j == 1:
        i+=1
    if j == 0:
        j+=1
    else:
        j=0
    



# print the image's dimensions
print(image_array.shape)

# plot the image
plt.imshow(image_array, cmap='gray')
plt.show()