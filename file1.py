file=open("city.txt","r")
city_data=[]
for i in range(5):
    city=file.readline().split()
    city_data.append(city)
print("Details of all Cities:")
for i in city_data:
    for j in i:
        print(f"{j}\t",end=" ")
    print()
print("\nDetails of cities having population more than 10 Lakh: ",end=" ")
area_sum=0
for i in city_data:
    if float(i[1])>10:
        print(f"{i[0]}\t{i[1]}\t{i[2]}",end=" ")
        area_sum+=float(i[2])
    print()
print(f"\nSum of Areas of all cities: {area_sum}")
file.close()