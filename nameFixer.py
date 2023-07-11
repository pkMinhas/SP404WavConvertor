import shutil
import os
import sys

finalMessageArr = []

def diveInto(directory):
    print(f"Processing {directory}")
    dirName = directory.split(os.sep)[-1]
    processed = 0
    skipped = 0

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        #if directory, dive into this directory and process
        if os.path.isdir(f):
            diveInto(f)

        if filename.startswith("._") or not filename.lower().endswith(".wav"):
            continue
        
        # checking if it is a file
        if os.path.isfile(f):
            # remove repeated name "Cymatics", "Cymatics - ", "BC" etc...
            # Edit this line to remove other words/phrases/characters from the file names
            fixedFilename = filename.replace("Cymatics -","").replace("Cymatics", "").replace("-ADSR","").replace("ADSR","").replace(" - ", "-").strip()
            if fixedFilename == filename:
                skipped = skipped + 1
            else:
                newFilePath = os.path.join(directory, fixedFilename)
                print(f"Rename {filename} to {fixedFilename}")
                tempFile = os.rename(f,newFilePath)
                processed = processed + 1

    finalMessageArr.append(f"{directory} - files processed: {processed}, skipped: {skipped}")


# Renames all files in dir (recursive). Removed common sample pack provider names from files
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
confirm = input("Files will be renamed and prefixes removed. Continue? (y/n): ")
if confirm != "y":
    print("exiting...")
    exit(0)

diveInto(directory)

for msg in finalMessageArr:
    print(msg)
print("Done!")

