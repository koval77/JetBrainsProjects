def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Who for you is Donald Trump?")
    print("1. Just Tramp")
    print("2. Russian operative")
    print("3. Neonazi symphatiser")
    print("4. Rapist")
    print("5. Moron")
    print("6. Lier")
    print("7. Megalomaniac")
    print("8. Conman")
    print("9. All above")
    answer=input()
    while answer != "9":
        answer=input()
        check_quiz()
    print('Completed, have a nice day!')

def check_quiz():
    print("Please, try again.")
    
def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
# ...
test()
end()
