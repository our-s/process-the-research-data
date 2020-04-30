import collections
import csv
import matplotlib.pyplot as plt

with open('OD_2017.csv') as csvfile:
    locais = collections.defaultdict(
        lambda: collections.defaultdict(set))

    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        id = int(row['ID_PESS'])

        xy = []

        xy.append(row['CO_ESC_X'])
        xy.append(row['CO_ESC_Y'])
        xy.append(row['CO_TR1_X'])
        xy.append(row['CO_TR1_Y'])
        xy.append(row['CO_TR2_X'])
        xy.append(row['CO_TR2_Y'])
        xy.append(row['CO_O_X'])
        xy.append(row['CO_O_Y'])
        xy.append(row['CO_D_X'])
        xy.append(row['CO_D_Y'])
        xy.append(row['CO_T1_X'])
        xy.append(row['CO_T1_Y'])
        xy.append(row['CO_T2_X'])
        xy.append(row['CO_T2_Y'])
        xy.append(row['CO_T3_X'])
        xy.append(row['CO_T3_Y'])

        for i in range(0, len(xy) - 1):
            x = int(xy[i])
            y = int(xy[i+1])

            if x == 0 and y == 0: # invalid coordinates
                continue

            locais[x][y].add(id)

    data = []

    for i in sorted(locais):
        for j in sorted(locais[i]):
            data.append(len(locais[i][j]))
    
    data.sort(reverse=True)
    # for i in data:
    #     print(i)

    plt.hist(data, data[0]) # plotting a histogram
    plt.title('Histograma do Número de Pessoas - Locais')
    plt.xlabel('Nº de pessoas que frequentam (frequentadores)')
    plt.ylabel('Quantidade de lugares')
    plt.show()