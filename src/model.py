class Users:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __repr__(self)->str:
        return f"({self.username},{self.password})"

class Subjects:
    def __init__(self,SubjectName):
        self.SubjectName = SubjectName

    def __repr__(self)->str:
        return f"({self.SubjectName})"

class Students:
    def __init__(self,FirstName,LastName,Email,DateOfBirth,PhoneNumber,ParentPhoneNumber,Subject,Mark):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.DateOfBirth = DateOfBirth
        self.PhoneNumber = PhoneNumber
        self.ParentPhoneNumber = ParentPhoneNumber
        self.Subject = Subject
        self.Mark = Mark

    def __repr__(self)->str:
        return f"({self.FirstName},{self.LastName},{self.Email},{self.DateOfBirth},{self.PhoneNumber},{self.ParentPhoneNumber},{self.Subject},{self.Mark})"
