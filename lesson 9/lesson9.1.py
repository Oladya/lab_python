import csv


# sberbank.py


def money_reader(cat, exclude_region, year):
        f = open('opendata.csv', encoding='cp1251')
        reader = csv.reader(f, delimiter=',')

        d = {}
        

        for row in reader:
                # row[0] - cat
                # row[1] - region
                # row[2] - yyyy-mm-dd
                # row[3] - value

                b = row[2].split("-")
                if row[0] == cat and row[1] != exclude_region and int(b[0]) == year:
                        #print (row)
                        if row[1] in d:
                                d[row[1]] += int(row[3])
                        else:
                                d[row[1]] = int(row[3])


        print(d)
        max_value = 0
        max_region = ""
        
        for i in d:        
                if d[i] > max_value:
                        max_value = d[i]
                        max_region = i
                 
        print(max_value, max_region)

if __name__ == '__main__':
        money_reader("Количество заявок на потребительские кредиты", "Россия", 2017)

 
