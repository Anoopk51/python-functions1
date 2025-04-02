'''<----------------x---------------------x-----------------------x---------------------------x----------------->'''
# class Circle:
#     def __init__(self,radius):
#         self.pi=3.141
#         self.radius=radius
#     def Circumference(self):
#         return 2*self.pi*self.radius
#     def Area(self):
#         return self.pi*(self.radius)**2
# circle_1=Circle(float(input("Enter the radius of circle:")))
# print(f'The circumference of circle is{circle_1.Circumference()}')
# print(f'The area of circle is {circle_1.Area()}')


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''

# class Circle:
#     pi=3.141
#     def __init__(self,radius):
#         self.radius=radius
#         self.area=Circle.pi*(radius**2)
#     def Circumference(self):
#         return 2*Circle.pi*self.radius
# circle_1=Circle(float(input('Enter the radius of circle is:')))
# print(f'The circumference of circle is {circle_1.Circumference()}')
# print(f'The area of circle is {circle_1.area}')


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''


# class Human:
#     def eat(self):
#         print('I can eat')
#     def work(self):
#         print('I can work')
# class male:
#     def eat(self):
#         print('I can eat')
#     def work(self):
#         print('I can work')
# man_1=male()
# man_1.eat()
# man_1.work()


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''

# class Human:
#     def eat(self):
#         print('I can eat.')
#     def work(self):
#         print('I can work.')     
# class male(Human):
#     pass
# man_1=male()
'''man_1.eat()
man_1.work()''' # isko print function me likh  diya jaye to 
# print(f'Your result is-{man_1.eat(),man_1.work()}') # Yai result to print hoga lakin print wale function me None likha aayega
# kyuki usme retrun nahi ho rha hai.
'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''

# class Human:
#     def eat(self):
#         return 'I can eat'
#     def work(self):
#         return 'I can work'
# class male(Human):
#     pass
# man_1=male()
# # man_1.eat()
# # man_1.work()
# print(f'Your result is-\n {man_1.eat()} \n {man_1.work()}.')


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''


# class Human:
#     # def __init__(self,name):
#     #     self.name=name
#     def eat(self):
#         print('I can eat!')
#     def work(self):
#         print('I can work!')
# class male(Human):
#     def flirt(self):
#         print('I can flirt')
# man_1=male()
# man_1.flirt()
# man_1.eat()
# man_1.work()


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''


# class Human:
#     def eat(self):
#         return 'I can eat!'
#     def work(self):
#         return 'I can work!'
# class male(Human):
#     def flirt(self):
#         return 'I can flirt!'
# man_1=male()
# print(f'{man_1.eat()}\n{man_1.work()}\n{man_1.flirt()}')


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''   

# class Human:
#     def eat(self):
#         return 'I can eat!'
#     def work(self):
#         return 'I can work!'
# class male(Human):
#     def flirt(self):
#         return 'I can flirt!'
# man_1=male()
# man_1.eat()
# man_1.work()
# man_1.flirt()
# print(f'{man_1.eat()}\n{man_1.work()}\n{man_1.flirt()}')


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''  

# class Human:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         return 'I can eat!'
#     def work(self):
#         return 'I can work!'
# class male(Human):
#     def flirt(self):
#         return 'I can flirt!'
# man_1=male('Anoop')
# print(f'{man_1.eat()}\n{man_1.work()}\n{man_1.flirt()}')
# print(man_1.name)


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''  

# class Human:
#     def eat(self):
#         return 'I can eat!'
#     def work(self):
#         return 'I can work!'
# class male(Human):
#     def work(self):
#         return 'I can code'
#     def flirt(self):
#         return 'I can flirt!'
# man_1=male()
# print(f'{man_1.eat()}\n{man_1.work()}\n{man_1.flirt()}')
# print(man_1.name)

'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''  

# class Human:
#     def eat(self):
#         return 'I can eat!'
#     def work(self):
#         # return 'I can work!'
#         print('I can work!')
# class male(Human):
#     def work(self):
#         super().work()
#         # return 'I can code'
#         print('I can code')
#     def flirt(self):
#         return 'I can flirt!'
# man_1=male()
# man_1.work()
# # print(f'{man_1.eat()}\n{man_1.work()}\n{man_1.flirt()}')


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''  
# class Human:
#     def eat(self):
#         print('I can eat!')
#     def work(self):
#         print('I can work!')
# class male(Human):
#     def work(self):
#         super().work()
#         print('I can code!')
#     def flirt(self):
#         print('I can flirt!')
# man_1=male()
# man_1.work()


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''  

# class Human:
#     def __init__(self,name,age,date ):
#         self.name=name
#         self.age=age
#         self.date=date
#         # pass
#     def eat(self):
#         print('I can eat!')
#     def work(self):
#         print('I can work!')
# class male(Human):
#     def work(self):
#         super().work()
#         print('I can code!')
#     def flirt(self):
#         print('I can flirt!')
# man_1=male('Anoop',20,'07February2025')
# # man_1.work()
# # print(man_1.name)
# # print(man_1.age)
# # print(man_1.dob)
# # print(f'My name is {man_1.name} \n and my age is {man_1.age} \n Today date {man_1.dob}')
# print(man_1.name,man_1.age,man_1.date)


'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''  
# class Human:
#     def __init__(self,num_heart):
#         self.num_eyes=2
#         self.num_nose=1
#         self.num_heart=num_heart
#     def eat(self):
#         print('I can eat!')
#     def work(self):
#         print('I can work!')
# class Male(Human):
#     def __init__(self,name,heart):
#         super().__init__(heart)
#         self.name=name
#     def flirt(self):
#         print('I can flirt')
#     def work(self):
#         super().work()
#         print('I can code')
#     # def display(self):
#         # print(f'Hi , I am {self.name} and I have {self.num_eyea}')
# male_1=Male('Anoop',1)
# print(male_1.name)
# print(male_1.num_heart)
# male_1.work()
# # print(male_1.num_eyes)
# # print(male_1.num_nose)


'''<--------------x---------------------x--------------------x---------------------------x---------------------->''' 

# class Human:
#     def __init__(self,num_heart):
#         self.num_eye=2
#         self.num_nose=1
#         self.num_heart=1
#     def eat(self):
#         print('I can eat!')
#     def work(self):
#         print('I can work! and')
#         # return 'I can work! and'
# class male(Human):
#     def __init__(self,name, num_heart):
#         super().__init__(num_heart)
#         self.name=name
#     def flirt(self):
#         print('I can flirt!')
#     def work(self):
#         super().work()
#         # print('I can code!')
#         return 'I can code!'
#     def display(self):
#         print(f'My name is {mode_1.name} and in body haveing {mode_1.num_heart} heart , {mode_1.num_nose} nose and {mode_1.num_eye} eye. and {mode_1.work()}')
#         # return f'My name is {mode_1.name} and in body haveing {mode_1.num_heart} heart , {mode_1.num_nose} nose and {mode_1.num_eye} eye. and {mode_1.work()}'
#     # display(mode_1)
# mode_1=male('Anoop',1)
# mode_1.display()
    
'''<--------------x---------------------x--------------------x---------------------------x---------------------->''' 
# class Human:
#     # def __init__(self,name):
#     #     self.name=name
#     def eat(self):
#         print('I can eat!')
#     def work(self):
#         print('I can work!')
# class male:
#     def flirt(self):
#         print('I can flirt')
#     def work(self):
#         print('I can code!')
# class Boy(Human,male):
#     pass
# boy_1=Boy()
# boy_1.work()

'''<--------------x---------------------x--------------------x---------------------------x---------------------->''' 
# class Human:
#     def __init__(self):
#         print('calling init from Human')
#         self.num_eye=2
#         self.num_nose=1
#     def eat(self):
#         print('I can eat!')
#     def work(self):
#         print('I can work!')
# class male:
#     def __init__(self,name):
#         print("calling init from male")
#         self.name=name
#     def flirt(self):
#         print('I can flirt')
#     def work(self):
#         print('I can code!')
# class Boy(Human,male):
#     def __init__(self,name):
#         Human.__init__(self)
#         male.__init__(self,name)
    
#     def sleep(self):
#         print("I can sleep")
#     def work(self):
#         print('I can test')
#     pass
# # boy_1=Boy('Durgesh')
# # boy_1.work()
# print(Boy.mro())
# # print(boy_1.name)

'''<--------------x---------------------x--------------------x---------------------------x---------------------->'''

class Human:
    def __init__(self,num_heart):
        print('calling init from Human')
        self.num_eye=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print('I can eat!')
    def work(self):
        print('I can work!')
class male:
    def __init__(self,name):
        print("calling init from male")
        self.name=name
    def flirt(self):
        print('I can flirt')
    def work(self):
        print('I can code!')
class Boy(Human,male):
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        male.__init__(self,name)
        self.langauge=language
    
    def sleep(self):
        print("I can sleep")
    def work(self):
        print('I can test')
    def display(self):
        print(f'Hi i am {boy_1.name} and I work on {boy_1.langauge}')
boy_1=Boy('Anoop',1,'Python')
# boy_1.work()
print(Boy.mro())
# print(boy_1.num_nose)
# print(boy_1.name)
# print(boy_1.num_heart)
# print(boy_1.langauge)
boy_1.display()
'''Assingment is pass display methode and coll and print-->i am  and i work on language'''