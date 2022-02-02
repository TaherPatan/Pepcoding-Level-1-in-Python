def student_marks(student_mark):
    if student_mark > 90:
        print('excellent')
    elif student_mark > 80:
        print('good')
    elif student_mark > 70:
        print('fair')
    elif student_mark > 60:
        print('meets expectations')
    else:
        print('below par')


marks = int(input())
student_marks(marks)
