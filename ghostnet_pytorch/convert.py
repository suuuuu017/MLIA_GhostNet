import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

itk_image = sitk.ReadImage('Classification_data/train/Diseased/OAS30004_MR_d1101.mhd')
image_array = sitk.GetArrayViewFromImage(itk_image)

# print the image's dimensions
print(image_array.shape)

# plot the image
plt.imshow(image_array, cmap='gray')
plt.show()