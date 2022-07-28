student_scores = {
	"Harry": 81,
	"Ron": 78,
	"Hermione": 99,
	"Draco": 74,
	"Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
def scoring_criteria(number):
	if number > 90:
		return "Outstanding"
	elif 80 < number < 91:
		return "Exceeds Expectations"
	elif 70 < number < 81:
		return "Acceptable"
	else:
		return "Fail"


for score in student_scores:
	student_grades[score] = scoring_criteria(student_scores[score])

# 🚨 Don't change the code below 👇
print(student_grades)
