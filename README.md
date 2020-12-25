Add Watermark
=

    Write for id card
    Python(3.8)

#### Usage

    watermark -f origin.png -t WatermarkText

#### Help

```shell
usage: cmd.exe [-h] [--version] --file FILE --text TEXT [--angle ANGLE] [--font-size FONT_SIZE] [--font-x FONT_X] [--font-y FONT_Y] [--alpha ALPHA]

Add watermark to image

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program version
  --file FILE, -f FILE  the image file you want to add a watermark text
  --text TEXT, -t TEXT  the watermark text
  --angle ANGLE         text tilt angle
  --font-size FONT_SIZE
                        text font size
  --font-x FONT_X       text x-axis spacing
  --font-y FONT_Y       text y-axis spacing
  --alpha ALPHA         watermark transparency
```

#### Former

![image](image.png)

#### After

![image](after.png)

#### Dependency

+ Pillow

#### Build

+ [Nuitka](https://github.com/Nuitka/Nuitka)
+ [MSVC](https://visualstudio.microsoft.com/vs/features/cplusplus/)

```shell
nuitka --msvc=14.2 cmd.py && rename cmd.exe watermark.exe
```

#### License

[Apache-2.0 License](LICENSE)

#### Tip

```python
# add different background color
image: Image = PIL.Image.open("background_less.png")
background: Image = PIL.Image.new("RGBA", image.size, (255, 0, 0))
background.paste(image, (0, 0, image.width, image.height), image)
background.save("test.png")
```