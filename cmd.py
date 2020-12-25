import argparse
import traceback

import PIL

from main import gen

__version__ = "Program v0.0.1 Pillow version %s" % PIL.__version__

parser = argparse.ArgumentParser(description = "Add watermark to image", )
parser.add_argument('--version', '-v', help = 'show program version', action = 'version', version = __version__)
parser.add_argument('--file', '-f', help = 'the image file you want to add a watermark text',
                    default = 'origin.png', required = True, type = str)
parser.add_argument('--text', '-t', help = 'the watermark text', default = 'WATERMARK', required = True, type = str)
parser.add_argument('--angle', help = 'text tilt angle', default = 45, type = int)
parser.add_argument('--font-size', help = 'text font size', default = 45, type = int)
parser.add_argument('--font-x', help = 'text x-axis spacing', default = 10, type = int)
parser.add_argument('--font-y', help = 'text y-axis spacing', default = 5, type = int)
parser.add_argument('--alpha', help = 'watermark transparency', default = 20, type = int)
args = parser.parse_args()

if __name__ == "__main__":
    try:
        gen(args.file, args.text, args.angle, args.font_size, args.font_x, args.font_y, args.alpha)
    except Exception as e:
        traceback.print_exc()
