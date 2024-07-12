
grades_ = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Aaron_ = ((5 + 3 + 3 + 5 + 4)/5)
#print(Aaron_)
#Bilbo_ = ((2 + 2 + 2 + 3)/4)
#print(Bilbo_)
#Johnny_ = ((4 + 5 + 5 + 2)/4)
#print(Johnny_)
#Khendrik_ = ((4 + 4 + 3)/3)
#print(Khendrik_)
#Steve_ = ((5 + 5 + 5 + 4 + 5)/5)
#print(Steve_)
#middle_grades = {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
#print(middle_grades)
#middle_grades={'Aaron':(5+3+3+5+4)/5,'Bilbo':(2+2+2+3)/4,'johnny':(4+5+5+2)/4,'Khendrik':(4+4+3)/3,'Steve':(5+5+5+4+5)/5}
#print(middle_grades)

#print(grades_[0])
#print(len(grades_[0]))
#print(sum(grades_[0]))
#print(sum(grades_[0])/len(grades_[0]))

middle_1 = (sum(grades_[0])/len(grades_[0]))
middle_2 = (sum(grades_[1])/len(grades_[1]))
middle_3 = (sum(grades_[2])/len(grades_[2]))
middle_4 = (sum(grades_[3])/len(grades_[3]))
middle_5 = (sum(grades_[4])/len(grades_[4]))
middle_grades = {'Aaron': middle_1, 'Bilbo': middle_2, 'Johnny': middle_3, 'Khendrik': middle_4, 'Steve': middle_5}
print(middle_grades)