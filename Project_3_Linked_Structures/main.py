'''main.py'''
from course import Course
from courselist import CourseList

def create_linked_list():
    '''reads from text file and creates linked list'''

    course_list = CourseList()

    file = open('data.txt', 'r')

    for line in file:
        line = line.rstrip()
        data = line.split(',')
        course = Course(int(data[0]), data[1], float(data[2]), float(data[3]))
        course_list.insert(course)

    return course_list



def main():
    '''main'''
    cl = create_linked_list()
    print(cl)

    return str(cl)

if __name__ == '__main__':
    main()
