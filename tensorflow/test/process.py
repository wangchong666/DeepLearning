from PIL import Image
import os
import os.path

sourceDir ="12306";
imagesPath = os.path.join("train","images")
labelsPath = os.path.join("train","labels")
lst = os.listdir(sourceDir) 
for l in lst:
    try:
        img = Image.open(os.path.join(sourceDir,l))
        img1 = img.crop((118,0,178,23))
        
        im2 = img1.convert('RGBA')
        rot = im2.rotate(10, expand=1)
        fff = Image.new('RGBA', rot.size, (255,)*4)
        out = Image.composite(rot, fff, rot)
        out.convert(img.mode).save(os.path.join(labelsPath,l))
        # img1.save(os.path.join(labelsPath,l))
        # for i in range(4):
        #     for j in range(2):
        #         left = 5+72*i;
        #         top = 41+72*j;
        #         box = (left, top, left+67, top+67);
        #         img1 = img.crop(box)
        #         img1.save(os.path.join(imagesPath,l)+"_{}_{}.jpg".format(j,i))
    except Exception as err: 
        print("process file {} failed!".format(l))
        print(err);

# name = "12306\\1501667615.8588958.jpg"
# img = Image.open(name)
# # 从左上角开始 剪切 200*200的图片
# # img2 = img.crop((5,41,72,108))
# # img2.save("lena2.jpg")

# for i in range(4):
#     for j in range(2):
#         left = 5+72*i;
#         top = 41+72*j;
#         box = (left, top, left+67, top+67);
#         print(box);
#         img1 = img.crop(box)
#         img1.save(name+"_{}_{}.jpg".format(j,i))
