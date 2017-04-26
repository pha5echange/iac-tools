# auto_iac03.py

# Automated Internet Audio Cyclotron
# version a0.3
# April 25th 2017

# Looping MP3 encoder

# Requires an 'audio' subfolder where files are sought for encoding

# by jmg*AT*phasechange*DOT*info
# Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/

import os
import glob
from pydub import AudioSegment

versionNumber = 'a03'

audio_dir = 'audio/'  # dir where the files are located
extension_list = ('*.wav')

# get user input
encBitRateInt = int(input("Enter the desired encoder bitrate - options are 8, 16, 24, 32, 40, 48, 64, 80, 96, 112, 128, 160, 192, 224, 256 or 320: "))

if encBitRateInt == 8:
	encBitRateStr = '8k'

elif encBitRateInt == 16:
	encBitRateStr = '16k'	

elif encBitRateInt == 24:
	encBitRateStr = '24k'

elif encBitRateInt == 32:
	encBitRateStr = '32k'

elif encBitRateInt == 40:
	encBitRateStr = '40k'

elif encBitRateInt == 48:
	encBitRateStr = '48k'

elif encBitRateInt == 64:
	encBitRateStr = '64k'

elif encBitRateInt == 80:
	encBitRateStr = '80k'

elif encBitRateInt == 96:
	encBitRateStr = '96k'

elif encBitRateInt == 112:
	encBitRateStr = '112k'

elif encBitRateInt == 128:
	encBitRateStr = '128k'

elif encBitRateInt == 160:
	encBitRateStr = '160k'

elif encBitRateInt == 192:
	encBitRateStr = '192k'

elif encBitRateInt == 224:
	encBitRateStr = '224k'

elif encBitRateInt == 256:
	encBitRateStr = '256k'

elif encBitRateInt == 320:
	encBitRateStr = '320k'

else:
	print ("Invalid bitrate.")
	print ("Please enter 8, 16, 24, 32, 40, 48, 64, 80, 96, 112, 128, 160, 192, 224, 256 or 320")

loops = int(input("Enter the number of passes through the encoder: "))

print
print('Processing ' + str(loops) + ' encoder passes at ' + encBitRateStr)
print

os.chdir(audio_dir)

loopCounter = 0

sourceFile = open("source.wav", "r")

mp3FileName = 'output_' + str(loopCounter) + '.mp3'
AudioSegment.from_file(sourceFile).export(mp3FileName, format='mp3', bitrate=encBitRateStr)

sourceFile.close()

mp3SourceName = mp3FileName

while (loopCounter < loops):

	mp3File = open(mp3SourceName, "r")

	loopPlus = loopCounter + 1

	mp3FileName = 'output_' + str(loopPlus) + '.mp3'
	AudioSegment.from_file(mp3File).export(mp3FileName, format='mp3', bitrate=encBitRateStr)

	mp3File.close()

	mp3SourceName = mp3FileName

	loopCounter += 1
