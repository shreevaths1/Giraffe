class Student:
    # initialization function
    def __init__(self, name, major, gpa, isOnProbation):
        self.name = name  # assigning parameter vals to attributes of object
        self.major = major
        self.gpa = gpa
        self.isOnProbation = isOnProbation

    def isOnHonorRoll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False
