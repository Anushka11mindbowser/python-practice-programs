def check_obj(parameter1, parameter2):
    if parameter1 == parameter2:
        return True
    else:
        return False


print(check_obj([5, 8, 2, 6], [5, 8, 6, 2]))

a = "Hello World"
b = a
print(b)

print(check_obj(a, b))

lisa = (16, 'new york city', 'coffee', 'columbia', True)
martin = (18, 'conneticut', 'iced tea', 'yale', False)
print(check_obj(lisa, martin))

#Approach Two: Using is operator

def check_another(p1, p2):
    if p1 is p2:
        return True
    else:
        return False


print(check_another(lisa, martin))
