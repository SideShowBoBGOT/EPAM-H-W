# import random
# with open('students.csv', 'w') as file:
#     with open('names.txt') as f:
#         for line in f:
#             l = line[:-1] +','+str(random.randint(17, 30))+','+str(float(random.randint(100,1000))/100.0)+'\n'
#             file.write(l)

def get_top_performers(file_path, number_of_top_students) -> list:
    """
    Function which receives file path and returns names of top performer students
    @param file_path: file of students
    @param number_of_top_students: number of top students to be returned
    @return: list of students
    """
    if not isinstance(file_path, str) or not isinstance(number_of_top_students, int):
        raise TypeError
    if number_of_top_students <= 0:
        raise ValueError
    students = []
    with open(file_path) as file:
        for line in file:
            students.append(tuple(line.split(',')))
    students.sort(key=lambda x: x[2], reverse=True)
    if number_of_top_students < len(students):
        return list(map(lambda x: x[0], students[:number_of_top_students]))
    return list(map(lambda x: x[0], students))


def write_students_age_desc(file_path, output_file) -> None:
    """
    Function which receives the file path with students info and writes
    CSV student information to the new file in descending order of age.
    @param file_path: file of students
    @param output_file: file of sorted students
    @return: None
    """
    if not isinstance(file_path, str) or not isinstance(output_file, str):
        raise TypeError
    students = []
    with open(file_path) as file:
        for line in file:
            students.append(tuple(line.split(',')))
    students.sort(key=lambda x: x[1], reverse=True)
    with open(output_file, 'w') as file:
        for student in students:
            line = ','.join(student)
            file.write(line)
    return None


print((get_top_performers('students.csv', 4)))
write_students_age_desc('students.csv', 'sorted_students.csv')
