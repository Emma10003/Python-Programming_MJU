total = 0
num = 1

print("1부터 10까지의 합계는")
# for num in range(1, 11, 1):
#     if num == 10:
#         total += num
#         print(num, end=' = ')
#         break
#     total += num
#     print(num, end=' + ')
#     num += 1

for num in range(1, 11):
    if num == 10:
        total += num
        print(num, end=' = ')
    else:
        total += num
        print(num, end=' + ')
        num += 1

print(f"{total}입니다.")