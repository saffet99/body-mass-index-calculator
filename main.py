import time
print("Body Mass Index Calculator")
print("This program calculate your body mass index. \n\nFirstly, we need you to input your 'Body Weight' in KG. \n"
      "Secondly, your 'Height' in Meter. So you need te enter your height like '1.72'\n")

decision= input("Press 'Y' to continue otherwise program will shut itself ").lower()
print("If the body mass index is between the following ranges print the respective result message:\n"
"- Below 18.5: UNDERWEIGHT\n"
"- Between 18.5-25: NORMAL\n"
"- Beten 25-30: OVERWEIGHT\n"
"- Between 30-35: OBESE\n"
"- Over 35: EXTREMELY OBESE\n\n")

while decision == "y":
      users_weight = input("Please enter your weight ")
      users_height = input("Please enter your height ")
      body_mass = round((float(users_weight) / float(users_height) ** 2), 2)
      if 0 <= body_mass and body_mass <= 100:
            print(body_mass)
            if body_mass <= 18.4:
                  print("Unfortunately you are UNDERWEIGHT")
            elif body_mass <= 25:
                  print("You are NORMAL")
            elif body_mass <= 30:
                  print("Be careful, you are OVERWEIGHT")
            elif body_mass <= 35:
                  print("Attention, you are OBESE")
            else:
                  print("Unfortunately you are EXTREMELY OBESE..")
            decision = input("If you want to recalculate press 'Y', "
                             "if you do not want, press 'Q' ").lower()
      if decision != "q" and decision != "y":
            print("You entered wrong value. Press 'Y' / 'Q' or it will turn off")
            decision = input("'Y' or 'N' ").lower()
else:
      print("Exiting...")
      time.sleep(5)
