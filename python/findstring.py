def ispresent(person):
    names = ["AL", "PK", "JN"]
    if person in names:
        return True
    else:
        return False

def nodigit(person):
    if person.isalpha(): #ISALPHA() RETURNS TRUE IF ALL CHARACTERS ARE ALPHABET LETTERS
        return True
    else:
        return False

