import curses
import json
import os

# Path to the high scores JSON file
high_scores_file = 'high_scores.json'

# Initialize default high scores if the file doesn't exist
default_scores = []

# Load or initialize high scores
def load_high_scores():
    if os.path.exists(high_scores_file):
        with open(high_scores_file, 'r') as file:
            return json.load(file)
    else:
        with open(high_scores_file, 'w') as file:
            json.dump(default_scores, file)
        return default_scores

# Save updated high scores
def save_high_scores(scores):
    with open(high_scores_file, 'w') as file:
        json.dump(scores, file)

# Update high scores if eligible
def update_high_scores(new_score, new_name):
    scores = load_high_scores()
    scores.append({"name": new_name, "score": new_score})
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]
    save_high_scores(scores)

def display_scoreboard(stdscr, scores, selected_option):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    title = "High Scores"
    x_title = w // 2 - len(title) // 2
    stdscr.addstr(3, x_title, title)  # Position title a little higher (y = 3)

    # Calculate starting position for the scoreboard
    start_y = 5  # Start displaying scores from y = 5 (below the title)

    # Display each score in the list
    for idx, entry in enumerate(scores):
        score_text = f"{entry['name']}: {entry['score']}"
        x = w // 2 - len(score_text) // 2
        y = start_y + idx  # Positioning based on calculated start_y
        stdscr.addstr(y, x, score_text)

    # Menu options
    options = ["Play Again", "Main Menu", "Quit"]
    for i, option in enumerate(options):
        x = w // 2 - len(option) // 2
        y = start_y + len(scores) + 2 + i  # Position options just below the scoreboard
        if i == selected_option:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, option)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, option)

    stdscr.refresh()

def game_over_screen(stdscr, score):
    high_scores = load_high_scores()
    min_score = min([entry["score"] for entry in high_scores]) if high_scores else 0

    # Check if the score qualifies for high score
    if score > min_score:
        curses.echo()
        stdscr.addstr(5, 5, "New High Score! Enter your name: ")
        stdscr.addstr(6, 5, ">> ")
        name = stdscr.getstr(6, 8, 20).decode("utf-8")
        update_high_scores(score, name)
        curses.noecho()
    selected_option = 0
    while True:
        display_scoreboard(stdscr, load_high_scores(), selected_option)
        key = stdscr.getch()

        # Navigate the menu
        if key == curses.KEY_UP and selected_option > 0:
            selected_option -= 1
        elif key == curses.KEY_DOWN and selected_option < 2:
            selected_option += 1
        elif key in [10, 13]:  # Enter key
            if selected_option == 0:
                # Restart the game or call the function to play again
                break
            elif selected_option == 1:
                # Go back to main menu
                break
            elif selected_option == 2:
                # Quit the game
                exit()

# Main function for demonstration
def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Example game-over screen call with a sample score
    sample_score = 3600
    game_over_screen(stdscr, sample_score)

curses.wrapper(main)
