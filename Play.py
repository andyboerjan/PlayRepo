from datetime import datetime

## input file ##
my_file = open('Input.txt', encoding="UTF-8")

## output file ##
output_file = open("Output.txt --- " + datetime.now().strftime('%Y-%m-%d') + ".txt", "w", encoding="UTF-8")
output_file.write("Running the Play App at: " + str(datetime.now()) + "\n")

for line in my_file:
    output_file.write(line + "\n")

output_file.write("Completed the Play App at: " + str(datetime.now()) + "\n")
##print(bookingResults)
my_file.close()
output_file.close()
