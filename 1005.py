# n1 = int(input("請輸入數字:"))
# n2 = 1

# fac = []

# for i in range(2,n1):
#     if n1 % i == 0:
#         fac.append(i)
#         continue
#     else:
#         pass

# if len(fac) == 0:
#     print("Prime number")
# else:
#     print(fac)

Class_1 = ['B177793449','A134689794','G130949062','K147378503'
,'B200674844','B163671690','B205054646','E231081836','D219055993','D183361919'
,'X161067471','B281840622','B153971781','N151829346','B283079309']

Taichung_people = []
Taichung_man = []
Taichung_woman = []

for i in range(0,15):
    str = Class_1[i]
    if str[0:1] == "B":
        Taichung_people.append(Class_1[i])
        
        if str[1:2] == "1":
            Taichung_man.append(Class_1[i])
        elif str[1:2] == "2":
            Taichung_woman.append(Class_1[i])

print(Taichung_people)
print(Taichung_man)
print(Taichung_woman)