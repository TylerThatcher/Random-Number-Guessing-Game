#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random

def guess_game():
    game = True
    while game:
    
        number = random.randrange(1, 10)
        tries = 0
             
        ## Game Start
        print("I'm thinking of a number between 1 and 10")

        guess = int(input("Have a guess, you have 3 tries: "))
        while guess != number:

        ## Check win/lose
            if guess == number:
                print('Congrats you got it!')
                game = False


        ## Check if guess is higher or lower
            if guess > number:
                print("Guess lower...")
                tries = tries + 1


            if guess < number:
                print("Guess higher...")
                tries = tries + 1

            if tries == 3:
                print('You lose!')
                game = False

            if game == True:
                guess = int(input("Have another guess: "))
            else:
                break

        if guess == number:
                print('Congrats you got it! First guess too, awesome!')
                game = False
            
       
    
    


# In[6]:


guess_game()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




