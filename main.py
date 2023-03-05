with open("my_file.txt", mode="rw") as file:
    file.write("\nI am studying python.")
    contents = file.read()
    print(contents)