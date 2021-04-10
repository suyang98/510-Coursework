import csv
rows = []
count = 0
with open("student-mat.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        tmp = row[0].replace("\"","").split( ";")
        if count == 0:
            headers = tmp
        else:
            rows.append(tmp)
        count = count + 1
with open('data.csv','w',newline='') as f :
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
    