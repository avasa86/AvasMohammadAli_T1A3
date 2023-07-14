class Subjects:
    def __init__(self,SubjectName):
        self.SubjectName = SubjectName

    def __repr__(self)->str:
        return f"({self.SubjectName})"

class Students:
    def __init__(self,FirstName,LastName,Email,Age,PhoneNumber,ParentPhoneNumber,Subject,Mark):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Age = Age
        self.PhoneNumber = PhoneNumber
        self.ParentPhoneNumber = ParentPhoneNumber
        self.Subject = Subject
        self.Mark = Mark

    def __repr__(self)->str:
        return f"({self.FirstName},{self.LastName},{self.Email},{self.Age},{self.PhoneNumber},{self.ParentPhoneNumber},{self.Subject},{self.Mark})"
