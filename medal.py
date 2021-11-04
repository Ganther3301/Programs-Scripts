num = int(input("Enter number of countries: "))
countries = {} 
medals = []
highest = 0
lowest = 0
for i in range(num):
    count = input("Enter country: ")
    medal = int(input("Enter number of medals: "))
    countries[medal] = count
    medals.append(medal)
medals.sort(reverse=True)

for i in medals:
    print(countries[i],":",i)