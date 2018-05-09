test = {"hello": "hello", "goodbye": "goodbye", "seeya": "see ya!"}

user_input = ""
while user_input != "q":
    user_input = str(raw_input("> "))
    if user_input == "q":
        break
    for i in test.keys():
        if len(user_input) == 1 and user_input == i[0]:
            user_input = i
    if user_input in test:
        print(test[user_input])
print("done") 