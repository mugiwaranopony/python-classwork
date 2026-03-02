# i = 3

# while i != 0:
#     print("meow")
#     i -= 1

   # i = i - 1
    


# i = 0

# while i <= 3:
#     print("meow")
#     i = i + 1


# i = 0

# while i < 3:
#     print("meow")
#     i = i + 1

#lst = [1, 2, 3]
#for i in range(3):
#for _ in range(3):
# for i in [0, 1, 2]:
#     print("meow")


# print("meow\n" * 3, end="")


# while True:
#     n = int(input("What's n? "))
#     if n <= 0:
#         continue
#     else:
#         break


# for _ in range(n):
#     print("meow")



# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    returned_value = get_number
    meow(returned_value)
    # meow(get_number())

def get_number():
    while True:
         n = int(input("What's n? "))
         if n >= 1:
             return n

def meow(n):
    for _ in range(n):
        print("meow")

main()