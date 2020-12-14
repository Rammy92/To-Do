def to_hello():
        print("Welcome to a simple To-Do app ")
        
def day():
        day = input("Which day of the week do you want to choose? ")
        return day
        
        
def create_todos_read_todos(day_of_the_week):
        
    user_choice = input(
"""Insert 1 if you want to add todos
Insert 2 if you want to see your todos""" + "\n")
    print(user_choice)
        
    if user_choice == "1":
        
            
            my_file = open("c:\Projects\\todos\\" + day_of_the_week + ".txt", "w")
            user_add_todos = input("please write your todo" + "\n")
            my_file.write(user_add_todos + "\n")
            
    elif user_choice == "2":

        
            my_file= open("c:\Projects\\todos\\" + day_of_the_week + ".txt", "r")

            contents = my_file.read()

            print(f"That what you have to do att {day_of_the_week} : " + contents + "\n")

    else:
        print("Somthing went wrong. Try again!")



my_list = [
        "mon.txt",
        "tue.txt",
        "wed.txt",
        "thu.txt",
        "fri.txt",
        "sat.txt",
        "sun.txt"
    ]
for filename in my_list:
        my_file = open("c:\Projects\\todos\\" + filename, "a+")

while True:
    
    
    to_hello()
    day_of_the_week = day()
    
    create_todos_read_todos(day_of_the_week)
    input_user = input("Do you want to exit y/n" + "\n") 
    if input_user == "y":
        print("Bye")
        break
    else: continue







