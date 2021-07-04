
#https://docs.python.org/3/library/csv.html
import csv
#zieht Country, Year, Score, Rank, Healthyl Life Expectancy aus world-happiness-index.csv
#und fügt sie in dieser Spalten-Ordnung als neue CSV zusammen:

#Das Script ist hardgecoded für dei speziellen Formatierungen der fuenf Dateien und muss im gleichen Ordner wie sie ausgeführt werden

def main():

	
	growth_csvfile = open("population_growth_CLEANED.csv", newline="\n")
	growth_datareader = csv.reader(growth_csvfile, delimiter= ",", quotechar='"')
	total_csvfile = open("population_total_CLEANED.csv", newline="\n")
	total_datareader = csv.reader(total_csvfile, delimiter= ",", quotechar='"')
	#
	csv_field =[]
	i = 0
	#read each row out of reader-iterator
	for row in total_datareader:
		try:
			i +=1
			pop_total = next(growth_datareader)
			row.append(pop_total[2])
		except StopIteration:
			print("growth Population shorter than total! pleease check Files!\nQuitting...")
			return -1
		
		csv_field.append(row)
		
	csv_field.sort()
	#erzeuge neue CSV mit gegeb Werten
	with open("population_CLEANED.csv", "w", newline="\n") as csvfile_write:
		datawriter= csv.writer(csvfile_write)
		for row in csv_field:
			datawriter.writerow(row)
			
	return



if __name__ == "__main__":
	main()