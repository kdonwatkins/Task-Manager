# This program will help you keep track of your users and tasks!

# There are 6 pre-defined functions and the actual program flowchart has three sections:

# STAGE 1: LOGIN PROCESS
# STAGE 2: IDENTIFY USER'S OBJECTIVE
# STAGE 3: IMPLEMENTING USER'S OBJECTIVE

########################################################################################################################################################

### PRE-DEFINED FUNCTIONS ###

# FUNCTION 1

def reg_user():                                                 # Register a user (that has not been registered before)

    print("Great! You would like to register a new user! You need to set a new username and password.")

    user_file = open("user.txt", "r")
    contents = user_file.read()

    valid_choice = False

    while valid_choice == False:
        
        user_name = str.lower(input("\nPlease enter a new username: "))
        pword = input("Please enter a new password: ")      
        pword2 = input("Now reenter and confirm the pasword: ")

                
        if (pword == pword2) and (user_name not in contents):
            valid_choice = True
                
            print("Great, your username and password will be stored in the 'user.txt' file.")
                
            with open("user.txt", "a") as user_file:
                user_file.write("\n" + user_name.lower() + ", " + pword)
                break
                
        elif (pword != pword2) or (user_name in contents):      # If user already registered then they will have to retry
            valid_choice = False
            print("\nWhoops! Please make sure that your passwords match and your username is original. Please try again!")
                    
        user_file.close()



# FUNCTION 2
           
def add_task():             # Add a task to a text file

    import datetime
    today = datetime.date.today()
    
    print("\nGreat! You would like to add a task!")

    task_user = str.lower(input("Please enter the username of the person the task is assigned to: "))  
    task_title = input("Please enter the title of the task: ")
    task_descrip = input("Please enter a description of the task: ")
    task_due = input("Please enter the due date of the task (YYYY-MM-DD format only): ")        # Specific format requested to match 'datetime's format
        
    with open("tasks.txt", "a") as user_file:                          
        user_file.write(f"\n{task_user}, {task_title}, {task_descrip}, {today}, {task_due}, No") # Task written to file in desired format
        user_file.close()

        print("\nGreat! Your new task has been stored in the 'tasks.txt' file.")



 
# FUNCTION 3

def view_all():                                     # View all registered tasks

    print("\nGreat! You would like to view all tasks! Here they are:")

    task_file = open("tasks.txt", "r")
        
    for line in task_file:
        details = line.strip().split(", ")          # Strip/Split here to display (accurate) separate items within each task
            
        print(f"\nTask:\t{details[1]}")     
        print(f"Assigned to:\t{details[0]}")
        print(f"Task description:\t{details[2]}")
        print(f"Date Assigned:\t{details[3]}")
        print(f"Due Date:\t{details[4]}")
        print(f"Task Complete?\t{details[5]}")

    task_file.close()



# FUNCTION 4

def view_mine():                                    # User can view and edit specific tasks

    specific_choice = str.lower(input("""\nPlease choose an option:

'A' to view all personal tasks
'B' to access a specific tasks
'-1' to exit: """)) 

    if specific_choice == "a":                                 # Choice 1 - display user's specific tasks

        user_file = open("tasks.txt", "r")
   
        for index, line in enumerate(user_file, start = 1):

            if (specific_choice == "a") and (user_name in line):
            
                details = line.strip().split(", ")      
            
                print("\nHere are all tasks assigned to you (if you have any!):")
                print(f"\nTask number:\t{index}.")
                print(f"Task:\t\t{details[1]}")         
                print(f"Assigned to:\t{details[0]}")
                print(f"Task description: {details[2]}")
                print(f"Date Assigned:\t{details[3]}")
                print(f"Due Date:\t{details[4]}")
                print(f"Task Complete?\t{details[5]}")

        user_file.close()
        

    elif specific_choice == "b":                                # Choice 2 - User selects specific task to edit

        user_file = open("tasks.txt", "r")

        specific_task = int(input("\nPlease enter the task number: "))
        user_choice = str.lower(input("\nWould you like to mark the task complete ('A') or edit the task ('B')? "))

        new_contents = ""

        if user_choice  == "a":                                 # Choice 2A - Change a task to complete (i.e. 'Yes')
        
            for index, line in enumerate(user_file, start = 1):
                new_line = line.strip()
            
                if index == specific_task:
                    new_contents += new_line.replace("No", "Yes") + "\n"
                else:
                    new_contents += new_line + "\n"

            print("\nGreat! Task was changed to complete ('Yes') in tasks.txt.")  
            user_file = open("tasks.txt", "w")
            user_file.write(new_contents)
            

        elif user_choice == "b":                                # Choice 2B - Change task's username and due date

            print("\nIf the task you want to edit can be edited you will be prompted to here. Tasks need to be incomplete to be edited!")

            for index, line in enumerate(user_file, start = 1):
                real_line = line.strip()
                new_line = line.strip().split(", ")
            
                if index == specific_task and new_line[5] == "No":
                    new_username = input("\nPlease type a new username: ")
                    new_due_date = input("Please type a new due date: ")

                    final = real_line.replace(new_line[0], new_username)
                    new_contents += final.replace(new_line[4], new_due_date) + "\n"

                else:
                    new_contents += real_line + "\n"

            user_file = open("tasks.txt", "w")
            user_file.write(new_contents)
 

        user_file.close()
                  

    elif specific_choice == "-1":                                 # Choice 3 - Exit
        exit()




# FUNCTION 5

def generate_reports():                             # User generates reports based on users or task information

    import datetime
    today = datetime.date.today()

    task_overview = open("task_overview.txt", "w")  # Task details file generated here

    task_file = open("tasks.txt", "r")
    user_file = open("user.txt", "r")

    task_count = 0
    tasks_complete = 0
    tasks_incomplete = 0
    overdue_count = 0
    overdue_and_incomplete = 0

       
    for line in task_file:
            
        task_count += 1
            
        details = line.strip().split(", ")

        date1 = str(datetime.date.today())
        today_date = date1.replace("-", "")

        date2 = str(details[4])
        task_due = date2.replace("-", "")
            
        if details[5].lower() == "yes":
            tasks_complete += 1
        if details[5].lower() == "no":
            tasks_incomplete += 1
        if int(today_date) > int(task_due):
            overdue_count += 1
        if (details[5].lower() == "no") and (int(today_date) > int(task_due)): # Date module brought in
            overdue_and_incomplete += 1

    task_file.close()
    user_file.close()   

    incomplete_percentage = round(((tasks_incomplete / task_count) * 100), 2)
    overdue_percentage = round(((overdue_count / task_count) * 100), 2)
                
    task_overview.write("Task information below:\n")            
    task_overview.write(f"\n\tTotal generated and tracked tasks: {task_count}.")
    task_overview.write(f"\n\tTotal complete tasks: {tasks_complete}.")
    task_overview.write(f"\n\tTotal incomplete tasks: {tasks_incomplete}.")
    task_overview.write(f"\n\tTotal incomplete and overdue tasks: {overdue_and_incomplete}.")       
    task_overview.write(f"\n\tPercentage incomplete tasks: {incomplete_percentage}%.")                          
    task_overview.write(f"\n\tPercentage overdue tasks: {overdue_percentage}%.")

    user_overview = open("user_overview.txt", "w")      # Task details file generated here

    task_file = open("tasks.txt", "r")
    user_file = open("user.txt", "r")

    user_count = 0
    users_tasks = 0
    tasks_complete = 0
    tasks_incomplete = 0
    incomplete_and_overdue = 0
    

    for line in user_file:
        user_count += 1

    for line in task_file:
        details = line.strip().split(", ")

        date1 = str(datetime.date.today())
        today_date = date1.replace("-", "")

        date2 = str(details[4])
        task_due = date2.replace("-", "")
        

        if user_name in line:
            users_tasks += 1
        if (user_name in line) and (details[5].lower() == "yes"):
            tasks_complete += 1
        if (user_name in line) and (details[5].lower() == "no"):
            tasks_incomplete += 1
        if (user_name in line) and (details[5].lower() == "no") and (int(today_date) > int(task_due)):
            incomplete_and_overdue += 1

    task_file.close()
    user_file.close()

    user_percentage = round(((users_tasks / task_count) * 100), 2)
    complete_percentage = round(((tasks_complete / users_tasks) * 100), 2)
    incomplete_percentage = round(((tasks_incomplete / users_tasks) * 100), 2)
    incomplete_overdue_percentage = round(((incomplete_and_overdue / users_tasks) * 100), 2)
            
    user_overview.write("Current user information below:\n")
    user_overview.write(f"\n\tTotal users: {user_count}.")
    user_overview.write(f"\n\tTotal generated and tracked tasks: {task_count}.")
    
    user_overview.write(f"\n\tTotal tasks belonging to you: {users_tasks}.")
    user_overview.write(f"\n\tTotal percentage of tasks assigned to you: {user_percentage}%.")
    user_overview.write(f"\n\tTotal percentage of your completed tasks: {complete_percentage}%.")
    user_overview.write(f"\n\tTotal percentage of your tasks are incomplete: {incomplete_percentage}%.")
    user_overview.write(f"\n\tTotal percentage of your incomplete and overdue tasks: {incomplete_overdue_percentage}%.")
            


# FUNCTION 6

def view_stats():                                   # User views stats on generated reports

    import os.path

    file_created = False                            # This checks if a file is created already. If not, it will be created beforehand

    if os.path.isfile("task_overview.txt"):
        file_created = True
    else:
        file_created = False

    if file_created == False:
        task_file = open("task_overview.txt", "w")
        user_file = open ("user_overview.txt", "w")
        file_created = True

    
    if file_created == True:
        task_file = open("task_overview.txt", "r")
        user_file = open ("user_overview.txt", "r")
        
        print("\nGreat! You would like to see current statistics! If you dont see them below, it means you havent generated any.\n")

        task_contents = ""
        user_contents = ""
        
        for line in task_file:
            task_contents += line
              
        for line in user_file:
            user_contents += line

        print(task_contents)
        print("")
        print(user_contents)

    task_file.close()
    user_file.close()
    


############################## ACTUAL PROGRAM: STAGE 1 - LOGIN PROCESS ######################################

login_success = False   
username_check = False
password_check = False
valid_choice = False

print("Greetings and welcome to our online task manager!")
print("Let's get you logged in to get started!")

user_file = open("user.txt", "r")                      
login = user_file.read()

user_name = str.lower(input("\nPlease enter your username here: "))       

while username_check == False:                                      
    
    if user_name in login:                              
        print("\nGreat! Username found! Now we just need your password!")
        username_check = True
        break
    elif user_name not in login:
        user_name = input("Username not found! Please reenter your username here: ")


user_pword = str.lower(input("Please enter your password here: "))

while username_check == True:
    
    if user_pword in login:                             
        print("Great! Password found!")
        login_success = True
        break
    elif user_pword not in login: 
        user_pword = input("No match! Please reenter your password here: ")

    
        
############################## STAGE 2: IDENTIFY USER'S OBJECTIVE ##############################################

if login_success == True and user_name != "admin":          
    print("""\nPlease select one of the following options:

    "A" - to add a task
    "VA" - to view all tasks
    "VM" - to view all of your tasks
    "GR" - to generate reports
    "E" - to exit/logout""")
    
elif login_success == True and user_name == "admin":        
    print("""\nPlease select one of the following options:

    "R" - to register a new user
    "A" - to add a task
    "VA" - to view all tasks
    "VM" - to view all of your tasks
    "GR" - to generate reports  
    "S" - to view statistics
    "E" - to exit/logout""")

user_choice = str.lower(input("\nPlease type your choice (letter only): "))   


############################## STAGE 3: IMPLEMENTING USER'S OBJECTIVE ###########################################


while user_choice == "r" and user_name != "admin":                                         
    user_choice = input("Sorry but only Admin can register new users. Please enter a valid option: ") 
    break

valid_choice = False

while valid_choice == False:
    
    if user_choice == "r" and user_name == "admin":     ## CHOICE 1: Register a new user
        reg_user()
        break

    elif user_choice == "a":                            ## CHOICE 2: Add a new task
        add_task()
        break

    elif user_choice  == "va":                          ## CHOICE 3: View all tasks
        view_all()
        break

    elif user_choice == "vm":                           ## CHOICE 4: User views tasks only assigned to them
        view_mine()
        break

    elif user_choice == "gr":                           ## CHOICE 5: User (Admin only) wants to view statistics
        generate_reports()
        break

    elif user_choice == "s":                            ## CHOICE 6: User wants to generate reports
        view_stats()
        break
        
    elif user_choice == "e":                            ## CHOICE 7: User wants to exit
        exit()
        
    else:
        user_choice = input("Invalid input. Please reenter a valid choice (letter only): ")

