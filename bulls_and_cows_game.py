from random import choice


class SameNumbersError(Exception):
    pass


class WrongNumberLengthError(Exception):
    pass


def take_data():
    while True:

        try:
            tries = int(input('Please type the number of tries: '))
            length = int(input('Please type the length of the number: '))

        except ValueError:
            print('Error, player input must be a number. Please try again.')

        else:
            break

    return tries, length


def random_number_generator(length: int):
    generated_number = []
    n_range = [n for n in range(1, 10)]

    for i in range(length):
        random_number = choice(n_range)
        n_range.remove(random_number)

        generated_number.append(random_number)

        if i == 0:
            n_range.append(0)

    return generated_number


def matching_numbers(generated_number, current_player_numbers, n_length, current_turn):

    bulls = [generated_number[i] for i in range(len(generated_number)) if generated_number[i] == player_numbers[i]]
    cows = [n for n in generated_number if n in current_player_numbers and n not in bulls]

    bulls_length = len(bulls)
    cows_length = len(cows)

    if bulls_length != n_length:
        return f'{current_turn}: {bulls_length} bulls and {cows_length} cows.', False

    else:
        return f'{current_turn}: {bulls_length} bulls! You won!\nAnswer: {"".join(map(str, generated_number))}', True


n_tries, number_length = take_data()
comp_num = random_number_generator(number_length)
turn = 0
won = False

while n_tries != turn and not won:

    try:
        player_numbers = list(map(int, input(f'Please type {number_length} numbers.\n')))

        if len(player_numbers) != number_length:
            raise WrongNumberLengthError

        if len(set(player_numbers)) != number_length:
            raise SameNumbersError

        turn += 1

        message, won = matching_numbers(comp_num, player_numbers, number_length, turn)

        print(message)

    except ValueError:
        print('Error, player input must be a number. Please try again.')

    except SameNumbersError:
        print('Numbers must be different.')

    except WrongNumberLengthError:
        print(f'Numbers must be {number_length}.')

if not won:
    print(f'You lost. Better luck next time.\nAnswer: {"".join(map(str, comp_num))}')
