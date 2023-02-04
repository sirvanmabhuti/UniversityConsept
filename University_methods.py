class University:
    person = 0
    def __init__(self,name,age,bool(certificate)):
        self.name = name
        self.age = age
        self.certificate = certificate
        person += 1
    def __del__(self):
        person -= 1

class Student(University):
    if self.certificate == 'diplom':
        pass
    else:
        return 'be dalile nabood madrak kafi shoma hagh sabt nam nadarid'

class Perfossor(University):
    if self.certificate == 'fogh':
        pass
    else:
        return 'be dalile nabood madrak kafi shoma hagh tadris nadarid'