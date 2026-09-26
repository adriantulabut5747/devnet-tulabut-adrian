"""
Midterm Practical Exam — Network Device Inventory Tool
Student: [Adrian A Tulabut]
"""

devices = []  # starts empty — the user adds devices as the program runs
name: str

def display_menu():
    print("choose what you want to do:")
    print("1 = Add devices")
    print("2 = View devices")
    print("3 = Count devices")
    print("4 = Find devices")
    print("5 = Check devices")
userinput = input()
pass

def add_device(device_list):
    print("Enter Devices You Want to add:")
    devices = input()
pass

def view_devices(device_list):
    print (devices)
pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
pass

# BONUS (optional)
 # def remove_device(device_list):
    # your code here
   # pass

def main():
     running = True
     while running:
      display_menu()
      if userinput == '1':
        display_menu()
      elif userinput == '2':
        add_device()
      elif userinput == '3':
        view_devices()
      elif userinput == '4':
        count_active_inactive()
      elif userinput == '5':
        find_device()
     else:
        print ("error")
running = False
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
pass


main()
