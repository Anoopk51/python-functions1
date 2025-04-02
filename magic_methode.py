# list1=[1,0,-1] #if needs to findout len of list then use bulidin opration.
# print(len(list1))
# print(list1)
# print(type(list1))

'''If we want to use user defind object then use Dunder methode.'''
# class Demo:
#     name='jenny'
# d=Demo()
# # print(len(d))
# print(d)


# print(8+9)
# print(dir(int))
class Author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    def __len__(self):
        return self.pages
    def __call__(self,*args,**kwargs):
        print("Hi")
    # def __del__(self):
    #     print("Author object has been deleted.")
d=Author('Jenny','Python Basic to Advance',300)
# print(d)
print(str(d))
'''So we have dunder methode. __str__'''
# and __str__ was return string version of any methode.
# print(len(d))
d()
del d  # thise is del methode.
print(d)