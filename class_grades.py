from typing import Type
import numpy as np

def weighted_average(weights, grades):
    """ computes the weighted average of grades"""

    try:
        tot_grade = 0
        for grade_type in grades.keys():
            tot_grade += np.mean(grades[grade_type]) * weights[grade_type]
        return tot_grade
    except TypeError:
        # While Python3.6+ dictionaries are ordered, allowing it can introduce
        # subtle computational bugs in computation if an unordered dictionary is entered
        # So we disquality the input by casting to numpy arrays

        weights = np.array(weights)

        #This supports both points earned, points possible and points earned formats
        grades = np.array(grades)
        if (len(grades.shape) == 2):
            if (grades.shape[0] == 1 or grades.shape[1] == 1):
                pass
            else:
                assert(grades.shape[1] == 2)
                np.mean()
            
        return np.sum(weights*grades)

class GradeEntry:
    
    """ 
    Supports a number of different types of grade entries:
    1. grade type, float
    2. points earned, points possible
    3. points earned
    """



class ClassGrades:

    """ Stores grades for a class """

    def __init__(self, grade_func=weighted_average, weighting=None, grades=None):
        self._grades = grades               #maps type of grade to a list of grades
        self._weighting = weighting         #maps type of grade to it's weight in the total grade calculation
        self._tot                           #total grade
        self._grade_func = grade_func       #function to calculate total grade


    def add_grade(self, grade):
        """
        Adds a grade entry to the store of grades 

        If grade is a tuple and grades is a hashmap, 
        Parameters:
            grade: Tuple (grade type, grade) or value 
        """
        try:
            grade_type, grade_val = grade[0], grade[1]
            if grade_type not in self._grades:
                self._grades[grade_type] = []

            self._grades[grade_type].append(grade_val)
        except (IndexError, TypeError):
            self._grades.append(grade)


