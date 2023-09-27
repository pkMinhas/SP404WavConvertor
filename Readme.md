# Utility to convert wav files to 16bit, 48kHz - the format supported by SP 404 MK2
I have a ton of sample packs that I wish to use with my SP404MK2. However, many of the loops gave me "Unsupported File" error on the SP. 

After a couple of searches on reddit, I came to know that the SP supports 16bit,48kHz files while importing from SD Card. 

Since manual conversion of samples/loops takes a long time, I decided to automate this process and ease my life. I hope that this script helps you too.


## Salient features
1. Does a deep scan of the directory (looks into subdirectories [and subdirectories within subdirectories as well]) 
2. Converts all wav files to the specified format
3. In-place conversion. Original files are replaced
4. Does not alter the file if it already is 16bit, 48kHz
5. Uses industry-standard ffmpeg library under the hood


## Installation instructions
This utility is a python script which uses ffmpeg under the hood. In order to run this, ensure that you have the following pre-requisites installed on your system:
1. latest version of [python](https://www.python.org/downloads/)
2. [ffmpeg](https://ffmpeg.org/download.html)
3. [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)

## Usage instructions
1. Ensure that you a backup of the sample folder that you are about to convert. This will ensure that you do not loose any samples if the conversion process fails for any reason
2. Open Terminal/Command Line tools and navigate to the directory where the convertor.py script is present. 
For example, if the script is in `~/awesomeTools` directory, enter
`cd ~/awesomeTools` on the command prompt
3. Execute `python3 convertor.py <path to sample folder>` on the command prompt. For example, if the sample folder is at /Volumes/SP404MKII/IMPORT/My Sample Pack, enter `python3 convertor.py /Volumes/SP404MKII/IMPORT/My\ Sample\ Pack`
4. Follow on-screen prompts
5. Done! All samples converted to 16bit, 48kHz


## Feedback/Issues/Appreciation
Contact me via [email](mailto:preet@marchingbytes.com)

Subscribe to my [Youtube Channel](https://www.youtube.com/@BigSmilezBeats)

Follow me on [Instagram](https://www.instagram.com/bigsmilezbeats/)


#
#

# Bonus Utility: Name Fixer
Removes provided phrases from the filenames. Sample packs downloaded from popular providers have long file names of format `<Provider>-<Pack>-<SampleName>.wav`. This makes it harder to select samples on the tiny SP screen. Use this nameFixer to remove the unwanted parts from the names. For example, **Cymatics - Cicada Guitar Loop - 90 BPM D# Min Layer 1.wav** will be renamed to **Cicada Guitar Loop-90 BPM D# Min Layer 1.wav**

## Usage instructions
1. Open `nameFixer.py` and edit the `wordsToRemove` array to add words that you wish to remove from the renamed files.
2. Rest is same as above. Just replace the script name `convertor.py` with `nameFixer.py`

#
#

# Bonus 2: Collator
Collates samples from across folders into a collection, categorized as per the names defined in categories array
Script: `collator.py`


#
#

# Bonus 3: metadataPrepender
Appends beat metadata such as bpm and scale info to start of beat name, coz the sp screen does not show complete names when [Remain] is pressed.
Script: `metadataPrepender.py`