import shutil
import tempfile
import ffmpeg
import os
import sys

finalMessageArr = []

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
            print(f)
            try:
                probe = ffmpeg.probe(f)
                audioInfo = probe["streams"][0]
                codec_name = audioInfo["codec_name"]
                sample_rate = audioInfo["sample_rate"]
                print(codec_name,sample_rate)
                if codec_name == "pcm_s16le" and sample_rate == "48000":
                    print("Already meets requirement, skipping...")
                    skipped = skipped + 1
                    continue
                stream = ffmpeg.input(f)
                tempFile = os.path.join(tempfile.gettempdir(),filename)
                ffmpeg.output(stream, tempFile, acodec="pcm_s16le",ar="48000").run(overwrite_output=True)
                #overwrite original with tempfile
                shutil.move(tempFile, f)
                processed = processed + 1
            except:
                print(f"[!!] Some exception occurred while processing {filename}")
                skipped = skipped + 1

    finalMessageArr.append(f"{directory} - files processed: {processed}, skipped: {skipped}")


#converts all wav files in given directory to 16bit, 48khz wav
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
confirm = input("Samples which are not 16bit, 48khz will be overwritten. Continue? (y/n): ")
if confirm != "y":
    print("exiting...")
    exit(0)

diveInto(directory)

for msg in finalMessageArr:
    print(msg)
print("Done!")

