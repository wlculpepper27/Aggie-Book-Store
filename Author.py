#Weston Culpepper
#11/10/24
#Comp163-012
#Makes a class for Author, constructor and methods

#imports datetime package
from datetime import datetime

class Author:
# constructor
    def __init__(self, Fname, Lname, Mname, dob):
        self.Fname = Fname
        self.Lname = Lname
        self.Mname = Mname
        self.dob = dob

#getter and setter methods
    def getFname(self):
        return self.Fname

    def setFname(self, _Fname):
        self.Fname = _Fname

    def getLname(self):
        return self.Lname

    def setLname(self, _Lname):
        self.Lname = _Lname

    def getMname(self):
        return self.Mname

    def setMname(self, _Mname):
        self.Mname = _Mname

    def getDOB(self):
        return self.dob

    def setDOB(self, _DOB):
        self.dob = _DOB

    def getAge(self):
        if isinstance(self.dob, str):
            dob_date = datetime.strptime(self.dob, "%Y-%m-%d").date()
        elif isinstance(self.dob, datetime):
            dob_date = self.dob.date()
        else:
            raise ValueError("Date of Birth must be a string in 'YYYY-MM-DD' format or a datetime object.")

        today = datetime.now().date()
        age = today.year - dob_date.year
        if (today.month, today.day) < (dob_date.month, dob_date.day):
            age -= 1
        return age

    def getName(self):
        name = self.Fname + ' ' + self.Mname + ' ' + self.Lname
        return name
