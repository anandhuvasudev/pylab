filename = 'example.txt'
lines = []
try:
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(lines)
