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

        if filename.startswith("._"):
            continue
        
        # Check for supported audio file extensions
        supported_extensions = ['.wav', '.mp3', '.flac', '.aac', '.ogg', '.m4a', '.wma']
        if not any(filename.lower().endswith(ext) for ext in supported_extensions):
            continue
        
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
            try:
                probe = ffmpeg.probe(f)
                audioInfo = probe["streams"][0]
                codec_name = audioInfo["codec_name"]
                sample_rate = audioInfo["sample_rate"]
                print(codec_name, sample_rate)
                
                # Determine output filename
                if filename.lower().endswith('.wav'):
                    output_filename = filename
                    if codec_name == "pcm_s16le" and sample_rate == "48000":
                        print("Already meets requirement, skipping...")
                        skipped = skipped + 1
                        continue
                else:
                    # For non-WAV files, output as WAV
                    output_filename = os.path.splitext(filename)[0] + '.wav'
                
                stream = ffmpeg.input(f)
                tempFile = os.path.join(tempfile.gettempdir(), output_filename)
                ffmpeg.output(stream, tempFile, acodec="pcm_s16le", ar="48000").run(overwrite_output=True)
                
                # Overwrite original or create new WAV file
                output_path = os.path.join(os.path.dirname(f), output_filename)
                shutil.move(tempFile, output_path)
                
                # If converting a non-WAV file, remove the original
                if not filename.lower().endswith('.wav'):
                    os.remove(f)
                
                processed = processed + 1
            except Exception as e:
                print(f"[!!] Some exception occurred while processing {filename}: {e}")
                skipped = skipped + 1

    finalMessageArr.append(f"{directory} - files processed: {processed}, skipped: {skipped}")


# Converts all supported audio files in given directory to 16bit, 48khz WAV
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
confirm = input("Supported audio files will be converted to 16bit, 48khz WAV. Non-WAV files will be replaced with WAV versions. Continue? (y/n): ")
if confirm != "y":
    print("exiting...")
    exit(0)

diveInto(directory)

for msg in finalMessageArr:
    print(msg)
print("Done!")

