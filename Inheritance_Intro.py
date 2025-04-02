# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")

# # class Male:
# class Male(Human):
    
#     # def eat(self):
#     #     print("I can eat")        '''ye sub to above class me hi hai to hum usko inheritence ker lenge.'''
#     # def work(self):
#     #     print("I can work")
#     def flirt(self):
#         print("I can flirt")

# male_1=Male()
# male_1.eat()


'''<-------x---------------x------------x-------->'''

# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def flirt(self):
#         print("I can flirt")
    

# male_1=Male()
# male_1.flirt()
# male_1.work()



'''<-------------x-----------------x------------x------------>'''
# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def flirt(self):
#         print("I can flirt")
#     def work(self):
#         print("I can code")

# male_1=Male()
# male_1.flirt()
# male_1.work() ### Overriding


'''<------x------------------------x--------------x-------->'''

# class Human:

#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def flirt(self):
#         print("I can flirt")
#     def work(self):
#         super().work()
#         print("I can code")

# male_1=Male()
# male_1.flirt()
# male_1.work() ### Overriding

'''<---------x------------x------------------x---------------->'''
class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart # iske liye parater pass karna padeya nahi  to error aayega
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")
    # def display(self):
        # print(f'Hi, I am {self.name} and I have {self.num_heart} heart.')
male_1=Male("Anoop",1)
# male_1=Male()
# male_1.flirt()
# male_1.work() ### Overriding
# print(male_1.num_eyes)
# print(male_1.num_nose)
print(male_1.name)
print(male_1.num_heart)
# male_1.display()