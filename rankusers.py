import csv, sys, operator

with open('final_output_2_header.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["UserID", "u1", "Hate","PropHate","u4","tweets"])

    with open('final_output_2.csv', 'rU') as incsv:
        reader1 = csv.reader(incsv)
        writer.writerows(row for row in reader1)

     
data = csv.reader(open('final_output_2_header.csv'))
sortedlist = sorted(data, key=operator.itemgetter(4))    
with open("final_output_2_sorted.csv", "wb") as f:
    fileWriter = csv.writer(f)
    for row in sortedlist:
        fileWriter.writerow(row)