def show_array(seat, row, col):
    for r in range(0, row):
        print(f"{r+1:.2d}", end=" ")
        for c in range(0, col):
            if (seat[r][c]==0):
                print("□", end=" ")
            else:
                print("■", end=" ")

print("2차원 배열을 만들어 0으로 초기화 합니다.")
row = int(input("행: "))
col = int(input("열: "))

data = [[0 * col for _ in range(row)]]

show_array(data, row, col)