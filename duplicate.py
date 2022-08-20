import os
from PIL import Image, ImageStat
l = ['jpg','jpeg','jfif','webp','png']
image_files= []
image_folder=r'C:\Users\P.Dhanashreenydhi\Downloads\duplicate files'
#print(image_folder)
for i in l:
    for j in os.listdir(image_folder):
        if j.endswith(i):
            image_files.append(j)
print(image_files)

duplicate_files=[]


for file_org in image_files:
    if file_org not in duplicate_files:
        image_org = Image.open(os.path.join(image_folder, file_org))
        pix_mean1 = ImageStat.Stat(image_org).mean
        #print(pix_mean1)
        for file_check in image_files:
            if file_check != file_org:
                image_check = Image.open(os.path.join(image_folder, file_check))
                pix_mean2 = ImageStat.Stat(image_check).mean
                if pix_mean1 == pix_mean2:
                    duplicate_files.append(file_org)
                    duplicate_files.append(file_check)

print(duplicate_files)