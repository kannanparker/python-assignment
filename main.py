import random
cookie = input("Enter cookie number:")
print("your cookie number is: " + cookie)


fortune = ["Today will be a Lucky day", "You will meet someone new and intresting", "Watch out of obstacles in your path"]
for x in fortune:
   m=random.choice(fortune)
   print("Your Fourtune is : " +str(m))
   break