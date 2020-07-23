"""
pip install paddlepaddle
pip install paddlehub
hub install deeplabv3p_xception65_humanseg==1.0.0
"""
import os
import paddlehub as hub

# 加载模型
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')  
base_dir = os.path.abspath(os.path.dirname(__file__))

# 获取当前文件目录
path = os.path.join(base_dir, '原图/')
# 获取文件列表
files = [path + i for i in os.listdir(path)]  
print(files)
# 抠图
results = humanseg.segmentation(data={'image': files})  
for result in results:
    print(result)