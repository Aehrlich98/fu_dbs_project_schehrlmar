
#https://docs.python.org/3/library/csv.html
import csv
#zieht Country, Year, Score, Rank, Healthyl Life Expectancy aus world-happiness-index.csv
#und fügt sie in dieser Spalten-Ordnung als neue CSV zusammen:

#Das Script ist hardgecoded für dei speziellen Formatierungen der fuenf Dateien und muss im gleichen Ordner wie sie ausgeführt werden

def main():

	filename="owid-co2-data.csv"
	
	csvfile = open(filename, newline="\n")
	datareader = csv.reader(csvfile, delimiter= ",", quotechar='"')
	#
	csv_field =[]
	#read each row out of reader-iterator
	for line in datareader:
		row = line
		#skip unwanted dates
		if(row[2] not in ("2015", "2016", "2017", "2018", "2019")):
			continue
		#sort out iso code on index "0" and anthing after total Co2 count (index 2)
		row.pop(0);
		while(3<len(row)):
			row.pop(3)
		try:
			row[2] = str(1000000 * float(row[2]))
		except ValueError:
			print("whoops")
		csv_field.append(row)
	
	#die totaler Co2 emissionen sind Mil. Tonnen angegeben. Gleiche auf basolute Werte an.
	csv_field.sort()	
	#erzeuge neue CSV mit gegeb Werten
	with open("owid-co2-data_CLEANED.csv", "w", newline="\n") as csvfile_write:
		datawriter= csv.writer(csvfile_write)
		
		for row in csv_field:
			datawriter.writerow(row)

if __name__ == "__main__":
	main()