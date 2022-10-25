import scratchattach as scratch3
import tkinter as tk


print("Username and password please:")
session = scratch3.login(input(), input())

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
    
    print("On standby...")


       