import collections
import csv

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

    for i in sorted(locais):
        for j in sorted(locais[i]):
            print(str(i) + ', ' + str(j) + ': ' + str(len(locais[i][j])))
