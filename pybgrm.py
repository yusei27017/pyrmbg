from rembg import remove
import os
from PIL import Image
from io import BytesIO

directory_path = './input'
output_path = './output'

if not os.path.exists(output_path):  # 如果輸出目錄不存在，創建它
    os.makedirs(output_path)

def Reformat_Image(ImageFilePath, img_name):
    image = Image.open(ImageFilePath, 'r')
    opened_img = remove(image)
    image = Image.new("RGB", opened_img.size, (255, 255, 255))
    image.paste(opened_img, (0, 0), opened_img)  # 這裡的mask就是img_no_bg自己，因為它自己就是一個透明度的遮罩
    image_size = image.size
    width = image_size[0]
    height = image_size[1]
    bigside = width if width > height else height

    background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
    offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2), 0)))

    background.paste(image, offset)
    background.save(os.path.join(output_path, img_name))
    print(img_name + " has been reformatted!")

if __name__ == "__main__":
    
    # 遍歷目錄並找到所有.png檔案的相對路徑
    png_files_relative_paths = [os.path.join(directory_path, f)
                                for f in os.listdir(directory_path) if f.endswith('.png')]
    for path in png_files_relative_paths:

        Reformat_Image(path, os.path.basename(path))
