import csv


#https://realpython.com/python-csv/
with open('datasets/train/prelabel/ExtractedTweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print("Processing training dem/rep files...")
    for row in csv_reader: #party, handle, tweets row[1],2,3
        if line_count == 0:
            line_count += 1
        else:
            if row[0] == "Democrat":
                demo_file = open("datasets/train/democratic/"+row[1], "w+")
                demo_file.write(row[2])
                demo_file.close()
            elif row[0] == "Republican":
                repub_file = open("datasets/train/republican/"+row[1], "w+")
                repub_file.write(row[2])
                repub_file.close()
        line_count += 1
    print("Processing completed")
