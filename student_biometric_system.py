from datetime import datetime

class StudentBiometricSystem:
    def __init__(self, details_file, log_in_file, log_out_file):
        self.details_file = details_file
        self.log_in_file = log_in_file
        self.log_out_file = log_out_file

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def user_search(self, student_id):
        with open(self.details_file, "r") as file:
            next(file) 

            for row in file:
                line = row.strip().split()

                if line[0].strip() == str(student_id).strip():
                    return line

        raise ValueError(f"User {student_id} not found")

    def input_entry(self, time_entered, user_details):
        with open(self.log_in_file, "a") as f:
            f.write(f"\n{user_details} {time_entered}")

    def output_entry(self, time_exited, user_details):
        with open(self.log_out_file, "a") as e_file:
            e_file.write(f"\n{user_details} {time_exited}")

    def sign_in(self):
        student_id = input("Enter your ID to sign-in: ")

        user = self.user_search(student_id)
        time_entered = self.get_time()
        self.input_entry(time_entered, user)

        return f"Hi {user[1].strip()}. You have entered at {time_entered}"
    
    def sign_out(self):
        student_id = input("Enter your ID to sign-out: ")

        user = self.user_search(student_id)
        time_exited = self.get_time()
        self.output_entry(time_exited, user)

        return f"Hi {user[1].strip()}. You have exited at {time_exited}"
    
    """
    Need to create a method for calculating the hours between time_entered and time_exited

    """
        


system = StudentBiometricSystem("student_details.txt", "student_log_in.txt", "student_log_out.txt")
print(system.sign_in())
print(system.sign_out())
