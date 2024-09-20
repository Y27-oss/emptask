emp = {'eno':[1,2,3],'ename':['A','B','C'],'esal':[1000,2000,3000]}
print("\n the employee database: is:")
print(emp)
print("-------------------------------------------------------")
print("\n The Employee name are:", emp['ename'])
print("-----------------------------------------------------")
print("\n The employee salaries are :")
print("-----------------------------------------------")
for i in emp['esal']:
    print(i)