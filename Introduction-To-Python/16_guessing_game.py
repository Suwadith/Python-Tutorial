secret_value = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_input = int(input('Guess: '))
    guess_count += 1
    if user_input == secret_value:
        print('You win!')
        break
else:
    print('Sorry, you failed!')
