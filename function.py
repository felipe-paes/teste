import csv

def insert(name, especie, dono):
    with open('hotel.csv', 'at', newline='') as file_out:
        fieldnames = ['name', 'especie', 'dono']
        writer = csv.DictWriter(file_out, fieldnames=fieldnames)
        writer.writerow({'name': name, 'especie': especie, 'dono': dono})

def remove(i):
    i += 1
    with open('hotel.csv', 'r') as file_in:
        lines = file_in.readlines()
        pointer = 1
        with open('hotel.csv', 'w') as file_out:
            for line in lines:
                if pointer != i:
                    file_out.write(line)
                pointer += 1
    return

def alternate(i, name, especie, dono):
    remove(i)
    insert(name, especie, dono)
    return