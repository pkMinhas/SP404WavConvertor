# Removes all provided phrases from the filenames. Sample packs downloaded from popular providers have long file names of format <Provider>-<Pack>-<SampleName>.wav.
# Edit the wordsToRemove dictionary to add words that you wish to remove from the renamed files
import os
import sys

finalMessageArr = []

# Edit this line to remove other words/phrases/characters from the file names
wordsToRemove = ["Cymatics","ADSR","Beatclub"]

def diveInto(directory):
    print(f"Processing {directory}")
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
            fixedFilename = filename
            # remove unwanted words from string
            for word in wordsToRemove:
                fixedFilename = fixedFilename.replace(word,"")
            
            fixedFilename = fixedFilename.strip()

            if fixedFilename.startswith("-"):
                fixedFilename = fixedFilename[1:]

            fixedFilename = fixedFilename.replace(" - ","-").strip()
            
            if fixedFilename == filename:
                skipped = skipped + 1
            else:
                newFilePath = os.path.join(directory, fixedFilename)
                print(f"Rename {filename} to {fixedFilename}")
                os.rename(f,newFilePath)
                processed = processed + 1

    finalMessageArr.append(f"{directory} - files processed: {processed}, skipped: {skipped}")


# Renames all files in dir (recursive). Removes common sample pack provider names from filenames.
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

