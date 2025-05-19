items = {"coffee":100,
         "pen":200,
         "mouse":300,
         "phone":400,
         "cola":500,
         "book":600}

item = input("input name of item: ")
if item in items:   # if item in items.keys() -> item이 key로 존재할 때 검색.
    print(items[item])
else:
    print("not exist")