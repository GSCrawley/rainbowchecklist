import sys

def print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()

checklist = list()
def create(item):
   checklist.append(item)
def read(index):
   item = checklist[index]
   return item
def update(index, item):
   checklist[index] = item
def destroy(index):
   checklist.pop(index)
def list_all_items():
   index = 0

   for list_item in checklist:
       print(str(index) + list_item)
       index += 1

def mark_completed(index):
   update(index, "√" + checklist[item])
   list_all_items()

def select(function_code):
   # Create item
   if function_code == "C":
       input_item = user_input("Input item:")
       create(input_item)
   # Read item
   elif function_code == "R":
       item_index = user_input("Index Number")
       # Remember that item_index must actually exist or our program will crash.
       print(read(int(item_index)))
   elif function_code == "D":
       index = user_input("Index Number")
       destroy(index)
       list_all_items()
   elif function_code == "U":
       index = user_input("Index Number")
       item = user_input("item")
       update(int(index), item)
       list_all_items()
   # Print all items
   elif function_code == "P":
       list_all_items()
   elif function_code == "Q":
       return False
   # Catch all```
   else:
       print("Unknown Option")
   return True

# I did it a little differently - user is asked what dsy it is; console outputs Captain Rainbow's outfit according to that day.

def user_input():
   user_input = input("What day is it today?")
   return user_input

colors = ["red","yellow","orange","blue","green","purple","pink"]
clothing = ["shoes","socks","pants","shirt","jacket","tie","hat"]


outfits = {
"Sunday":colors[0]+" "+clothing[0]+
        ", "+colors[1]+" "+clothing[1]+
        ", "+colors[2]+" "+clothing[2]+
        ", "+colors[3]+" "+clothing[3]+
        ", "+colors[4]+" "+clothing[4]+
        ", "+colors[5]+" "+clothing[5]+
        ", "+colors[6]+" "+clothing[6],
        "Monday":colors[1]+" "+clothing[0]+
            ", "+colors[2]+" "+clothing[1]+
            ", "+colors[3]+" "+clothing[2]+
            ", "+colors[4]+" "+clothing[3]+
            ", "+colors[5]+" "+clothing[4]+
            ", "+colors[6]+" "+clothing[5]+
            ", "+colors[0]+" "+clothing[6],
        "Tuesday": colors[2]+" "+clothing[0]+
            ", "+colors[3]+" "+clothing[1]+
            ", "+colors[4]+" "+clothing[2]+
            ", "+colors[5]+" "+clothing[3]+
            ", "+colors[6]+" "+clothing[4]+
            ", "+colors[0]+" "+clothing[5]+
            ", "+colors[1]+" "+clothing[6],
        "Wednesday":colors[3]+" "+clothing[0]+
            ", "+colors[4]+" "+clothing[1]+
            ", "+colors[5]+" "+clothing[2]+
            ", "+colors[6]+" "+clothing[3]+
            ", "+colors[0]+" "+clothing[4]+
            ", "+colors[1]+" "+clothing[5]+
            ", "+colors[2]+" "+clothing[6],
        "Thursday":colors[4]+" "+clothing[0]+
            ", "+colors[5]+" "+clothing[1]+
            ", "+colors[6]+" "+clothing[2]+
            ", "+colors[0]+" "+clothing[3]+
            ", "+colors[1]+" "+clothing[4]+
            ", "+colors[2]+" "+clothing[5]+
            ", "+colors[3]+" "+clothing[6],
        "Friday":colors[5]+" "+clothing[0]+
            ", "+colors[6]+" "+clothing[1]+
            ", "+colors[0]+" "+clothing[2]+
            ", "+colors[1]+" "+clothing[3]+
            ", "+colors[2]+" "+clothing[4]+
            ", "+colors[3]+" "+clothing[5]+
            ", "+colors[4]+" "+clothing[6],
        "Saturday":colors[6]+" "+clothing[0]+
            ", "+colors[0]+" "+clothing[1]+
            ", "+colors[1]+" "+clothing[2]+
            ", "+colors[2]+" "+clothing[3]+
            ", "+colors[3]+" "+clothing[4]+
            ", "+colors[4]+" "+clothing[5]+
            ", "+colors[5]+" "+clothing[6]

}
weekdays = list(outfits.keys())

user_guess = user_input()

for i in range(len(weekdays)):
    if user_guess==weekdays[i]:
        print("Today is {}. On {}s, Captain Rainbow wears \n {}".format(user_guess, user_guess, outfits[user_guess]))

def user_input(prompt):
    user_input = input(prompt)
    return user_input

#instead of inputting C,Q,R,etc, the user will input the day of the week, which will then determine the output
# Select function for getting input from terminal.
# user_value = user_input("Please Enter a value:")
# print(user_value)
#
# def test():
#     running = True
#     while running:
#         selection = user_input(
#         "Press C to add to list, Q to stop loop, R to Read from list, D to remove items and P to display list")
#         running = select(selection)



# Select function for getting input from terminal.
