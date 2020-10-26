# This code returns some mad libs text based on the user input
# Is the code always returning the correct input?
# What do you think I did to write this code that I shouldn't have done?
#Answer ---> return causes the function to exit or terminate immediately, even if it is not the last statement of the function.
def change_name(adjective):# you forgot to put a colon at the end of the function definition.

    if adjective =='red':
        print( "The quick brown fox jumps over the red dog")
    elif adjective == 'lazy':
        print ("The quick brown fox jumps over the lazy dog")
    elif adjective == 'energetic':
        print ("The quick brown fox jumps over the energetic dog")
    elif adjective == 'happy':
        print ("The quick brown fox jumps over the happy dog")
    elif adjective == 'sad':
        print ("The quick brown fox jumps over the happy dog")
    else:
        print ("No case for that adjective found!")
adj =input("Enter one of the following adjectives\n 1) red\n 2) lazy\n 3)energetic\n 4) happy\n 5)sad\n").lower() # to convert the any uper case letter to lower case 
change_name(adj)
