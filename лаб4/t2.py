# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

indent = 4

dictions = []

def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dictions.append(dict(row))


    with open(OUTPUT_FILENAME, 'w') as file2:
        json.dump(dictions, file2, indent=indent)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
