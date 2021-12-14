def main():
	with open("l_r_kons_prog.csv", "r") as file:
		text = file.read()
		konsLines = text.split("\n") # load lines
		konsLines = konsLines[3:] # remove title and weird empty lines
		del konsLines[-20:] # remove empty end lines
		for i in range(len(konsLines)):
			konsLines[i] = konsLines[i].split(",", 1)[1] # remove custom numbering
			konsLines[i] += "\n"

		asDict = {} # create dictionary
		for line in konsLines:
			split = line.split(",", 1)
			asDict[float(split[0])] = split[1]

		result = []
		# create missing entries
		with open("swissvotes_dataset_after_1900_utf8.csv", "r") as swiss:
			data = swiss.read()
			lines = data.split("\n")
			del lines[0] # remove title
			for l in lines:
				if l != "":
					split = l.split(";")
					i = float(split[0])
					if float(i) in asDict: # if the line already exists take it
						result += [str(i) + "," + asDict[i]]
					else: # else create a new line from big dataset
						date = split[1].split(".")
						dateFormatted = date[2]+"-"+date[1]+"-"+date[0]
						title = split[2].replace(",", ";")
						toAdd = str(split[0]) + "," + dateFormatted + "," + title + "," + "NaN,NaN,Nan\n"
						result += [toAdd]

			with open("l_r_kons_prog_padded.csv", "w") as save:
				print("Writing to l_r_kons_prog_padded.csv")
				writeData = "".join(result)
				save.write(writeData)
		

if __name__ == "__main__":
	main()