import json

file = "input.json"

def task() -> float:
    sum = 0
    with open(file, 'r') as f:
        data = f.read()
        data_d = json.loads(data)
        for diction in data_d:
            numbers = 1
            for key in diction:
                numbers *= diction[key]
            sum += numbers
    return(round(sum, 3))


print(task())