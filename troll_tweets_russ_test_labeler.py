import csv


#https://realpython.com/python-csv/
with open('datasets/test/prelabel/russian-troll-tweets/tweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print("Processing russian-troll-tweet files...")
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            file = open("datasets/test/testpayload/"+row[1], "w+")
            file.write(row[7])
            file.close()
          
        line_count += 1
    print("Processing completed")
