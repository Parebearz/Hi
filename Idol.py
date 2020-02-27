#idol

def CEO():
    print("Facebook")
    
def Education():
    print("Ardsley High School, Phillips Exeter Academy, Harvard University")

def Birthday():
    print("May 14, 1984")
    
def Children():
    print("2")

def name():
    print("Mark Elliot Zuckerberg")
    
def age():
    print("36")
    
question = input("Pick one [name age Children Birthday Education CEO]")

if question == "name":
    name()
elif question == "age":
    age()
elif question == "Children":
    Children()
elif question == "Birthday":
    Birthday()
elif question == "Education":
    Education()
elif question == "CEO":
    CEO()
else :
    print("I know only 6 question")
