# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:30:05 2023

@author: lEO
"""

class Human:
    # OUR ATTRIBUTES OR CHARACTERISTICS
    def __init__(self, firstname, lastname, age, phone_number, height, weight, skin_color, eye_color, hair_style, body_build, shoe_size, fathers_name, mothers_name, gender):
        self.__firstname = firstname
        self.__lastname = lastname 
        self.__age = age
        self.__phone_number = phone_number
        self.height = height
        self.__weight = weight
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.hair_style = hair_style
        self.body_build =  body_build   # Possible options ("Average Size", "Muscular", "Chubby", "Obese", "Skinny", "Petite")
        self.__shoe_size = shoe_size
        self.__fathers_name = fathers_name
        self.__mothers_name = mothers_name
        self.__friends = []
        self.__gender = gender
    
    
    # OUR METHODS OR ACTIONS
    def make_friends(self, name):
        self.__friends_name = name
        self.__friends.append(self.__friends_name)
    
    def who_are_your_friends(self):
        return self.__friends
        
    # Write the METHOD to remove a friend --- ASSIGNMENT




Leonard = Human(
    firstname = "Leonard", 
    lastname = "Onyiriuba", 
    age = 25, 
    phone_number = "09076488226", 
    height = 6.1, 
    weight = 82, 
    skin_color = "Black", 
    eye_color = "Brown", 
    hair_style = "Afari", 
    body_build = "Obese", 
    shoe_size = 46, 
    fathers_name = "Leonard Snr", 
    mothers_name = "Stella", 
    gender = "Male")

Francis = Human(
    firstname = "Francis", 
    lastname = "Ndubeke", 
    age = 19, 
    phone_number = "09026498220", 
    height = 5.1, 
    weight = 92, 
    skin_color = "Black and Yellow Mix", 
    eye_color = "Blue", 
    hair_style = "Dreads", 
    body_build = "Obese", 
    shoe_size = 32, 
    fathers_name = "Edwin", 
    mothers_name = "Cynthia", 
    gender = "Male")
        
Vanessa = Human(
    firstname = "Vanessa", 
    lastname = "Enimorie", 
    age = 25, 
    phone_number = "09012580921", 
    height = 6.9, 
    weight = 62, 
    skin_color = "Yellow", 
    eye_color = "Green", 
    hair_style = "Braids", 
    body_build = "Skinny", 
    shoe_size = 52, 
    fathers_name = "Eddie", 
    mothers_name = "Felicia", 
    gender = "Female")   
  
    


Leonard.make_friends("Vanessa")
Leonard.make_friends("Henry")



# Leonards_friends = Leonard.who_are_your_friends()

















 
    
  
    
  
    
  
    
  
    


