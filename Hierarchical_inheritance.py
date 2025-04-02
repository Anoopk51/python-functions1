class Human:
    def __init__(self,name,age):
        print('calling init from human class.')
        self.name=name
        self.age=age
    def showDetails(self):
        print(f'name:{self.name},age:{self.age}')
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self,m_name,age,location):
        print("calling init from Male class.")
        Human.__init__(self,m_name,age)
        self.location=location
    def sleep(self):
        print("I can sleep whole day.")
class Female(Human):
    def __init__(self,name,age,can_dance):
        print("calling from female class.")
        super().__init__(name,age)
        self.know_dancing=can_dance
    def showDetails_F(self):
        Human.showDetails(self)
        print(f'Know_dancing:{self.know_dancing}')
        # return super().showDetails()
    def work(self):
        print("I can code")
female_1=Female('Jiya',20,True)
female_1.showDetails_F()
print(female_1.name)
print(female_1.age)
# female_1.work()
# male_1=Male("Ram",'34','Delhi')
# print(Male.mro())

'''<----create one super class you can tak one person class take two attribute and two methode and person 
class driving student class and fecualty class and student and faculty class having ones atrribute and methode-----> '''