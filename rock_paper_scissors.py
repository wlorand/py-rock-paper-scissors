from random import randint


def main():
    # institute a play loop
    play_again = ''
    while play_again.upper() != 'N':
        play()
        print('Do You Want to Play Again? ')
        play_again = input('type "y" for Yes, "n" for No: ')


def play():
    print('''
    --------------------------------
    Welcome to Rock, Paper, Scissors.
    Please pick your weapon...
    ''')
    options_list = ['Rock', 'Paper', 'Scissors']  # TODO: try as tuple
    player_weapon = get_player_choice(options_list)
    computer_weapon = computer_choice(options_list)
    print(
        f'(player picks {options_list[player_weapon]}, computer picks {options_list[computer_weapon]})')
    print('----------------------------------------------')
    check_results(options_list, player_weapon, computer_weapon)
    print('----------------------------------------------')


def get_player_choice(options):
    valid_choices = []
    for i, option in enumerate(options):
        print(f'{i}={option}')
        valid_choices.append(i)
    user_input = int(input('Choose Your Weapon by Entering its Number: '))
    if str(user_input).isnumeric() and user_input in valid_choices:
        return user_input
    else:
        print('Please enter a valid choice')
        get_player_choice(options)


def computer_choice(options):
    '''generate and return random int from options list'''
    # print(computer_choice.__doc__)
    return randint(0, len(options)-1)


def check_results(options, player_result, computer_result):
    if player_result == computer_result:
        print(
            f'TIE GAME, both player and computer picked {options[player_result]}')
    # strength cycle logic outlier: first option (rock) is stronger than last one (scissors)
    elif (player_result == 0 and computer_result == len(options) - 1):
        print(
            f'PLAYER WINS as {options[player_result]} crushes {options[computer_result]}')
    # strength cycle logic: items to the right are usually stronger
    elif (player_result > computer_result and not(player_result == len(options) - 1 and computer_result == 0)):
        print(
            f'PLAYER WINS as {options[player_result]} beats {options[computer_result]}')
    else:
        print(
            f'COMPUTER WINS as {options[computer_result]} beats {options[player_result]}')


if __name__ == "__main__":
    main()
