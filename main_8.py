# class UserN:
#     role = 'user'
#
#     def __init__(self, f_name: str) -> None:
#         self.first_name: str = f_name.title()
#
#     def info(self) -> str:
#         return f'Name {self.first_name} and {UserN.role}'
#
#
#
#     @classmethod
#     def change_role(cls, new_role):
#         cls.role = new_role.lower()
#
#     @staticmethod
#     def method(a, b):
#         return a+b
#
# vasa = UserN(f_name='Vass')
# vasa.last = 'pupkin'
# sash = UserN(f_name='sasss')
#
# print(sash.info())
# print(vasa.role)
# print(sash.role)
# UserN.change_role(new_role='ttt')
# print(UserN.role)
# # print(UserN.method(4, 5))
#
# class MyClass:
#     name = 'My name is '
#
#     def __init__(self, my_n: str, age: int) -> str:
#         self.my_n = my_n.title()
#         self.age = age
#
#     def __str__(self):
#         return self.my_n
#     def __int__(self):
#         return self.age
#
#     def info(self):
#         return f'Ok! Your name is {self.my_n} and My name is {MyClass.name}'
#
#     def __len__(self):
#         return self.age*2
#
#
# user = MyClass(my_n = 'alena', age=35)
# print(len(user))

class Button:
    def __init__(self, text: str, request_contact: bool = False) -> None:
        self.text = text
        self.request_contact = request_contact

    def dict(self) -> dict:
        return {'text': self.text, 'request_contact': self.request_contact}

user = Button(text = 'a', request_contact=True)
print(user.dict())

class Keybord:

    def __init__(self, keybord: list[list[Button]]) -> None:
        if not isinstance(keybord, list):
            raise ValueError
        for line in keybord:
            if not isinstance(line, list):
                raise ValueError
            for button in line:
                if not isinstance(button, list):
                    raise ValueError
        self.keybord= keybord

    def sr(self) -> list[list[dict]]:
        from copy import deepcopy
        keybord = deepcopy(self.keybord)


