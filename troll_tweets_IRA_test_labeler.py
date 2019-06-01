import csv
import glob

IRA_files = glob.glob('datasets/test/prelabel/russian-troll-tweets-IRA-handle/*')
#https://realpython.com/python-csv/

print("Processing russian-troll-tweets-IRA-handle files...")
for file in IRA_files:
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[4] == "English":
                    print("succ")
                    file = open("datasets/test/testpayload/"+row[1], "w+")
                    file.write(row[2])
                    file.close() 
        line_count += 1
        
print("Processing completed")
