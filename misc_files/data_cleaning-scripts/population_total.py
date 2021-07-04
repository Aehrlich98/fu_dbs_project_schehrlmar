
#https://docs.python.org/3/library/csv.html
import csv
#zieht Country, Year, Score, Rank, Healthyl Life Expectancy aus world-happiness-index.csv
#und fügt sie in dieser Spalten-Ordnung als neue CSV zusammen:

#Das Script ist hardgecoded für dei speziellen Formatierungen der fuenf Dateien und muss im gleichen Ordner wie sie ausgeführt werden

def main():

	filename="population_total.csv"
	date_start= 2015-1960
	date_end = 2019-1960
	
	csvfile = open(filename, newline="\n")
	datareader = csv.reader(csvfile, delimiter= ",", quotechar='"')
	next(datareader)#drop first line, containing Table hader
	#
	csv_field =[]
	#read each row out of reader-iterator
	for row in datareader:
		if(row[1] not in ("2015", "2016", "2017", "2018", "2019")):
			continue
		csv_field.append(row)
		
		if(row[1] == "2017"):
			csv_field.append([row[0], "2018", ""])
			csv_field.append([row[0], "2019", ""])
		
	csv_field.sort()
	#erzeuge neue CSV mit gegeb Werten
	with open("population_total_CLEANED.csv", "w", newline="\n") as csvfile_write:
		datawriter= csv.writer(csvfile_write)
		for row in csv_field:
			datawriter.writerow(row)
			
	return



if __name__ == "__main__":
	main()