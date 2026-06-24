import random

subjects = [
    "A Karen",
    "A TikToker",
    "A raccoon",
    "Your ex",
    "An alien",
    "A toddler"
]

actions = [
    "sued",
    "bribed",
    "robbed",
    "hypnotized",
    "married",
    "flew into"
]

places = [
    "Arby's",
    "Space",
    "a Walmart",
    "a cult",
    "an IKEA",
    "jail"   
]

sponsors = [
    "Sugar-Free Mayonnaise.",
    "Concrete Pillows.",
    "The Federation of Angry Raccoons.",
    "Dehydrated Water: Just Add Water!",
    "Socks with individual toe holes."
]

print("Welcome to the Fake News Generator Program!!! \n")


while True:
    subject=random.choice(subjects)

    action=random.choice(actions)

    place=random.choice(places)
    
    sponsor=random.choice(sponsors)
    
    print(f"Breaking News: {subject} {action} {place} \n ")
    print(f"This news is brought to you by {sponsor}\n")
   
    
    user_input=input("Do you want to generate another headline yes/no:\n").strip()
    if user_input=="no":
        break
    
    
    
print("Thank's for playing.Stay tunned for more fake news!!!")
        