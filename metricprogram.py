print("I will ask for two numbers, feet and inches, so please enter them in order of _ft. and _in.")
# 1 ft. = 0.3048 meters
# 1in. = 0.0253 meters
feet = int(input("Ft?"))
inches = int(input("In?"))

#note the conversion rates are "HARD-CODED"
meters = (feet * 0.3048) + (inches * 0.0254)

print("You are " + str(meters) + " meters tall.")