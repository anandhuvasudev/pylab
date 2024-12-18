import csv

filename = 'data2.csv'
colnum=int(input("Enter columns "))
columns_to_read = [colnum]

try:
    with open(filename, mode='r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        print("Header:", [header[i] for i in columns_to_read])
        for row in csv_reader:
            selected_columns = [row[i] for i in columns_to_read]
            print(selected_columns)
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
