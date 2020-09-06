import PIL
from PIL import ImageDraw, ImageFont
from PIL.Image import Image

if __name__ == '__main__':
    # 参数
    image_path: str = 'image.png'  # 需要添加图片的位置
    txt: str = "水印"  # 水印文字
    angle: int = 45  # 倾斜角度, default
    font_size: int = 50  # 文字大小, default
    txt_internal: int = 10  # 文字间隔, default
    alpha: int = 50  # 水印透明度设置, default

    # 处理
    image: Image = PIL.Image.open(image_path)  # 原始图片
    new_x = image.size[0] * 3
    new_y = image.size[1] * 3
    # 构造原始图像的9个, 作为处理的图像, 因为会对水印进行45°倾斜, 为了覆盖整个图片, 所以将原始图片复制为9个
    new: Image = PIL.Image.new("RGBA", (new_x, new_y))
    for i in range(0, new_x, image.size[0]):
        for j in range(0, new_y, image.size[1]):
            new.paste(image, (i, j))

    font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", font_size)  # 使用微软雅黑

    # 生成同等大小的图片, 透明100%
    watermark = PIL.Image.new("RGBA", new.size, (255, 255, 255, 0))
    # txt_overlay = txt_overlay.ro(PIL.Image.ROTATE_90)
    watermark_draw = PIL.ImageDraw.Draw(watermark)

    # 获取文本大小
    txt_x, txt_y = watermark_draw.textsize(txt, font = font)

    # 添加文本, 最大距离要够大(1_0000), 才能够覆盖整个图片, 透明50%
    for i in range(0, 1_0000, txt_x + txt_internal):
        for j in range(0, 1_0000, txt_y + txt_internal):
            watermark_draw.text((i, j), text = txt, font = font, fill = (255, 255, 255, alpha))

    # 旋转45°
    watermark = watermark.rotate(angle, PIL.Image.BICUBIC)
    # alpha = watermark.split()[3] # 对透明度处理
    # alpha = PIL.ImageEnhance.Brightness(alpha).enhance(0.7)
    # watermark.putalpha(alpha)

    # 将水印加到图片上
    after: Image = PIL.Image.composite(watermark, new, watermark)

    # 剪切中间的图片
    after = after.crop((new_x / 3, new_y / 3, new_x - new_x / 3, new_y - new_y / 3))  # 要剪切部分的左上角, 和右下角的坐标
    after.save("after.png")
