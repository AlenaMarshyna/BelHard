# def do_something(a, b=6, c=None):
#     if not c:
#         print(a*b)
#     else:
#         print(a+b+c)
#
# a = 5
# b = 10
# do_something(2, 6, 7)
#
# def baz(**kwargs):
#     print(kwargs)
#
# baz(a=1, c=2, i=3)
#
# def do_it(a, b):
#     if a > b:
#         return a+b
#     else:
#         return a*b
# res = do_it(4, 5)
# print(res)
#
# def is_pol(text):
#     return text.lower() == text[::-1].lower()
#
#
# print(is_pol('Holloh'))
#
# def zam(a):
#     def zamok(b):
#         return a*b
#     return zamok
#
# c = zam(4)
# d = zam(8) b
# print(c(5))
# print(d(5))

# def decimal_(dec):
#     bin = ''
#     while dec > 0:
#         bin = str(dec % 2) + bin
#         dec //= 2
#     return bin
#
# print(decimal_(18))

# morse = {
#     'a':'111'
# }
# def text_morse(text):
#     global morse
#     result = ''
#     text = text.lower()
#     for i in text:
#         if i in morse:
#             result += morse[i] + ' '
#         if i == '  ':
#             result += '  '
#     return result

# def list_olffset(lst, n):
#     n -= len(lst) * (n // len(lst))  # dвыкидываем целое цисло цилов
#     lst = lst[-n:] + lst[:-n]
#     return lst
#
# print(list_olffset([1, 2, 3, 4, 5, 6, 7], 13))
#
# lst = [1, 2, True, 'rrr']
# lst = list(filter(lambda x: isinstance(x, str), lst))
# print(lst)
#
# a: int = int(input())
# a += 1
#
# lst = [1, 2, True, 'rrr']
# lst = list(filter(lambda x: isinstance(x, str), lst))
# print(lst)


 