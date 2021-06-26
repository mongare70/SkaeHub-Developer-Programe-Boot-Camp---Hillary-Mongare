# list of dictionaries
student_one = {
    "name"   : "Hillary",
    "age"    : 23,
    "height" : 5.8
}

student_two = {
    "name"   : "Lydia",
    "age"    : 20,
    "height" : 5.4
}

student_three = {
    "name"   : "Kihara",
    "age"    : 24,
    "height" : 5.6
}


students = [student_one, student_two, student_three]

# sort students according to age in ascending order
sorted_students = sorted(students, key=lambda x:x['age'], reverse=False)

print(sorted_students)