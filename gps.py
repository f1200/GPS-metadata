from PIL import Image
IMG=Image.open("Y.jpg")
from PIL import ExifTags
ED={
    ExifTags.TAGS[k]: v
    for k,v in IMG.getexif().items()
    if k in ExifTags.TAGS
}
try:
    print(ED)
except:
    pass
