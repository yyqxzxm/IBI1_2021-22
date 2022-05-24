#I looked up a lot of knowledge about class on the Internet and sought the help of Zuo Jingyi. The following is the most concise version in my opinion
#creat a class
class Staff:
    def __init__(self,firstname,lastname,location,role):
        self.f_name=firstname
        self.l_name=lastname
        self.l=location
        self.r=role

    def ZJEinformation(self):
        print("name:",self.f_name,self.l_name, "location:",self.l, "role:",self.r)
#the example(Caitriana Nicholson, International Campus, faculty)
#(Robert Holmes, International Campus, faculty)
Staff1 = Staff("Caitriana","Nicholson","International Campus","faculty")
Staff1.ZJEinformation()

Staff2 = Staff("Robert","Holmes","International Campus","faculty")
Staff2.ZJEinformation()
