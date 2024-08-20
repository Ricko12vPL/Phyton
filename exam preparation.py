# # Input the number of poor grades allowed
# poor_grades_limit = int(input())
#
# # Initialize variables to keep track of the necessary details
# poor_grades_count = 0
# total_grades_sum = 0
# problems_count = 0
# last_problem = ""
#
# while True:
#     # Read the problem name
#     problem_name = input()
#
#     # Check if the input is "Enough", indicating the end of input
#     if problem_name == "Enough":
#         # Calculate the average score
#         average_score = total_grades_sum / problems_count
#         # Print the results
#         print(f"Average score: {average_score:.2f}")
#         print(f"Number of problems: {problems_count}")
#         print(f"Last problem: {last_problem}")
#         break
#
#     # Read the grade for the current problem
#     grade = int(input())
#
#     # Increment the count of problems solved
#     problems_count += 1
#     # Add the grade to the total grades sum
#     total_grades_sum += grade
#     # Update the last problem name
#     last_problem = problem_name
#
#     # Check if the grade is a poor grade (<= 4)
#     if grade <= 4:
#         poor_grades_count += 1
#
#     # If the number of poor grades exceeds the limit, print a message and break the loop
#     if poor_grades_count == poor_grades_limit:
#         print(f"You need a break, {poor_grades_count} poor grades.")
#         break


poor_grades_max = int(input())
poor_grades_count = 0
problem_name = ""
problem_grade_sum = 0
problem_grade_count = 0

while problem_name != "Enough" or poor_grades_max != poor_grades_count:
    last_problem_name = problem_name
    problem_name = input()

    if problem_name == "Enough":
        if problem_grade_sum > 0 and problem_grade_count > 0:
            average_score = problem_grade_sum / problem_grade_count
        else:
            average_score = 0

        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {problem_grade_count}")
        print(f"Last problems: {last_problem_name}")
        break
    else:
        problem_grade = int(input())

        problem_grade_sum += problem_grade
        problem_grade_count += 1

        if problem_grade <= 4:
            poor_grades_count += 1

        if poor_grades_max == poor_grades_count:
            print(f"You need a break, {poor_grades_max} poor grades.")
            break


