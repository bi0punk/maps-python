import math

def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    distance = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    return distance

def orientation(coord1, coord2, coord3):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat3, lon3 = coord3
    val = (lon2 - lon1) * (lat3 - lat2) - (lat2 - lat1) * (lon3 - lon2)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def compare_coords(coord1, coord2):
    orientation_val = orientation(p0, coord1, coord2)
    if orientation_val == 0:
        return calculate_distance(p0, coord2) >= calculate_distance(p0, coord1)
    return orientation_val == 2

def sort_coords(coords):
    n = len(coords)
    if n <= 1:
        return coords
    min_coord = float('inf')
    min_index = -1
    for i in range(n):
        lat, lon = coords[i]
        if lon < min_coord or (lon == min_coord and lat < coords[min_index][0]):
            min_coord = lon
            min_index = i
    coords[0], coords[min_index] = coords[min_index], coords[0]
    global p0
    p0 = coords[0]
    coords[1:] = sorted(coords[1:], key=lambda coord: calculate_distance(p0, coord))
    sorted_coords = [coords[0]]
    i = 1
    while i < n:
        j = i + 1
        while j < n and orientation(p0, coords[i], coords[j]) == 0:
            j += 1
        sorted_coords.extend(sorted(coords[i:j], key=lambda coord: compare_coords(coord, coords[i-1])))
        i = j
    return sorted_coords

# Coordenadas desordenadas
lista_coordenadas = [
    [-28.58114994769431, -70.7474194285063],
    [-28.581006913205417, -70.7471809029528],
    [-28.581006913205417, -70.7471809029528],
    [-28.580842762646707, -70.74686853420152],
    [-28.580842762646707, -70.74686853420152],
    [-28.580676451950946, -70.74657584222197],
    [-28.580676451950946, -70.74657584222197],
    [-28.580518780528998, -70.74627577145303],
    [-28.580518780528998, -70.74627577145303],
    [-28.580451824100233, -70.74615525122617],
    [-28.580451824100233, -70.74615525122617],
    [-28.58039134728922, -70.74605194817455],
    [-28.58039134728922, -70.74605194817455],
    [-28.58027903311937, -70.74583058449255],
    [-28.58027903311937, -70.74583058449255],
    [-28.580091416494394, -70.74551593626781],
    [-28.580091416494394, -70.74551593626781],
    [-28.57899558301244, -70.74353367927436],
    [-28.57899558301244, -70.74353367927436],
    [-28.578922850297648, -70.74339563909375],
    [-28.578922850297648, -70.74339563909375],
    [-28.57695419901856, -70.73980107259719]
]

# Ordenar las coordenadas
coordenadas_ordenadas = sort_coords(lista_coordenadas)

# Imprimir las coordenadas ordenadas
for coordenada in coordenadas_ordenadas:
    print(coordenada)
