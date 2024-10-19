import curses

# Define menus
main_menu = ['Play', 'Settings', 'Scoreboard', 'Exit']
settings_menu = ['Audio', 'Graphics', 'Controls', 'Back']
play_menu = ['New Game', 'Load Game', 'Back']

# Fake scoreboard (name, score)
fake_scores = [
    ("Mario", 5000),
    ("Luigi", 4500),
    ("Peach", 4000),
    ("Bowser", 3500),
    ("Toad", 3000),
]

# Define a stack to handle navigation between menus
menu_stack = [main_menu]


def print_menu(stdscr, selected_row_idx, menu):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Print the "Dr Mario" title at the top
    title = "Dr Mario"
    x_title = w // 2 - len(title) // 2
    stdscr.addstr(1, x_title, title)

    # Print the menu below the title
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def draw_scoreboard(stdscr, scores):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Print the title "Scoreboard"
    title = "Scoreboard"
    x_title = w // 2 - len(title) // 2
    stdscr.addstr(1, x_title, title)

    # Print each player's name and score
    for idx, (name, score) in enumerate(scores):
        score_text = f"{name}: {score}"
        x = w // 2 - len(score_text) // 2
        y = h // 2 - len(scores) // 2 + idx
        stdscr.addstr(y, x, score_text)

    stdscr.refresh()
    stdscr.getch()  # Wait for user input before returning


def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Specify the current selected row
    current_row = 0

    # Get the current menu from the stack
    current_menu = menu_stack[-1]

    # Print the menu
    print_menu(stdscr, current_row, current_menu)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(current_menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected_option = current_menu[current_row]

            # Logic for navigating between menus
            if selected_option == 'Play':
                menu_stack.append(play_menu)
                current_row = 0
            elif selected_option == 'Settings':
                menu_stack.append(settings_menu)
                current_row = 0
            elif selected_option == 'Scoreboard':
                draw_scoreboard(stdscr, fake_scores)  # Call the scoreboard function
            elif selected_option == 'Back':
                if len(menu_stack) > 1:
                    menu_stack.pop()
                    current_row = 0
            elif selected_option == 'Exit':
                break

            # Update the current menu and display it
            current_menu = menu_stack[-1]

        # Reprint the menu
        print_menu(stdscr, current_row, current_menu)


curses.wrapper(main)
