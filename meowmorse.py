#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main():
    import random
    import string
    a = eval(input("How many questions do you want? Type '0' for instructions"))
    letra = {'a': '_.', 'b':'_...', 'c':'_._.', 'd':'_..', 'e':'.', 'f':'.._.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}
    i = 0
    correct = 0
    
    if a == 0:
        print("This is a review game that tests your knowledge of the letters of morse code.\n")
        print("If at any point you get stuck type 'help' in the response bar.\n")
        print("Typing 'help' will give you another chance to answer correctly and avoid the sad cat that will come for you if you answer wrong. \n")
        a = eval(input("How many questions do you want?"))
 
    while i < a:
        m = random.choice(string.ascii_letters).lower()
        b = input(letra[m])
        
        if b == m: 
            print("                    /\___/\ ")
            print("Correct, Great Job!( =^.^= ) ")
            print("                    (0)_(0)_/ ")
            correct += 1
        
        elif b == "help":
            print()
            print("a: _. b: _... c: _._. d: _.. e: . f: .._. g: --. h: ....")
            print("i: .. j: .--- k: -.- l: .-.. m: -- n: -. o: --- p: .--.")
            print("q: --.- r: .-. s: ... t: - u: ..- v: ...- w: .-- x: -..- y: -.-- z: --..")
            b = input(letra[m])
             
        else: 
            print("!! /\___/\  !!")
            print("!!( =T.T= ) !! ", letra[m], "is", m)
            print("!! (0)_(0)_/!! ")
            
        i +=1
        
    print("Thank you for playing! Score:", correct,"/", a)
main()


# In[ ]:





# In[ ]:




