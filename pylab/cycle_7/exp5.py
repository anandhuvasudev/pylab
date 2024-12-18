import csv

def read_dictionary_from_user():
    data_dict = []
    while True:

        name = input("Enter name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        age = input("Enter age: ")
        city = input("Enter city: ")

        data_dict.append({'Name': name, 'Age': age, 'City': city})
    return data_dict


filename = 'output.csv'

data_dict = read_dictionary_from_user()

try:
    with open(filename, mode='w', newline='') as csvfile:

        csv_writer = csv.DictWriter(csvfile, fieldnames=data_dict[0].keys())
        csv_writer.writeheader()

        csv_writer.writerows(data_dict)

    print(f"Data written to {filename} successfully.")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

try:
    with open(filename, mode='r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        print("\nContent of the CSV file:")
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print(f"The file {filename} was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
