# *args and **kwargs in Functions
# Here we are exploring the differences between *args and *kwargs 
# Credit goes to Medium Article

# *args allow our function to take in any number of positional arguments, which will be stored in the tuple args.

def myFunction(a, b, *args):
    print(f"{a=} {b=} {args=}")
    #print(f"{a} {b} {args}")

myFunction(1,2,3,4,5,6,7,8,9,10)

# **kwargs allow our function to take in any number of keyword arguments , which will be stored in the dict kwargs.

def myFunction1(a , b , **kwargs):
    print(f"{a=} {b=} {kwargs=}")

#It only acce
myFunction1(a=1,b=2,c=3,d=4,e=5)