#We would be using our knowledge abount booleans and comparison to compare the data of two students from a collection of grade submissions.

#We'll kick it off by saving the id, average grade, and recent test score in variables for each of the two student entries.

#Let's start saving the data for the first student entry! Create the variable ID_1 that stores "#4"

id_1 = "#4"

#Next, let's save the student's average grade by creating the variable AVERAGE_GRADE_1 with the value "A".

average_grade_1 = "A"

#Finally, save the student's test with the variable TEST_SCORE_1 and set it to 90.

test_score_1 = 90

#Let's move onto the next student entry! Like before, create id_2 that stores the value "#5".

id_2 = "#5"

#Create the variable AVERAGE_GRADE_2 and store the second student's average grade, "A".

average_grade_2 = "A"

#Finally, create TEST_SCORE_2, and store the second stident's test score, 70.

test_score_2 = 70

##Now that we've saved the data for each student entry,  we're ready to compare them.

# Next, we'll check for duplicate IDs, compare their average grade, and finally compare their test scores.

#Create a no_duplicates  variable that stores the result of the inequality comparison != between ID_! and ID_2.

no_duplicates = id_1 != id_2

#Start displaying the result of the comparison by using print with "No duplicate entries:"

print("no_duplicates entries:")

#Finally, display the value of the no_dupliocates variable.

print(no_duplicates)

#Next, create the variable same_average and store the result of comparing average_grade_1 and average_grade_2 with ==.

same_average = average_grade_1 == average_grade_2

#Display the string "Same average grade:" and on the next line display the variable same_average.
print("Same average grade:")

print(same_average)

#Next, instead a new variable called higher_score, use > to check if test_score_1 is greater than test_score_2.

higher_score  = test_score_1 > test_score_2

#To finish up, check the result by displaying "id_1 has a higher score:" then on the next line, display the variable higher_score.

print("id_1 has a higher score:")

print (higher_score)

