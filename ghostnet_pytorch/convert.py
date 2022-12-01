import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import os

# for file in os.listdir("/mydir"):
#     if file.endswith(".txt"):
#         print(os.path.join("/mydir", file))

rootdir = '/Users/suuuuu017/PycharmProjects/Efficient-AI-Backbones-master/ghostnet_pytorch/Classification_data'

datadir = '/Users/suuuuu017/PycharmProjects/Efficient-AI-Backbones-master/ghostnet_pytorch/data/'
subdir = ['train/', 'val/']
subsubdir = ['Diseased/', 'Healthy/']

subI = 0
subsubI = 0

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
            image_array = np.array(sitk.GetArrayViewFromImage(itk_image))
            # sitk.WriteImage(image_array, os.path.join(datadir, subdir[subI], subsubdir[subsubI]))
            path = os.path.join(datadir, subdir[subI], subsubdir[subsubI], file[:-4])
            # path = os.path.join(datadir, subdir[subI])
            # print(path)
            # path = os.path.join(path, subsubdir[subsubI])
            # print(path)
            # path = os.path.join(path, file[:-4])
            # print(path)
            if not (os.path.exists(path)):
                # create the directory you want to save to
                # os.mkdir(path)
                np.save(path, image_array)
    subI = (subI + 1) % 2
    subsubI = (subsubI + 1) % 2



# print the image's dimensions
print(image_array.shape)

# plot the image
plt.imshow(image_array, cmap='gray')
plt.show()