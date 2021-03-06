import math
from Ctimer import *
from Etimer import *
from realTimer import *
def calc_standardDeviation(file_in,f_Average,typeTimer, typeCom):
	f_data = open(file_in,"r")
	average = 0
	stdDev = 0
	counter = 0
	t_max = 0
	t_min = 10000
	for ligne in f_data:
		line = ligne.split(" ")
		data = int(line[4])
		average += data
		counter += 1
		if t_max < data:
			t_max = data
		if t_min > data:
			t_min = data 

	average /= counter
	counter = 0

	f_data.seek(0)
	for ligne in f_data:
		line = ligne.split(" ")
		data = int(line[4])
		stdDev += math.pow((data-average),2)
		counter += 1
	stdDev /= counter
	stdDev = math.sqrt(stdDev)
	counter = 0
	f_Average.write("/***********"+ typeTimer +"****************/" + "\n")
	f_Average.write("->	" + typeCom + "\n")
	f_Average.write(" Time max = " +str(t_max)+ " Time min = " +str(t_min)+ " Time average = " +str(average)+ " Standard deviation = "+str(stdDev)+ "\n")
	f_data.close()

if __name__ == "__main__":
	f_Average = open("Average.txt","w")
	startCTimer()
	startETimer()
	startRealTimer()
	calc_standardDeviation("Ctimer/ProperDataReceiver.txt",f_Average,"Ctimer", "Reception")
	calc_standardDeviation("Ctimer/ProperDataSender.txt",f_Average,"Ctimer", "Sending")
	calc_standardDeviation("Etimer/ProperDataReceiver.txt",f_Average,"Etimer", "Reception")
	calc_standardDeviation("Etimer/ProperDataSender.txt",f_Average,"Etimer", "Sending")
	calc_standardDeviation("realTimer/ProperDataReceiver.txt",f_Average,"Rtimer", "Reception")
	calc_standardDeviation("realTimer/ProperDataSender.txt",f_Average,"Rtimer", "Sending")
	f_Average.close()
	
