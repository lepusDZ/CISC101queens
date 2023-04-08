L1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
L2 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
L3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L4 = [[4, 9, 2], [3, 5, 5], [8, 1, 6]]

def main(hello):
    row1 = hello[0][0] + hello[0][1] + hello[0][2]
    row2 = hello[1][0] + hello[1][1] + hello[1][2]
    row3 = hello[2][0] + hello[2][1] + hello[2][2]
    col1 = hello[0][0] + hello[1][0] + hello[2][0]
    col2 = hello[0][1] + hello[1][1] + hello[2][1]
    col3 = hello[0][2] + hello[1][2] + hello[2][2]
    dia1 = hello[0][0] + hello[1][1] + hello[2][2]
    dia2 = hello[0][2] + hello[1][1] + hello[2][0]
    
    if row1 == row2 and row2 == row3:
        if col1 == col2 and col2 == col3:
            if dia1 == dia2:
                return True
    else:
        return False
        
print(main(L1))
print(main(L2))
print(main(L3))
print(main(L4))