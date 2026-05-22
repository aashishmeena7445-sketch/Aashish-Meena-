while True:
    print("\n----- MENU -----")
    print("1. Print numbers from 1 to 10")
    print("2. Addition of first 10 numbers")
    print("3. Multiplication table")
    print("4. Factorial of a number")
    print("5. Print even numbers from 1 to 20")
    print("6. Print Hello using while loop")
    print("7. Reverse a number")
    print("8. Star pattern")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(1, 11):
            print(i)

    elif choice == 2:
        total = 0
        for i in range(1, 11):
            total += i
        print("Sum =", total)

    elif choice == 3:
        num = int(input("Enter a number: "))
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    elif choice == 4:
        num = int(input("Enter a number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print("Factorial =", fact)

    elif choice == 5:
        for i in range(1, 21):
            if i % 2 == 0:
                print(i)

    elif choice == 6:
        i = 1
        while i <= 5:
            print("Hello")
            i += 1

    elif choice == 7:
        num = int(input("Enter number: "))
        rev = 0

        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10

        print("Reverse =", rev)

    elif choice == 8:
        for i in range(1, 6):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == 9:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
