# Collates files in a pack, clubbing them into folders covering: kicks, snares, claps etc...
import os
import sys
import shutil

# change this list to add terms to search list
categories = ["kick", "snare", "clap", "hat", "cymbal","crash", "tom", "808", "bass", "perc", "fx", "vox", "vocal", "fill"]

# all samples will be placed in folders under this dir. Will be populated based on user input
oneshotRootDir = ""

# map of category to dest. dir
categoryToDirMap = {}

def makeSampleFolders():
    """Makes sample folders in the collationRootDir dir"""
    for i in range(len(categories)):
        cat = categories[i]
        dir = os.path.join(oneshotRootDir, f"{i}. {cat}")
        if not os.path.exists(dir):
            os.mkdir(dir)
        categoryToDirMap[cat] = dir
        

# Classifies (no ML, simple name based classification only) and copies all files in dir (recursive) to folders under root folder
argLen = len(sys.argv)
if argLen != 2:
    print("Please provide input directory path")
    exit(1)

directory = sys.argv[1]
print("*")
print("*")
print("* CAUTION: This utilty will run a deep scan within the directory. All subdirectories will be processed. Do keep a backup of your data before proceeding...")
print("")
print(f"Processing {directory}")

oneshotRootDir = os.path.join(directory, "0. one-shots")

confirm = input(f"Samples will be copied to folders under {oneshotRootDir}. Continue? (y/n): ")
if confirm != "y":
    print("exiting...")
    exit(0)


if not os.path.exists(oneshotRootDir):
    os.mkdir(oneshotRootDir)

print("Be patient, this will take a while...")
makeSampleFolders()

# start copy process
for (dirpath, dirnames, filenames) in os.walk(directory):
    # ignore the one shot dir
    if dirpath.startswith(oneshotRootDir):
        continue
    fileCount = len(filenames)
    print(f"Processing {fileCount} files in {dirpath} ->")
    for filename in filenames:
        filenameLower = filename.lower()
        if filenameLower.endswith(".wav") or filenameLower.endswith(".mp3"):
            for cat in categories:
                if cat in filenameLower:
                    src = os.path.join(dirpath,filename)
                    dest = os.path.join(categoryToDirMap[cat], filename)
                    shutil.copyfile(src,dest)
                    fileCount = fileCount - 1
                    print(".",end="")
                    break
    print(f"\n{fileCount} files ignored")

print("Done!")