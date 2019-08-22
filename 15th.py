def freq(str):
    list1 = str.split()
    words = set(list1)
    for i in words:
        print("Frequency of ", i, "is : ", list1.count(i))


if __name__ == "__main__":
    str = input("enter sentance : ")
    freq(str)