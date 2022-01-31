def printTable(table_data):
    # find maximum string length as justification
    max_just = 0
    for i, _ in enumerate(table_data):
        for word in table_data[i]:
            if len(word) > max_just:
                max_just = len(word)

    for col, _ in enumerate(table_data[0]):
        for row, _ in enumerate(table_data):
            print(table_data[row][col].rjust(max_just), end="")
        print()


printTable(
    [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"],
    ]
)
