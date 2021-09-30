def printTable(table_data):
    col_widths = [0] * len(table_data)
    for row in range(len(table_data)):
        for col in range(len(table_data[row])):
            string_len = len(table_data[row][col])
            if string_len > col_widths[row]:
                    col_widths[row] = string_len
    r_val = max(col_widths)
    for row in range(len(table_data[0])):
        for col in range(len(table_data)):
            print(table_data[col][row].rjust(r_val), sep='')
    print()



printTable([['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']])





