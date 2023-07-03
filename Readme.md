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
This utility is a python script which uses ffmpeg under the hood. In order to run this, ensure that you have the following pre-requesites installed on your system:
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