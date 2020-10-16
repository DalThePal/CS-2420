'''courselist.py'''
from recursioncounter import RecursionCounter

class CourseList:
    '''CourseList'''

    def __init__(self):
        '''init'''
        self.head = None

    def insert(self, course):
        '''inserts an instance of Course in course number ascending order'''
        if self.head is None:
            self.head = course

        elif course.number() < self.head.number():
            course.next = self.head
            self.head = course

        else:
            self.head = self.__insert_helper(self.head, course)

    def __insert_helper(self, cursor, course):
        '''recursion for insert method'''
        RecursionCounter()

        if cursor is None:
            return course

        if course.number() < cursor.number():
            course.next = cursor
            return course

        cursor.next = self.__insert_helper(cursor.next, course)
        return cursor

    def remove(self, number):
        '''removes the first occurrence of the specified course'''
        return self.__remove_helper(self.head, number)

    def __remove_helper(self, cursor, number):
        '''recursion for remove'''
        RecursionCounter()

        if cursor is None:
            return

        if cursor.number() == number:
            self.head = cursor
            return

        if cursor.next.number() == number:
            cursor.next = cursor.next.next
            return

        return self.__remove_helper(cursor.next, number)

    def remove_all(self, number):
        '''removes all instances of a course'''
        return self.__remove_all_helper(self.head, number)

    def __remove_all_helper(self, cursor, number):
        '''recursion for remove_all'''
        RecursionCounter()

        if cursor is None:
            return

        if cursor.number() == number:
            self.remove(number)

        return self.__remove_all_helper(cursor.next, number)

    def find(self, number):
        '''find the first occurrance of the specified course in the list or return -1'''
        return self.__find_helper(self.head, number)

    def __find_helper(self, cursor, number):
        '''recursion for find'''
        RecursionCounter()

        if cursor is None:
            return -1

        if cursor.number() is number:
            return cursor

        return self.__find_helper(cursor.next, number)

    def size(self):
        '''return the number of items in the list'''
        return self.__size_helper(self.head)

    def __size_helper(self, cursor):
        '''recursion for size'''
        RecursionCounter()

        if cursor is None:
            return 0

        return 1 + self.__size_helper(cursor.next)

    def calculate_gpa(self):
        '''return the GPA using all courses in the list'''

        total_grade_points = self.__total_grade_points(self.head)
        total_credits = self.__total_credits(self.head)

        if self.head is None:
            return 0.0

        return total_grade_points / total_credits

    def __total_grade_points(self, cursor):
        '''recursion for calculate_gpa'''
        RecursionCounter()

        if cursor is None:
            return 0.0

        return (cursor.grade() * cursor.credit_hr()) + self.__total_grade_points(cursor.next)

    def __total_credits(self, cursor):
        '''recursion for calculate_gpa'''
        RecursionCounter()

        if cursor is None:
            return 0.0

        return cursor.credit_hr() + self.__total_credits(cursor.next)

    def is_sorted(self):
        '''return True if the list is sorted by Course Number, False otherwise'''
        return self.__is_sorted_helper(self.head)

    def __is_sorted_helper(self, cursor):
        '''recursion for is_sorted'''
        RecursionCounter()

        if cursor is None or cursor.next is None:
            return True
        if cursor.number() > cursor.next.number():
            return False
        return self.__is_sorted_helper(cursor.next)

    def __str__(self):
        '''returns a string with each Course’s data on a separate line'''
        return f'Current List: ({self.size()})\n' + self.__str_helper(self.head)

    def __str_helper(self, cursor):
        RecursionCounter()
        if cursor is None:
            return "\n\n\nCumulative GPA: " + str(self.calculate_gpa())

        return str(cursor) + '\n' + self.__str_helper(cursor.next)


    def __iter__(self):
        '''iterate through the list'''
        self.cursor = self.head
        return self

    def __next__(self):
        '''returns the next value'''
        if self.cursor is None:
            raise StopIteration
        else:
            course = self.cursor
            self.cursor = self.cursor.next
        return course
