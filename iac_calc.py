# iac_calc.py

# The Internet Audio Cyclotron Data Destruction Calculator
# version 0.5 (writes results to file, then reads file and prints to screen)

# Calculates the data destruction wrought by the Audio Cyclotron
# This version is for configurations with multiple encoders of differing bitrates
# Requires Python3

# by jmg*AT*phasechange*DOT*info
# April 29th 2014

# Import Decimal type to enable greater precision
from decimal import Decimal

# Present title
def title ():
	print ()
	print ("-------------------------------------------------------------------------")
	print ("-        Internet Audio Cyclotron | Data Destruction Calculator         -")
	print ("-------------------------------------------------------------------------")
	print ("-                          v0.5 | April 2014                            -")
	print ("-------------------------------------------------------------------------")
	print ("-     For single encoder or multiple encoders of different bitrates     -")
	print ("-------------------------------------------------------------------------")
	print ()

# Capture user input
def userinput (): 
	iactitle = str (input ("Enter the title of the piece: "))
	iacartist = str (input ("Enter the name of the artist(s): "))
	iacdate = str (input ("Enter the date of the performance: "))
	durationmins = float (input ("Enter the duration of the piece (in minutes): "))
	ipbitrate = float (input ("Enter the input bitrate in Kbps (CD-quality is 1411): "))
	looptime = float (input ("Enter the time taken to complete a cycle (in seconds): "))
	loopdist = float (input ("Enter the total loop distance (in km): "))

	return iactitle, iacartist, iacdate, ipbitrate, looptime, loopdist, durationmins


# Deal with audio encoders
def encoders (ipbitrate): 
	encs = []
	encpcs = []
	compratios = []
	encnumber = float (input ("Enter the number of encoders/stream-servers being used: "))
	encloop = int (encnumber)

	# Capture all encoder bitrates, calculate compression ratios and destruction percentages
	for i in range (encloop):
		encbitrate = float (input ("Enter the encoder/server bitrate in Kbps: "))
		compratio = float (ipbitrate / encbitrate)
		compratior = round (compratio, 3)
		encpc = round ((100- (100 * (encbitrate / ipbitrate))), 3)

		# Store all three sets of values in lists
		encs.append (encbitrate)
		compratios.append (compratior)
		encpcs.append (encpc)

	# Multiply encs list elements for later 'destruction.dataremains()' calculation
	encproduct = float (1.0)
	for i in encs:
		encproduct = encproduct * i

	# Multiply compratios list elements to calculate cumuative compression ratio
	compratioproduct = float (1.0)
	for i in compratios:
		compratioproduct = compratioproduct * i

	return encs, compratios, encpcs, encproduct, encnumber, encloop, compratioproduct 


# Calculate all loop and duration stuff
def loops (looptime, loopdist, durationmins):

	loopspermin = 60 / looptime
	loopspeed = loopdist / looptime
	looptotal = durationmins * loopspermin
	durationsecs = looptime * looptotal
	totaldist = loopspeed * durationsecs

	return loopspermin, loopspeed, looptotal, totaldist


# Calculate the destruction wrought by the process
def destruction (ipbitrate, encnumber, looptotal, encproduct):

	ipbitratedec = (Decimal (ipbitrate))
	encnumberdec = (Decimal (encnumber))
	looptotaldec = (Decimal (looptotal))
	encproddec = (Decimal (encproduct))

	# The business end
	dataremains = (Decimal (ipbitratedec ** (1 - (encnumberdec * looptotaldec))) * (encproddec ** looptotaldec))

	# Calculate bps and perentages
	dataremainsbps = (Decimal ( dataremains * 1024))
	dataremainspc = (Decimal (dataremains / ipbitratedec) * 100)
	dataremainspcr = round (Decimal (100 - dataremainspc), 3)

	return dataremains, ipbitratedec, dataremainsbps, dataremainspc, dataremainspcr


# Output results
def iacoutput (iactitle, iacartist, iacdate, durationmins, ipbitrate, encloop, encs, compratios, encpcs, compratioproduct, looptime, loopspermin, loopdist, looptotal, loopspeed, totaldist, dataremains, dataremainsbps, dataremainspc, dataremainspcr):
	
	# Format results, as they don't need all the decimal places
	ipbitrateint = int (ipbitrate)	
	compratioprodr = round (compratioproduct, 3)
	loopsperminr = round (loopspermin, 3)
	loopspeedr = round (loopspeed, 3)
	totaldistr = round (totaldist, 3)
	looptotalint = int (looptotal)

	# output file 'iac.txt'
	iac = open ('iac.txt', 'a')

	print ("\n", file = iac)
	print ("---------------------------------------------------------------------------------", file = iac)
	print ("-            Internet Audio Cyclotron | Data Destruction Calculator             -", file = iac)
	print ("---------------------------------------------------------------------------------", file = iac)
	print ("\n", file = iac)
	print ("THE PIECE: ", file = iac)
	print (iactitle, "by", iacartist, "was performed on", iacdate, file = iac)
	print ("It ran for", durationmins, "minutes", file = iac)
	print ("\n", file = iac)
	print ("CLIENT PARAMETERS: ", file = iac)
	print ("Input bitrate: ", ipbitrate, file = iac)
	print ("Encoder bitrate(s):", encs, file = iac)
	print ("Encoder compression ratio(s):", compratios, file = iac)
	print ("Compression ratio of all encoders (connected in series):", compratioprodr,"to 1", file = iac)
	print ("\n", file = iac)
	print ("LOOP PARAMETERS: ", file = iac)
	print ("Cycle time: ", looptime, "seconds", file = iac)
	print ("Loop distance: ", loopdist, "Km", file = iac)
	print ("Cyclotron speed:", loopsperminr, "loops per minute", file = iac)
	print ("Cyclotron traversals:", looptotalint, "loops", file = iac)
	print ("Signal speed (Km/s):", loopspeedr, "Kms per second", file = iac)
	print ("The signal will travel", totaldistr, "Km in total", file = iac)
	print ("\n", file = iac)
	print ("DATA DESTRUCTION: ", file = iac)
	print ("Encoder data destruction percentage(s): ", encpcs, file = iac)
	print ("Data remaining (Kbps):", dataremains, "Kbps", file = iac)
	print ("Data remaining (bps):", dataremainsbps, "bps", file = iac)
	print ("As a percentage, this equates to", dataremainspc, "%", file = iac)
	print ("Around", dataremainspcr, "percent of the original sound is now noise and artefacts", file = iac)
	print ("\n", file = iac)
	print ("---------------------------------------------------------------------------------", file = iac)
	print ("-                     (c) 2014 | jmg*AT*phasechange*DOT*info                    -", file = iac)
	print ("---------------------------------------------------------------------------------", file = iac)
	print ("\n", file = iac)
	iac.close ()


# Open 'iac.txt' file and print to screen
def writetoscreen ():
	infile = open ('iac.txt', 'r')
	iacdata = infile.read ()
	print (iacdata)
	infile.close ()

# Organise it all
def main ():

	title ()

	iactitle, iacartist, iacdate, ipbitrate, looptime, loopdist, durationmins = userinput ()

	encs, compratios, encpcs, encproduct, encnumber, encloop, compratioproduct = encoders (ipbitrate)

	loopspermin, loopspeed, looptotal, totaldist = loops (looptime, loopdist, durationmins)

	dataremains, ipbitratedec, dataremainsbps, dataremainspc, dataremainspcr = destruction (ipbitrate, encnumber, looptotal, encproduct)

	iacoutput (iactitle, iacartist, iacdate, durationmins, ipbitrate, encloop, encs, compratios, encpcs, compratioproduct, looptime, loopspermin, loopdist, looptotal, loopspeed, totaldist, dataremains, dataremainsbps, dataremainspc, dataremainspcr)

	writetoscreen ()

# Run it
main ()
