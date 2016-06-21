IAC Tools

Python tools to aid with the creation and documentation of IAC (Internet Audio Cyclotron) pieces
www.phasechange.info/iac

Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/

IAC_CALC

Version beta 01
Requires Python3 

Calculates metrics (such as data destruction and signal distance) for a piece

Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/

1) To run >> 'python3 iac_calc.py' in a terminal

2) This version DOES NOT catch errors with input data. Be careful with your input or the program will stop. 

3) Writes 'iac.txt' to the folder that houses the script ('iac.txt' is currently set to 'append'. Move and rename if you want multiple files of results.)


AUTO_IAC

Version alpha 01
Requires the PyDub library and FFMPEG

The beginnings of an automated, local simulation of the IAC process (currently just a Python-based MP3 encoder)