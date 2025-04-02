'''<-----------------x----------------------x--------------x------------------->'''
# class Human:
#     def __init__(self,num_heart):
#         self.eyes=2
#         self.heart=num_heart
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def sleep(self):
#         print("I can sleep whole day")
# class Boy(Male):
#     def work(self):
#         # Human.work(self)
#         super().work()
#         print("I can code")
# # class Programmer(Boy):
# #     def work(self):
# #         print('I can write programs.')
# #     # pass
# boy_1=Boy()
# # boy_1.eat()
# boy_1.work()
# # prog_1=Programmer()
# # prog_1.work()


'''<-----------------x----------------------x--------------x------------------->'''


class Human:
    can_breath=True
    def __init__(self,num_heart):
        print('calling init from Human class.')
        self.eyes=2
        self.heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self, name):
        print("calling init from Male class.")
        # super().__init__(num_heart)
        self.name=name
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    def __init__(self,heart,name,can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.know_dancing=can_dance
    def work(self):
        # Human.work(self)
        super().work()
        print('I can code')
boy_1=Boy(1,'Anoop',True)
print(boy_1.name)
print(boy_1.know_dancing)
print(boy_1.can_breath)
# print(Boy.mro())
