#We'll use comparisons to check if the heart rate is too low or too high and tell the patient if they should worry about their health≥

#Create a HEART_RATE variable. it'll store the heart rate from the heart rate sensor. Set the heart_rate variable to a number so we can compare it to other numbers.

heart_rate =  77

#Create a too_low variable. We'll use it to tell us if a heart rate is too low. Now check if heart_rate is less than 60 and store the result in too_low.

too_low = heart_rate < 60

#Create a too_high variable. We'll use it to tell us if a heart rate it's too high. Now use > to  check if HEART_RATE is greater than 180.

too_high = heart_rate > 100

# We'll tell the patient if their heart rate is too low. Start by displaying HEART RATE LOW: in the console.

print("Heart rate low:")

#Now display the value of too_low in the console.

print(too_low)

#We'll also tell the patient if their heart rate is too high. Display HEART RATE HIGH: in console.

print("Heart rate high:")

#Now display the values of TOO_HIGH in the console.

print(too_high)

#You have built a neat Program that checks if a heart rate is too low or high. 
