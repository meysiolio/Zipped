StudentNum, SubjectNum = map(int, input().split())
Grades = []

for _ in range(SubjectNum):
    Grades.append(list(map(float,input().split())))
    
for i in list(zip(*Grades)):
    print(sum(i)/SubjectNum)