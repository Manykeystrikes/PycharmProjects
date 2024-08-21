'''Problem: A primary school needs to arrange their students to sit for the National Assessment Program −
Literacy and Numeracy test in multiple exam halls at Griffith University. Each school class has 25
students. A big exam hall can accommodate 45 students, and a small exam hall can accommodate 22
students. Write a program for the school to calculate how many full classes can be accommodated given
the input numbers of the number of big exam halls and small exam halls. For example, the output should
look like this when the program is run:
How many big exam halls? 10
How many small exam halls? 20
Number of classes = 35
Testing: Test your program by checking the output for the following two scenarios:
 Number of big exam halls: 15; Number of small exam halls: 10
 Number of big exam halls: 5; Number of small exam halls: 25
Can you change the output above and present it in a table format?'''

class_size = int(25)
big_hall_setting = int(45)
small_hall_setting = int(22)

big_exam_halls = int(input("How many big exam halls?: ",))
small_exam_halls = int(input("How many small exam halls?: ",))
number_of_classes = int(input("Number of classes?: ",))


#hall_setting_comparsion = (big_hall_setting / class_size)
#small_setting_comparsion = (small_hall_setting / class_size)

number_of_big_seats = int(big_exam_halls * big_hall_setting)
number_of_small_seats = int(small_exam_halls * small_hall_setting)
total_available_seats = int(number_of_big_seats + number_of_small_seats)

number_of_students = int(class_size * number_of_classes)


fullness = float(number_of_students/total_available_seats)
print(f'the halls are {fullness*100:.2f}% full.')



#data= {'Name': ['big_hall_setting', 'small_hall_setting',]:
  # 'Big_Hall': [big_hall_setting / class_size,],
   #'Small_Hall': [small_hall_setting / class_size]}

