import re

def rename_class(cls, new_name):
    if re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        cls.__name__ = new_name
    else:
        raise ValueError("Невірне ім'я класу: ім'я повинно починатися з великої літери і містити тільки літери та цифри.")

class MyClass:
    pass

rename_class(MyClass, "UsefulClass")
print(MyClass.__name__)  

rename_class(MyClass, "SecondUsefulClass")
print(MyClass.__name__) 

try:
    rename_class(MyClass, "secondUsefulClass")
except ValueError as e:
    print(e)

try:
    rename_class(MyClass, "Invalid_Class_Name!") 
except ValueError as e:
    print(e)

