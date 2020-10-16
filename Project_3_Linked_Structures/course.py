'''Course.py'''

class Course:
    def __init__(self, number=0, name="", credit_hr=0.0, grade=0.0):
        '''init'''

        if not isinstance(number, int):
            raise ValueError("invalid number")
        if number < 0:
            raise ValueError("invalid number")
        self._number = number

        if not isinstance(name, str):
            raise ValueError("invalid name")
        self._name = name

        if not isinstance(credit_hr, float):
            raise ValueError("invalid credit hours")
        if credit_hr < 0:
            raise ValueError("invalid credit hours")
        self._credit_hr = credit_hr

        if not isinstance(grade, float):
            raise ValueError("invalid grade")
        if grade < 0:
            raise ValueError("invalid grade")
        self._grade = grade

        self.next = None

    def number(self):
        '''get course number'''
        return self._number

    def name(self):
        '''get course name'''
        return self._name

    def credit_hr(self):
        '''get course credit hours'''
        return self._credit_hr

    def grade(self):
        '''get course grade'''
        return self._grade

    def __str__(self):
        '''get course as string'''
        return f'cs{self._number} {self._name} Grade:{self._grade} Credit Hours: {self._credit_hr}'
