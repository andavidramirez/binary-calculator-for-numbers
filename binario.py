def run():
    try:
        CONSTANT = 2
        list = []
        number = int(input(("Enter a number:  ")))
        if number == 1:
            print("1 in binary system is: 1")
        else:   
            assert number > 0, "You should enter a positive number"
            result1 = number // CONSTANT
            result2 = number % CONSTANT
            if result1 <= 1:
                    list.append(result2)
                    list.append(result1)
                    list = list[::-1]
                    print(str(number) + " in binary system is:")
                    print(*list, sep="")
            while result1 > 1:
                list.append(result2)
                result2 = result1 % CONSTANT
                result1 = result1 // CONSTANT
                if result1 < 2:
                    list.append(result2)
                    list.append(result1)
                    list = list[::-1]
                    print(str(number) + " in binary system is:")
                    print(*list, sep="")
                    continue
    except ValueError:
        print("you should enter a natural number")
if __name__ == "__main__":
    run()


