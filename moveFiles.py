import shutil
import glob

# set source folder and destination folder
sourceFolder = 'C:\\Users\\Luke.Moglia\\OneDrive - DN Colleges Group\\Pictures'
destinationFolder = 'C:\\Users\\Luke.Moglia\\OneDrive - DN Colleges Group\\Pictures\\ClippingTool'

# select clipping tool pictures and move into clipping tool folder
for clippingTool in glob.glob(sourceFolder + '\\ct_*'):
    print(clippingTool)
    shutil.move(clippingTool, destinationFolder)
