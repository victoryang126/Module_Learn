
import os
# PIL : Python Imaging Library
from PIL import Image

a = "/Users/monster/PycharmProjects/GitHub/MiniTool/Images/title.PNG"

b = "/Users/monster/PycharmProjects/GitHub/MiniTool/Images"
# 获取目录下文件名
files = ["/Users/monster/PycharmProjects/GitHub/MiniTool/Images/title.PNG"]
# 图标大小
size = (256,256)

# 给图标文件单独创建一个icon目录
if not os.path.exists('icon'):
    os.mkdir('icon')

for inName in files:
    # 分离文件名与扩展名
    tmp = os.path.splitext(inName)
    print(inName,tmp)
    # 因为python文件跟图片在同目录，所以需要判断一下
    if tmp[1] == '.PNG':
        outName = tmp[0] + '.ico'
        # 打开图片并设置大小
        im = Image.open(inName).resize(size)
        try:
            # 图标文件保存至icon目录
            path = os.path.join('icon', outName)
            im.save(path)
            print(1)
            print('{} --> {}'.format(inName, outName))
        except IOError:
            print('connot convert :',inName)