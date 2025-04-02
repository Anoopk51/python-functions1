class Human:
    def __init__(self):
        print('calling init from Human')
        self.num_eye=2
        self.num_nose=1
    def eat(self):
        print('I can eat')
    def work(self):
        print("I can work")
class Male:
    def __init__(self,name):
        print('calling init from Male')
        self.name=name
    def flirt(self):
       print("I can flirst")
    def work(self):
        print("I can code")
class Boy(Human,Male): # Parameter position change karne par MRO position change ho ja rha hai.
# class Boy(Male,Human): 
    def __init__(self,name):
        Human.__init__(self)
        Male.__init__(self,name) 

    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")
boy_1=Boy('Rahul')
# boy_1.flirt()
# boy_1.work()
# print(Boy.mro())
# # Male.work(boy_1) # methode  male  work wale ke liye work hoga.
# print(boy_1.name)
print(boy_1.num_nose)