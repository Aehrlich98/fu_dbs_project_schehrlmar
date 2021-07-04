
#https://docs.python.org/3/library/csv.html
import csv
#zieht Country, Year, Score, Rank, Healthyl Life Expectancy aus world-happiness-index.csv
#und fügt sie in dieser Spalten-Ordnung als neue CSV zusammen:

#Das Script ist hardgecoded für dei speziellen Formatierungen der fuenf Dateien und muss im gleichen Ordner wie sie ausgeführt werden

def main():

	filename="gdp.csv"
	date_start= 2015-1960
	date_end = 2019-1960
	
	csvfile = open(filename, newline="\n")
	datareader = csv.reader(csvfile, delimiter= ",", quotechar='"')
	next(datareader)#drop first line, containing Table hader
	#
	tmp_field =[]
	#read each row out of reader-iterator
	for line in datareader:
		row = line
		row.pop(1);row.pop(1);row.pop(1);
		#print(row)
		
		i = 1
		#print("LENGTH:::::" + str(len(row)))
		while(True):
			try:
				if (i-1 < date_start):	#skip entries for unwanted dates
					row.pop(1)
				elif((date_end < i-1)):
					row.pop(6)
				i += 1
				
			except IndexError:
				break		

		tmp_field.append(row)
		print(tmp_field)
	#bis jetzt sind die Daten noch in Form einer Zeile mit Land, und Werten für alle jahre
	#nun werden sie in Form: Land, Jahr, Eintrag umgeformt
	csv_field = []
	for row in tmp_field: #Zeilen
		for i in range(1, len(row)):	#neue Zeilen aus Jahresdaten len(row) * Anzahl Eintrage großes Feld	
			csv_field.append([row[0], str(2014+i), row[i]])
	
	csv_field.sort()	
	#erzeuge neue CSV mit gegeb Werten
	with open("gdp_CLEANED.csv", "w", newline="\n") as csvfile_write:
		datawriter= csv.writer(csvfile_write)
		for row in csv_field:
			datawriter.writerow(row)
			
	return



if __name__ == "__main__":
	main()