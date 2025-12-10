import matplotlib.pyplot as plt

student_names = ["Dmitrii", "Felix", "Oliver", "Jack", "Ella", "Isla", "Ellie"]
student_marks = [50, 45, 30, 40, 43, 20, 34]

marks_perc = []
for x in student_marks:
    res = (x / 50) * 100
    marks_perc.append(res)
print(marks_perc)

def marks_line_chart():
    plt.plot(student_names, student_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()
marks_line_chart()

def precentage_bar_chart():
    plt.bar(student_names, student_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()
precentage_bar_chart()