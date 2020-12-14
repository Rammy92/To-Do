def to_hello():
    print("Welcome to a simple To-Do app ")
        
def day():
    while True:
        day = input("Which day of the week do you want to choose? "+ "\n")
        if day in [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]:
            return day

        print("Error")
        continue
        
        
        
def create_todos_read_todos(day_of_the_week, my_file):
    while True:        
        user_choice = input("""
Insert 1 if you want to add todos
Insert 2 if you want to see your todos""" + "\n")
        
        if user_choice == "1":
            
                
                my_file = open("c:\Projects\\todos\\" + day_of_the_week + ".txt", "a+")
                user_add_todos = input("please write your todo" + "\n")
                my_file.write(user_add_todos + "\n")
                break
        elif user_choice == "2":

            
                my_file= open("c:\Projects\\todos\\" + day_of_the_week + ".txt", "r")

                contents = my_file.read()

                print(f"That what you have to do att {day_of_the_week}: " +"\n" + contents)
                break
        else:
            print("Somthing went wrong. Try again!")
            continue




def days_list():
    my_list = [
            "monday.txt",
            "tuesday.txt",
            "wednesday.txt",
            "thursday.txt",
            "friday.txt",
            "saturday.txt",
            "sunday.txt"
        ]
    for filename in my_list:
        my_file = open("c:\Projects\\todos\\" + filename, "a+")
        return my_file





while True:
    
    my_file = days_list()
    to_hello()
    day_of_the_week = day()
    
    create_todos_read_todos(day_of_the_week, my_file)


    input_user = input("Do you want to exit y/n" + "\n") 
    if input_user == "y":
        print("Have a nice day!")
        break
    if input_user == "n": 
        True
    else:
        continue
    






