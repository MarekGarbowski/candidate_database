import json


def add_user():
    with open("data/users.json", "r+") as file:
        data = json.load(file)
        print(data)
        print(type(data))
        user_name = input('Podaj nazwę użytkownika: ')
        for name in data:
            if name["user_name"] != user_name:
                continue
            if user_name not in data:
                password = input('Podaj hasło uzytkownika: ')
                new_user = {
                    "user_name": user_name,
                    "passowrd": password
                }
            else:
                print('Nazwa użytkownika już jest zajęta, podaj inną.')
                return
        data.append(new_user)
        with open("data/users.json", "w") as new_file:
            json.dump(data, new_file)
        # print(data)
        # file.seek(0)
        json.dumps(data)
        print(type(data))
        print(data)


add_user()
