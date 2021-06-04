class Employee:

    def check_hours(self, hours):
        print("Hours checked")

    def show_tasks(self):
        print("A lot of tasks done...")


class Manager(Employee):

    def show_tasks(self):
        print("Showing manager tasks...")

    def manage_teams(self):
        print("Managing teams...")


class Developer(Employee):

    def show_tasks(self):
        print("Showing programming tasks...")

    def code(self):
        print("Coding a lot...")


class Junior(Developer):
    pass


class Senior(Developer, Manager):
    pass

victor = Senior()
victor.code()
victor.show_tasks()

john = Junior()
john.show_tasks()