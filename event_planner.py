# Task 1: Code Correction

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue) 

# Task 2: Venue Selection 

if venue == "large hall":
    print("audio system recommended") if int(attendees) >= 150 else print("projector recommended")  
        
# Task 3: Catering Choices

catering_food = input("Would you like vegetarian food (yes or no)?") 
print("We recommend Veggie Delight Caterers") if catering_food == "yes" else print("We recommend Gourmet Meals Caterer") 
