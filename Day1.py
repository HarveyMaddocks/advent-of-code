import pandas as pd

with open("Data/Day1.txt") as f:
    data = f.readlines()

list1 = []
list2 = []

for row in data:
    items = row.strip().split()

    list1.append(int(items[0]))
    list2.append(int(items[1]))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

list_pairs = list(zip(sorted_list1, sorted_list2))

answer1 = sum(abs(x - y) for x, y in list_pairs)
print(answer1)

answer2 = 0
for i in list1:
    n = list2.count(i)
    n = i * n

    answer2 += n

print(answer2)

list1 = []
list2 = []

for row in data:
    items = row.strip().split()

    list1.append(int(items[0]))
    list2.append(int(items[1]))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

list_pairs = list(zip(sorted_list1, sorted_list2))

df = pd.DataFrame(list_pairs, columns=["List1", "List2"])

df["Diff"] = abs(df["List1"] - df["List2"])
print(df["Diff"].sum())


df["Occ"] = [len(df[df["List2"] == x]) for x in df["List1"]]
df["Occ-Val"] = df["Occ"] * df["List1"]
print(df["Occ-Val"].sum())