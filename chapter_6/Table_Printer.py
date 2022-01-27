def printTable(table_data):
    col_widths = [0] * len(table_data)
    for row in range(len(table_data)):
        for data in table_data[row]:
            string_len = len(data) #checks to the length of each string each list
            if string_len > col_widths[row]:
                    col_widths[row] = string_len #returns the maximum string lenght to col_widths
    max_just = max(col_widths)

    for row in range(len(table_data[0])):
        for data in range(len(table_data)):
            print(table_data[data][row].rjust(max_just), end='')
        print()



printTable([['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']])





