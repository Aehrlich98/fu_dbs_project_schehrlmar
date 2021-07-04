
#https://docs.python.org/3/library/csv.html
import csv
#entferne Laenderkuerzel aus der Co2-emission Tabelle und loesche alle Jahreszahlen ausserhalb 2015-19
#und fügt sie in dieser Spalten-Ordnung als neue CSV zusammen:

#Das Script ist hardgecoded für dei speziellen Formatierungen der fuenf Dateien und muss im gleichen Ordner wie sie ausgeführt werden

def helper_owid_co2():

	filename="owid-co2-data-2.csv"
	
	csvfile = open(filename, newline="\n")
	datareader = csv.reader(csvfile, delimiter= ",", quotechar='"')
	#
	csv_field =[]
	#read each row out of reader-iterator
	for line in datareader:
		row = line
		#skip unwanted dates
		if(row[2] not in ("2018", "2019")):
			continue
		#sort out iso code on index "0" and anthing after total Co2 count (index 2)
		row.pop(0);
		while(3<len(row)):
			row.pop(3)
		row[2] = str(1000000 * float(row[2]))
		csv_field.append(row)
	
	#die totaler Co2 emissionen sind Mil. Tonnen angegeben. Gleiche auf basolute Werte an.
	csv_field.sort()	
	return csv_field

def main():
	
	owid_field= helper_owid_co2()

	data_length = 155	#TODO #amount of lines to be used from each csv (lowest common amount of data)
	filenames_field=["co2_emission.csv"]
	
	for filename in filenames_field:
		
		csvfile = open(filename, newline="\n")
		datareader = csv.reader(csvfile, delimiter= ",", quotechar='"')

		csv_field=[]
		row = next(datareader)
		i = 0
		#filtere Daten ausserhalb des gegeb Zeitraums und fuege sie an
		while(True):
			try:
				if(row[2] not in ("2015","2016","2017","2018","2019")):
					row = next(datareader)
					continue
				row.pop(1)
				
				csv_field.append(row)
				try:
					if("2017" in row and i<len(owid_field)):
						print(owid_field[i])
						csv_field.append(owid_field[i])
						csv_field.append(owid_field[i+1])
					i += 2
				except IndexError:	#ignore if owid_field is not long enough
					continue
			except StopIteration as err:		#Ende of File: end loop
				break
		csv_field.sort()
	
	#erzeuge neue CSV mit gegeb Werten
	with open("co2_emission_CLEANED.csv", "w", newline="\n") as csvfile_write:
		datawriter= csv.writer(csvfile_write)
		
		for row in csv_field:
			datawriter.writerow(row)	
	
	return

if __name__ == "__main__":
	main()