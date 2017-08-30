# This program says hello and greets a person by name.
#
# Your Name
# August 24, 2017

print("Hello.")
print("What is your name?")
name = input()

print("It is good to meet you, " + name + ".")
print("How are you today?")
mood = input()
if "sad" in mood:
    print("Aw thats sad to hear. Um.....")
elif "good" in mood:
    print("Aw thats good to hear! I am too very good.")
else:
    print("Aw thats intresting to hear.")
print("What did you do today?")
activities = input()
print("Ah cool! I have just talked to you today " + name + ".")
print("Tell me something about yourslef...")
info = input()
running = True
while running:
    if "brother" in info:
        print("Aw thats cool! I dont have any siblings myself.")
    elif "dog" in info:
        print("I lovvvveeeee dogs!")
    elif "computers" in info:
        print("Well I am a computer soooo...yeah.")
    else:
        print("Ah thats cool! Good bye!")
running = False



