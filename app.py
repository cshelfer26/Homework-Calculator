class HomeworkCalculator:
    def __init__(self):
        self.subjects = {
            "Science": {
                "Biology": 30,
                "Chemistry": 30,
                "Honors Chem": 30,
                "Physics": 30,
                "Honors Physics": 30,
                "AP Biology": 30,
                "AP Chemistry": 30,
                "AP Physics C": 30,
                "Environmental Science": 30,
                "Organic Chemistry": 30,
                "Human Biology": 30
            },
            "History": {
                "History 1": 30,
                "History 2": 30,
                "AP World History Modern": 30,
                "US History": 30,
                "AP US History": 30,
                "American Government": 30,
                "Economic Policy": 30,
                "International Relations": 30
            },
            "Language Level": {
                "1": 30,
                "2": 30,
                "3": 30,
                "3 Honors": 30,
                "4": 30,
                "⅚": 30,
                "Language and Culture": 30,
                "AP": 30,
                "Post-AP": 30
            },
            "English": {
                "English 1": 30,
                "English 2": 30,
                "English 2 Honors": 30,
                "English 3 American Literature": 30,
                "AP English Language and Composition": 30,
                "AP English Literature and Composition": 30,
                "World Literature": 30,
                "World Literature (Honors)": 30
            },
            "Math": {
                "Algebra 1": 30,
                "Geometry": 30,
                "Geometry Honors": 30,
                "Algebra 2": 30,
                "Algebra 2 Honors": 30,
                "Statistics and Precalculus": 30,
                "Precalculus AB Honors": 30,
                "Precalculus BC Honors": 30,
                "Intro to Calculus": 30,
                "Calculus 1": 30,
                "AP Calculus AB": 30,
                "AP Calculus BC": 30,
                "AP Statistics": 30,
                "Multivariable Calculus Honors": 30,
                "Linear Algebra Honors": 30
            },
            "Computer Science": {
                "Exploring Computer Science": 30,
                "Programming Interactive Media": 30,
                "Data Science": 30,
                "AP Computer Science Principles": 30,
                "AP Computer Science A": 30,
                "Post AP Computer Science Honors": 30
            }
        }

    def calculate_total_homework_time(self, classes):
        total_time = 0
        for class_name in classes:
            for subject, courses in self.subjects.items():
                if class_name in courses:
                    total_time += courses[class_name]
        return total_time


def main():
    calculator = HomeworkCalculator()

    print("Welcome to the Homework Time Calculator!")

    user_classes = []
    for subject, courses in calculator.subjects.items():
        print(f"\nPlease enter the {subject} classes you are taking, separated by commas:")
        user_input = input().strip().split(",")
        user_classes.extend([class_name.strip() for class_name in user_input])

    total_homework_time = calculator.calculate_total_homework_time(user_classes)
    print("\nTotal time for homework:", total_homework_time, "minutes")

if __name__ == "__main__":
    main()
