from PIL import Image
import pyheif
import os,argparse

# convert image file
def convert_img(img, dst):
    if img.lower().endswith('.heic'):
        basename = os.path.basename(img)
        try:
            heif_file = pyheif.read(img)
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
                )
            save_name = os.path.join(dst,basename) + ".jpeg"
            if not os.path.exists(dst):
                os.mkdir(dst)
            image.save(save_name, "JPEG")
            print("Input file is %s, output destination is %s" % (img, save_name))
        except ValueError:
            print("%s Not a heic file." % img)
    else:
        print("%s Not a heic file." % img)

# loop file and convert image file
def loop_file(dir_src, dst):
    for (root, dirs, files) in os.walk(dir_src):
        for f_name in files:
            src_name = os.path.join(root, f_name)
            convert_img(src_name, dst)

# add args for command line
parser = argparse.ArgumentParser(description='Convert heic to jpeg.')
parser.add_argument('-i', '--input', help='Input file name, heic format.')
parser.add_argument('-s', '--src', default=os.getcwd(), help='Source directory name with heic image file. default=cwd')
parser.add_argument('-d', '--dst', default=os.path.join(os.getcwd(),"export"),help='Destination directory to save jpeg file.')
args = parser.parse_args()

src = args.input
dir_src = args.src
dir_dst = args.dst

if src and (dir_src != os.getcwd()):
    print("Not allowed args, exit!")
    exit(0)
elif src:
    convert_img(src, dir_dst)
elif dir_src:
    loop_file(dir_src, dir_dst)
else:
    print("Not allowed args, exit!")
    exit(0)