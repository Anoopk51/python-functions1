'''<---------------Methode Overloading-------------------->'''

# class Demo:
#     def add(self,a,b):
#         return a+b
    
# d=Demo()
# print(d.add(2,3))  


'''But in methode overloading'''

# class Demo:
#     def add(self,a,b):
#         return a+b
    
#     def add(self,a,b,c):
#         return a+b+c
    
# d=Demo()
# print(d.add(2,3))  
# print(d.add(1,2,3)) # TypeError: Demo.add() missing 1 required positional argument: 'c' this is colled methode overloading.
                    # Because error come from print(d.add(2,3)) lines and but class perfom is same name in class methode then
                    # take letest methode so in this program class take last methode means three parameter methode.
'''So now inprove this error using 1.default methode.'''

# class Demo:
#     def add(self,a,b,c=0):
#         return a+b+c
    
    
# d=Demo()
# print(d.add(2,3))  
# print(d.add(1,2,3))

'''2nd methode means using *args'''


# class Demo:
#     def add(self,*args): #this *args means variable length argument.means any number of argument you can pass essily.
#         total=0
#         for i in args:
#             total=total+i
#         return total
    
    
# d=Demo()
# print(d.add(2,3))  
# print(d.add(1,2,3))
# print(d.add(3,4,5,67,7,8))


'''<-----------------M'''
# class Father:
#     def sleep(self):
#         print("Sleeps from 10:00 pm to 5:00 AM")
#     def eat(self):
#         print("eating")
# class Son(Father):
#     pass
# Ram=Son()
# Ram.sleep()


class Father:
    def sleep(self):
        print("Sleeps from 10:00 pm to 5:00 AM")
    def eat(self):
        print("eating")
class Son(Father):
    def sleep(self):
        # return super().sleep()
        print("sleep from 2:00 AM to 10:00 AM")
        super().sleep() #Super is methode overriding
Ram=Son()
Ram.sleep()
# methode overloading is complie time polymorphical and overrriding is run time polymorphism