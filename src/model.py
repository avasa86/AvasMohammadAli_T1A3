class Subject:
    def __init__(self,SubjectName):
        self.SubjectName = SubjectName

    def __repr__(self)->str:
        return f"({self.SubjectName})"

class Student:
    def __init__(self,FirstName,LastName,Email,Age,PhoneNumber,ParentPhoneNumber,Mark,Subject):
        self.first_name = FirstName
        self.last_name = LastName
        self.email = Email
        self.age = Age
        self.phone_number = PhoneNumber
        self.parents_phone_number = ParentPhoneNumber
        self.subject_id = Subject
        self.mark = Mark

    def __repr__(self)->str:
        return f"{self.first_name},{self.last_name},{self.email},{self.age},{self.phone_number},{self.parents_phone_number},{self.mark},{self.subject_id}))"
