import csv

with open(r"C:\Users\ibsle\Documents\quantium-starter-repo\data\daily_sales_data_0.csv", newline="") as file:
    sales = csv.reader(file, delimiter = ",")
    file = open("data\sales.txt","a")

    for row in sales:
        product = row[0].strip()
        if product == "pink morsel":
            file.write(f"Sales: {int(row[2]) * float(row[1].replace("$", "").replace(",", "").replace(".",""))/100}, Date: {row[3]}, Region: {row[4]}\n")
with open(r"C:\Users\ibsle\Documents\quantium-starter-repo\data\daily_sales_data_1.csv", newline="") as text:
    sales = csv.reader(text, delimiter = ",")
    file = open("data\sales.txt","a")

    for row in sales:
        product = row[0].strip()
        if product == "pink morsel":
           file.write(f"Sales: {int(row[2]) * float(row[1].replace("$", "").replace(",", "").replace(".",""))/100}, Date: {row[3]}, Region: {row[4]}\n")
with open(r"C:\Users\ibsle\Documents\quantium-starter-repo\data\daily_sales_data_2.csv", newline="") as text_2:
    sales = csv.reader(text_2, delimiter = ",")
    file = open("data\sales.txt","a")

    for row in sales:
        product = row[0].strip()
        if product == "pink morsel":
           file.write(f"Sales: {int(row[2]) * float(row[1].replace("$", "").replace(",", "").replace(".",""))/100}, Date: {row[3]}, Region: {row[4]}\n")
