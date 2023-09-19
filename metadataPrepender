#Appends beat metadata such as bpm and scale info to start of beat name, coz the sp screen does not show complete names when [Remain] is pressed
import re
import sys
import os

keys = []
for i in range(ord('A'), ord('G')+1):
    keys.append(str(chr(i)))

#assuming that scale info is in the format Am, A#m, Bbm, BMaj OR A min, A# min, B Maj
scales = ["m","min","Maj", "Major", "minor", "Minor"]
sharp_flat = ["#","b"]
#some keys do not not have sharp or flats but we don't care
for i in range(0,len(keys)-1):
    k = keys[i]
    keys.append(k + "#")
    keys.append(k + "b")

keywordsOfInterest = []
for key in keys:
    for scale in scales:
        keywordsOfInterest.append(key + scale)
        keywordsOfInterest.append(f"{key} {scale}")

def suggestName(name):
    """returns a new name for the given filename. Output will be of format bpm-scale-name.ext"""
    bpm = None
    assumedScale = None
    for keyword in keywordsOfInterest:
        escapedKeyword = re.escape(keyword)
        match = re.search(f"\\b{escapedKeyword}\\b", name, re.IGNORECASE)
        if match:
            assumedScale = match.group()
            #there is a chance that - is used as separator. So we replace all "-" with a space
            for word in name.replace("-"," ").split():
                if word.isdigit():
                    bpm = word
                    break
            break

    if bpm is None and assumedScale is None:
        return name
    ext = name.split(".")[-1]
    newFileName = name.replace(bpm,'').replace(assumedScale,'').replace('bpm','').replace('BPM','').replace(ext,"").replace(".","")
    newFileName = newFileName.replace("-"," ").strip()
    words = newFileName.split()
    return f"{bpm}-{assumedScale}-{' '.join(words)}.{ext}"


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

confirm = input(f"Samples will be RENAMED. Continue? (y/n): ")
if confirm != "y":
    print("exiting...")
    exit(0)

# start copy process
for (dirpath, dirnames, filenames) in os.walk(directory):
    fileCount = len(filenames)
    print(f"Processing {fileCount} files in {dirpath} ->")
    for filename in filenames:
        if filename.startswith("."):
                continue
        filenameLower = filename.lower()
        if filenameLower.endswith(".wav") or filenameLower.endswith(".mp3"):
            newName = suggestName(filename)
            if newName != filename:
                src = os.path.join(dirpath,filename)
                dest = os.path.join(dirpath, newName)
                print(filename, "-->",newName)
                os.rename(src,dest)
                fileCount = fileCount - 1
    print(f"\n{fileCount} files ignored")

print("Done!")