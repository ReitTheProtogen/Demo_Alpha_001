# calculations portion
key = 0

menu = input("Welcome to Facility Demo! type 'start' to begin, or type 'help' anytime for help! :3. ")
# useful commands of those new
if menu == 'help':
    print("'pick up (object)' to grab or interact")
    print("'inspect (object)' to inspect")
    print("'use (object)' to use something")

# starting of the game
elif menu == 'start':
    print("Snow falls all around, blanketing the ground in a sea of white. Your coat is caked in the powder as cold washes over you.\n Before long, A light illuminates in the distance, like a twinkle, a twinkle of hope.")
    owo = input("do you wish to continue towards the light? ")

# second choice
    # start of the game (NO) choice
    if owo == 'no':
        print(
            "You ignore the light and go off into a random direction. Warmth slowly encroaches as your organs slowly fail.\n The memories that led you here fill your mind as you fall into the snow, and close your eyes to dream forever more.")
        quit()
# help
    elif owo == 'help':
        print("'pick up (object)' to grab or interact")
        print("'inspect (object)' to inspect")
        print("'use (object)' to use something")

    elif owo == 'yes':
      print("you slowly walk towards the light, before long a one story home looms over you. The only way up is up the stairs, covered in snow.")
      print("going up the stairs, you step onto a wooden porch. ")

      # value to help the story part 1
      while True:
          porch = input("> ")

          # main story part 1
          if porch == "inspect mat":
              print("Under the door is a mat, it reads 'welcome home'")

          elif porch == 'help':
               print("'pick up (object)' to grab or interact")
               print("'inspect (object)' to inspect")
               print("'use (object)' to use something")

          elif porch == "kick door":
              print("You try to kick the door open, and it works! Though the door sliced your leg open and you rapidly bleed out.")
              quit()

          elif porch == "inspect porch":
              print("The porch is wooden, bare of snow thanks to the ceiling above. A broken fan hangs above. There is a mat under the door.")

          elif porch == "inspect fan":
              print("It's a standard ceiling fan, the blades wooden. The strings are broken off.")

          elif porch == "pick up mat" and key == 0:
              print("You lift it up and you find a key, you pocket it.")
              key = 1

          elif porch == "pick up mat" and key == 1:
              print("The mat is too big to carry.")

          elif porch == "use door" and key == 0:
              print("You try the door and it's locked shut.")

          elif porch == "use door" and key == 1:
              print("You insert the key and open the door. It creaks open and lets you inside.")
              quit()

          else:
              print("You cannot do that.")

      # values to help part 2
      while True:
          home = input("> ")

      # story part 2
          if home == 'test':
              print("Walking inside, warmth hides your body like a warm blanket. As the door slammed shut behind, you were left with \nkitchen, living room, bedroom, bathroom, dining room, and a closet")

          elif home == 'help':
              print("'pick up (object)' to grab or interact")
              print("'inspect (object)' to inspect")
              print("'use (object)' to use something")

          else:
              print("I cannot do that.")



    # stops the program if the player fucks up like a dumb-ass
    else:
          quit()

# stops the program if the player fucks up like a dumb-ass
else:
    quit()