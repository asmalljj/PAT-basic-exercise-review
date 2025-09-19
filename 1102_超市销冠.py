N = int(input())
List = []

for i in range(N):
    line = input().split()
    Id = line[0]
    price, count = map(int, line[1:])
    total = price * count
    List.append([Id, price, count, total])

sales_champion = max(List, key = lambda x: x[2])
print(sales_champion[0], sales_champion[2])

total_champion = max(List, key = lambda x: x[3])
print(total_champion[0], total_champion[3])

