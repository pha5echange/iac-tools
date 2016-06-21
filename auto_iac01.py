# auto_iac01.py

# Automated Internet Audio Cyclotron
# version a0.1
# June 21st 2016

# Basic MP3 encoder at this point
# Requires an 'audio' subfolder where .WAV files are sought for encoding

# by jmg*AT*phasechange*DOT*info
# Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/

import os
import glob
from pydub import AudioSegment

audio_dir = 'audio/'  # dir where the files are located
extension_list = ('*.wav')

os.chdir(audio_dir)
for extension in extension_list:
    for audio in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(audio))[0] + '.mp3'
        AudioSegment.from_file(audio).export(mp3_filename, format='mp3', bitrate='64k')