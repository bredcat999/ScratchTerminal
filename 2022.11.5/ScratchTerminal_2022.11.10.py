'''
ScratchTerminal by bredcat999
ver. 2022.10.25 (Early Release)

'''

import scratchattach as scratch3

username = input("Username: ")

print("Username and password please:")
session = scratch3.login(username, input())

#Splash Text
print("You have been signed in.")
print("Welcome to ScratchTerminal.")
print("---------")
print("ver. 2022.10.25.1")

#updates until 
while 1 == 1 :
    
    
    print("Search user:")
    user = session.connect_user(input())
    
    print("User stats:")
    
    #gets follower count
    print("Followers:")
    print(user.follower_count())
    
    #gets project count
    print("Projects:")
    print(user.project_count())
    
    #gets following count
    print("Following:")
    print(user.following_count())
    
    user.post_comment(username + " has searched you on ScratchTerminal, a program built using ScratchAttach made by @BreadcatGames.", parent_id="", commentee_id="") 
    
    print("Would you like to leave a comment? y/n")
    
    MenuInput = input()
    if MenuInput == "y" :
        print("Input the username of the person you want to comment on:")
        user = scratch3.get_user(input())
        
        print("Comment:")
        user.post_comment(input(), parent_id="", commentee_id="") 
        print("Done!")


    
    
    print("On standby...")


       
