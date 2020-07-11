import csv
from datetime import date
from datetime import timedelta
class ITAcademy:
    choose_course = list()
    balance = 0
    name=None
    address = None
    email = None
    mobile_num = None
    enrolled_date = date.today()
    due_date = enrolled_date + timedelta(weeks=12)
    def edit_user(self):
        email = input('Enter email: ')
        userdata = list()
        with open('user_info.csv','r') as user:
            reader = csv.DictReader(user)
            for row in reader:
                userdata.append(row)
            print(userdata)
            for dict_value in userdata:
                if email == dict_value['Email']:
                    print(dict_value['Name'])
                    dict_value['Name'] = input('New Name: ')
                    print(dict_value['Email'])
                    dict_value['Email'] = input('New Email: ')
                    print(dict_value['Address'])
                    dict_value['Address'] = input('New Address: ')
        print(userdata)
        user.close()

        with open('user_info.csv','w') as editedInfo:
            writer = csv.DictWriter(editedInfo, fieldnames=['Name','Email','Address','Course Enrolled','Payment Done','remaining Payment','Enrolled Date','Due Date'])
            writer.writeheader()
            writer.writerows(userdata)
        editedInfo.close()
    def show_available_course(self):
        courses = []
        with open('available_course.csv','r') as course:
            reader = csv.DictReader(course)
            for read in reader:
                courses.append(read['Course Name'])
                print(read['Course Name']+'\t\t\t\t'+read['Time Peroid'])
        course.close()
        while True:
            print("\n1. Inquire the course.")
            print("\n2. Enroll in the course.")
            print("\n3. Exit ")
            choice = int(input('\nEnter the choice: '))
            if choice == 1:
                self.inquire()
            elif choice == 2: 
                course_choice = input("Enter course you want to enroll: ")
                if course_choice in courses:
                    self.user(course_choice)
                else:
                    print("No course found. Try again..")

            elif choice == 3:
                exit()
            else:
                print("Invalid Choice. Try Again")
    def user(self,course_choice):
        self.name = input("Full Name: ")
        self.email = input("Email: ")
        self.address = input('Address: ')
        self.mobile_num = input("Mobile Number: ")
        self.payment_menu(course_choice)

    def payment_menu(self,course_choice):
        print("\nNote : Payment can be done in two installment.")
        print("\n1. Full Payment")
        print("\n2. Two Installment")
        print("\n3. Exit")
        payment_choice = int(input("\nEnter choice:"))
        if payment_choice == 1:
            amount = int(input('Full Payment (20000):'))
            paid = self.payment(amount)
            if paid == 'full paid':
                self.choose_course.append(course_choice)
                print(self.choose_course)
                self.user_info_save()
        elif payment_choice == 2 :
            amount = int(input('Half Payment (10000):'))
            paid = self.payment(amount)
            print(self.choose_course)
            if paid == 'partial paid':
                self.choose_course.append(course_choice)
                print(self.choose_course)
                self.user_info_save()
        elif payment_choice == 3:
            exit()
        else:
            print("Invalid Choice.. Try Again")

    def inquire(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        mobile_num = input("Enter mobile number: ")
        course_name = input("Course you want to inquire: ")
        print("Enter your Inquire:\n")
        inquire = input()
        print("\nYour Inquire has been submitted.")
        with open('inquire.csv' ,'a+') as inquires:
            writer = csv.writer(inquires)
            # writer = csv.DictWriter(inquires,fieldnames=['Name','Email','Mobile Number','Course','Inquiries'])
            # writer.writeheader()
            writer.writerows([(name,email,mobile_num,course_name,inquire)])
        inquires.close()
    
    def payment(self,amount):
        self.balance = 0
        self.balance += amount
        if self.balance == 20000:
            print("Full payment is done.. You are enrolled to the course")
            return 'full paid'
        elif self.balance == 10000:
            print("Partial payment is done.. ")
            print("Next Due Date is : ",(30*3)//2)
            return 'partial paid'
        else:
            print("Payment should be either 10000 or 20000")

    def user_info(self):
        with open('user_info.csv','r') as userinfo:
            reader = csv.DictReader(userinfo)
            print("Name\t\t","Email\t\t","Address\t","Course Enrolled\t","Payment Done\t","Remaining Payment\t","Enrolled Date\t","Due Date")
            for user in reader:
                print(user['Name'],"\t",user['Email'],"\t",user['Address'],"\t",user['Course Enrolled'],'\t\t',user['Payment Done'],'\t\t\t',user['remaining Payment'],'\t\t',user['Enrolled Date'],'\t',user['Due Date'])
        userinfo.close()

    def user_info_save(self):
        with open('user_info.csv','a') as userInfo:
            writer = csv.writer(userInfo)
            # writer.writerow(['Name','Email','Address','Course Enrolled','Payment Done','remaining Payment','Enrolled Date','Due Date'])
            writer.writerows([(self.name,self.email,self.address,self.choose_course,self.balance,20000-self.balance,self.enrolled_date,self.due_date)])
            userInfo.close()

    def deleteUser(self):
        email= input("Enter user email to delete user data: ")
        data = list()
        with open('user_info.csv','r') as usrdata:
            reader = csv.reader(usrdata)
            for row in reader:
                data.append(row)
                for field in row:
                    if field == email:
                        data.remove(row)
                        print("Successfully deleted user {}".format(email))
                         
        with open('user_info.csv','w') as usrdata:
            writer = csv.writer(usrdata)
            writer.writerows(data)

            

def main():
    it_academy = ITAcademy()
    print("\nWelcome To IT Academy.")
    while True:
        print("\n1.View Available Courses")
        print("\n2.User Informations")
        print("\n3.Update User Informations")
        print("\n4.Delete user data")
        print("\n5.Exit")
        choice = int(input("\nEnter the choice: "))
        if choice == 1:
            it_academy.show_available_course()
        elif choice == 2 :
            it_academy.user_info()

        elif choice == 3:
            it_academy.edit_user()
        elif choice == 4:
            it_academy.deleteUser()
        elif choice == 5:
            break
        else:
            print("Invalid choice.. Try Again")
            
    print("\nThank You For Visiting. Hope to see you soon..")


if __name__ == "__main__":
    main()