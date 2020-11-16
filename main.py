import PIL
from PIL import ImageDraw, ImageFont
from PIL.Image import Image

if __name__ == '__main__':
    # 参数
    image_path: str = 'image.png'  # 需要添加图片的位置
    txt: str = "水印"  # 水印文字
    angle: int = 45  # 倾斜角度, default
    font_size: int = 30  # 文字大小, default
    txt_internal_x: int = 10  # 文字间隔, default
    txt_internal_y: int = 5  # 文字间隔, default
    alpha: int = 20  # 水印透明度设置, default

    # 处理
    image: Image = PIL.Image.open(image_path)  # 原始图片
    new_x = image.width * 3
    new_y = image.height * 3
    # 构造原始图像的9个, 作为处理的图像, 因为会对水印进行45°倾斜, 为了覆盖整个图片, 所以将原始图片复制为9个
    new: Image = PIL.Image.new("RGBA", (new_x, new_y))
    for i in range(0, new_x, image.width):
        for j in range(0, new_y, image.height):
            new.paste(image, (i, j))

    font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", font_size)  # 使用微软雅黑

    # 生成同等大小的图片, 透明100%
    watermark = PIL.Image.new("RGBA", new.size, (255, 255, 255, 0))
    watermark_draw = PIL.ImageDraw.Draw(watermark)

    # 获取文本大小
    txt_x, txt_y = watermark_draw.textsize(txt, font = font)

    # 添加文本, 透明20
    for i in range(0, new_x, txt_x + txt_internal_x):
        for j in range(0, new_y, txt_y + txt_internal_y):
            watermark_draw.text((i, j), text = txt, font = font, fill = (255, 255, 255, alpha))

    # 旋转45°
    watermark = watermark.rotate(angle, PIL.Image.BICUBIC)
    # alpha = watermark.split()[3] # 对透明度处理
    # 此方法为将RGBA分别获取出来作为一个Image, 模式即为L
    # alpha = PIL.ImageEnhance.Brightness(alpha).enhance(0.7)
    # watermark.putalpha(alpha)

    # 将水印加到图片上
    after: Image = PIL.Image.alpha_composite(new, watermark)

    # 剪切中间的图片. 要剪切部分的左上角, 和右下角的坐标, 以图片左上角为原点
    after = after.crop((image.width, image.height, new_x - image.width, new_y - image.height))
    after.save("after.png")
