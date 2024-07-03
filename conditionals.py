temperature = int(input("How hot is it outside?\n"))
if temperature > 80: 
    print("It's too hot!")
    print("Stay inside!") #Notice the indent
#now we are out of the if statement
elif temperature < 60:
    print("It's too cold, stay inside!")
else: 
    print("Enjoy the outdoors!")

forecast = ["rainy", "cloudy", "sunny"]
howMany = int(input("On a scale of 0 to 2 how many clouds are in the sky?"))
function conditions{}
if howMany == 0:
    print(forecast[0])
elif howMany == 1:
    print(forecast[1])
elif howMany == 2 or 3:
    print(forecast[2])
else:
    print("Scale of 0 to 2")