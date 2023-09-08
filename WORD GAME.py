import random
import tkinter as tk

# Function to generate a random grid of letters
def generate_grid(size):
    grid = []
    for _ in range(size):
        row = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(size)]
        grid.append(row)
    return grid

# Function to create a word list
def create_word_list():
    words = ["PYTHON", "JAVA", "CPLUSPLUS", "JAVASCRIPT", "RUBY", "HTML", "CSS", "VIDHI"]
    return words

# Function to hide words in the grid
def hide_words(grid, words):
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, len(grid) - 1)
            col = random.randint(0, len(grid) - len(word))
            for i in range(len(word)):
                grid[row][col + i] = word[i]
        else:
            row = random.randint(0, len(grid) - len(word))
            col = random.randint(0, len(grid) - 1)
            for i in range(len(word)):
                grid[row + i][col] = word[i]

# Function to play the word search game
def play_word_search():
    def check_guess():
        nonlocal found_words
        guess = entry.get().upper()
        entry.delete(0, 'end')
        if guess == 'QUIT':
            window.destroy()
        elif guess in words and guess not in found_words:
            found_words.append(guess)
            label_result.config(text=f"Found '{guess}'!")
            if len(found_words) == len(words):
                label_result.config(text="Congratulations! You found all the words.")
        else:
            label_result.config(text="Word not found. Try again.")
    
    grid_size = 10
    grid = generate_grid(grid_size)
    words = create_word_list()
    hide_words(grid, words)

    window = tk.Tk()
    window.title("Word Search Game")

    label_instruction = tk.Label(window, text="Find the following words:")
    label_instruction.pack()

    for word in words:
        label_word = tk.Label(window, text=word)
        label_word.pack()

    canvas = tk.Canvas(window, width=grid_size * 30, height=grid_size * 30)
    canvas.pack()

    for i in range(grid_size):
        for j in range(grid_size):
            canvas.create_text(i * 30 + 15, j * 30 + 15, text=grid[i][j])

    entry = tk.Entry(window, width=20)
    entry.pack()

    button_check = tk.Button(window, text="Check", command=check_guess)
    button_check.pack()

    label_result = tk.Label(window, text="")
    label_result.pack()

    found_words = []

    window.mainloop()

if __name__ == "__main__":
    play_word_search()
