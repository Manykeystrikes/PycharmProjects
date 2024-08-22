#Problem2
def calculate_grade(mark):
    if mark >= 85:
        return 7
    elif mark >= 75:
        return 6
    elif mark >= 65:
        return 5
    elif mark >= 50:
        return 4
    else:
        return "F"

def main():
    total_marks = 0
    total_grades = 0
    count = 0

    while True:
        try:
            user_input = float(input("Enter a mark (or any non-numeric value to finish): "))
        except ValueError:
            break

        grade = calculate_grade(user_input)
        print(f"Grade is {grade}")

        total_marks += user_input
        total_grades += grade
        count += 1

    if count > 0:
        average_mark = total_marks / count
        average_grade = total_grades / count
        print(f"Average mark = {average_mark:.2f}")
        print(f"Average grade = {average_grade:.2f}")
    else:
        print("No valid marks entered.")

if __name__ == "__main__":
   main()
