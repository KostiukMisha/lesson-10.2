class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def creation():
    return [Man(), Woman()]

adam_and_eve = creation()
print(type(adam_and_eve[0]))  
print(type(adam_and_eve[1]))  
