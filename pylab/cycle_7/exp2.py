input_filename = 'input.txt'
output_filename = 'output.txt'

try:
    with open(input_filename, 'r') as infile:
        with open(output_filename, 'w') as outfile:
            for index, line in enumerate(infile, start=1):
                if index % 2 != 0:
                    outfile.write(line)
except FileNotFoundError:
    print(f"The file {input_filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"Odd lines from {input_filename} have been copied to {output_filename}.")
