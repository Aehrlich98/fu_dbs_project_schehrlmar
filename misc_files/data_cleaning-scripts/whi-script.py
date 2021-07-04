
#https://docs.python.org/3/library/csv.html
import csv
#zieht Country, Year, Score, Rank, Healthyl Life Expectancy aus world-happiness-index.csv
#und fügt sie in dieser Spalten-Ordnung als neue CSV zusammen:

#Das Script ist hardgecoded für dei speziellen Formatierungen der fuenf Dateien und muss im gleichen Ordner wie sie ausgeführt werden

def main():
	
	
	data_length = 155	#TODO #amount of lines to be used from each csv (lowest common amount of data)
	filenames_field=["2015.csv","2016.csv","2017.csv","2018.csv","2019.csv",]
	
	fields =[]
	file_index = 0
	
	for filename in filenames_field:
		
		csvfile = open(filename, newline="\n")
		datareader = csv.reader(csvfile, delimiter= ",", quotechar='"')
		next(datareader)	#steige über 1. Zeile mit Tabellen Headern hinweg.
		file_field = sorted(datareader)	#sortiert die Listen in field nach erstem Eintrag
		
		#filtere ungewünschte Einträge aus jeder Liste
		#erhalte nur Values für Country, Score, Rank, Healthy Life Expectancy 
		#da die Dateien verschiedene Abfolgen haben, muss je Datei eigen vorgegangen werden.
		for row in file_field:
			if(filename == "2015.csv" or filename == "2016.csv"):
				row.pop(1);row.pop(3);row.pop(3);row.pop(3);row.pop(3);
			
				#remove any after last
				while(len(row)>4):
					row.pop(4)
				#sortiere zu Country, Year, Rank, Score, Healthy
				#add Jahr
				if("15" in filename):
					row.insert(1, "2015")
				else: 
					row.insert(1, "2016")
				#DONE
				
			elif(filename =="2017.csv"):
				row.pop(3);row.pop(3);row.pop(3);row.pop(3);
				#remove any after last
				while(len(row)>4):
					row.pop(4)
				#sortiere zu Country, Year, Rank, Score, Healthy
				#add Jahr
				row.insert(1, "2017")
				#DONE
				
			else:
				row.pop(3);row.pop(3);
				#remove any after last
				while(len(row)>4):
					row.pop(4)
					
				#sortiere zu Country, Year, Rank, Score, Healthy
				row.insert(2, row[0]); row.pop(0)	#Score von index 0 zu 1, dann entferne vom ersten Eintrag
				#add Jahr
				if("18" in filename):
					row.insert(1, "2018")
				else:
					row.insert(1, "2019")		
				#DONE
					
		#save gathered data
		fields.append(file_field)
		file_index += 1
		#END for
		
	print("fields len: " + str(len(fields)))
	print(fields[4])
	#erzeuge neue CSV mit gegeb Werten
	with open("world-happiness-index_COMBINED.csv", "w", newline="\n") as csvfile_write:
		datawriter= csv.writer(csvfile_write)
		
		csv_field = []
		for field in fields:
			for row in field:
				#if "Country" in row[0]:		#spare Tabellenüberschriften aus, dei bis jetzt mitübertragen wurden.
				#	continue
				csv_field.append(row)
					#print("yees! ")
		csv_field.sort()
		for row in csv_field:
			datawriter.writerow(row)
				
	
	return

if __name__ == "__main__":
	main()