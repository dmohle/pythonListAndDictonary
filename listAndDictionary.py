# listAndDictionary.py
# dH
# 8/27/23
#
# Lists[] and Dicts{}
#
# A list of numbers
my_list_of_nums = [11, 5, 33, 74, 55]
print(my_list_of_nums)
print("my_list_of_nums[3] is: " + str(my_list_of_nums[3]))
print("my_list_of_nums[] is: " + str(my_list_of_nums))
# change an element in the list
my_list_of_nums[2] = 745312
print("my_list_of_nums[] is: " + str(my_list_of_nums))
# Loop thru the list with a for-in loop()
for i in my_list_of_nums:
    print(i)
print("*********")
print("")
for num in my_list_of_nums:
    print(num)
print("*********")
print("")
my_dict_of_chars = {}
print("my_dict_of_chars is a " + str(type(my_dict_of_chars)))
my_dict_of_chars["a"] = 0
my_dict_of_chars["b"] = 8
print(my_dict_of_chars)
my_str = "The quick brown fox jumped over the lazy dog. and The lazy dog bowed to the regal fox."
print(my_str)

for i in my_str:
    print(i)
    # the first char is 'T', so we need a key named "T"
    # check if "T" is none or not.
    if my_dict_of_chars.get(i) == None:
        print("Key not found, creating one now...")
        # Create a new key with an initial value of 1
        my_dict_of_chars[i] = 1
    else:
        print("Key found, incrementing the value of the key now!")
        # Add 1 to the value of the char found
        my_dict_of_chars[i] = my_dict_of_chars[i] + 1

# print the dictionary
print("my_dict_of_chars is a " + str((my_dict_of_chars)))
# In this for,in loop, the K loop control variable represents the key and the V represents the value of the key.
# Your output should show the number of specific characters in my_str
for k, v in my_dict_of_chars.items():
    print(k + ": " + str(v))








