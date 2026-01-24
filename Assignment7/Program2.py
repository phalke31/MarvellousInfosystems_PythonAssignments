"""2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers."""

CheckEven = lambda No : (No % 2 == 0)

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Actula data is : ", Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filter : ", FData)

if __name__ == "__main__":
    main()


# ---------------------------------------------------------
# CheckEven = lambda No : (No % 2 == 0)

# def main():
#     Data = [1,2,3,4,5,6,7,8,9,10]
#     print("Actula data is : ", Data)

#     FData = filter(CheckEven, Data)
#     print("Data after filter : ", list(FData))

# if __name__ == "__main__":
#     main()


