import random
import os

# Word Database Module
class WordDatabase:
    def __init__(self):
        self.words = {
            "easy": [
                "planet", "flower", "laptop", "guitar", "banana", "bridge", "rocket",
                "pencil", "forest", "hammer", "orange", "pirate", "cookie", "friend",
                "kitten", "monkey", "castle", "candle", "butter", "peanut"
            ],
            "medium": [
                "orchard", "printer", "goblin", "sparrow", "helmet", "glacier", "anchor",
                "voyage", "chariot", "beetle", "sweater", "bicycle", "village", "dolphin",
                "phoenix", "lantern", "tundra", "walnut", "pyramid", "dagger"
            ],
            "hard": [
                "mountain", "calendar", "landmark", "sandwich", "universe", "mystical",
                "adventure", "terrible", "firewood", "syndrome", "umbrella", "champion",
                "question", "tropical", "wildfire", "aviation", "backpack", "drainage",
                "festival", "fortress"
            ],
        }

    def get_random_word(self, difficulty):
        return random.choice(self.words.get(difficulty, []))

# Game Logic Module
class GameLogic:
    def __init__(self, word):
        self.word = word
        self.hidden_word = ["_" for _ in word]
        self.attempts_left = 6
        self.guessed_letters = set()

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return "Already guessed."
        self.guessed_letters.add(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i] = letter
            return "Correct guess!"
        else:
            self.attempts_left -= 1
            return "Incorrect guess!"

    def is_game_over(self):
        return self.attempts_left <= 0 or "_" not in self.hidden_word

    def is_winner(self):
        return "_" not in self.hidden_word

    def get_game_state(self):
        return {
            "word_progress": " ".join(self.hidden_word),
            "attempts_left": self.attempts_left,
            "guessed_letters": self.guessed_letters,
        }

# Hangman Visuals
class HangmanVisual:
    STAGES = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           -----
           |   |
               |
               |
               |
               |
        ========="""
    ]

    def display(self, attempts_left):
        print(self.STAGES[6 - attempts_left])

# Score Tracking Module
class ScoreTracker:
    def __init__(self):
        self.score = 0

    def update_score(self, is_winner):
        if is_winner:
            self.score += 10
        else:
            self.score = 0
    def get_score(self):
        return self.score

# Leaderboard Module
class Leaderboard:
    FILE_PATH = "leaderboard.txt"

    def __init__(self):
        self.leaderboard = self.load_leaderboard()

    def load_leaderboard(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as file:
                lines = file.readlines()
                return [
                    {"name": line.split(":")[0].strip(), "score": int(line.split(":")[1].strip())}
                    for line in lines
                ]
        return []

    def save_leaderboard(self):
        with open(self.FILE_PATH, "w") as file:
            for entry in self.leaderboard:
                file.write(f"{entry['name']}:{entry['score']}\n")

    def update_leaderboard(self, player_name, score):
        self.leaderboard.append({"name": player_name, "score": score})
        self.save_leaderboard()

    def display_leaderboard(self):
        print("\nLeaderboard:")
        rank = 1
        for entry in self.leaderboard:
            print(f"{rank}. {entry['name']} - {entry['score']}")
            rank += 1

# Main Hangman Game
def hangman_game():
    print("Welcome to Hangman!")
    player_name = input("Enter your name: ").strip()

    valid_difficulties = ["easy", "medium", "hard"]
    difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()

    while difficulty not in valid_difficulties:
        print("Invalid difficulty selected. Please choose from: easy, medium, or hard.")
        difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()

    word_db = WordDatabase()
    word = word_db.get_random_word(difficulty)
    game_logic = GameLogic(word)
    hangman_visual = HangmanVisual()
    score_tracker = ScoreTracker()
    leaderboard = Leaderboard()

    print("\nLet's start the game!")

    while not game_logic.is_game_over():
        state = game_logic.get_game_state()
        hangman_visual.display(state["attempts_left"])
        print(f"\nWord: {state['word_progress']}")
        print(f"Attempts left: {state['attempts_left']}")
        print(f"Guessed letters: {', '.join(state['guessed_letters'])}")

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        result = game_logic.guess_letter(guess)
        print(result)

    if game_logic.is_winner():
        print("\nCongratulations! You guessed the word:", word)
        score_tracker.update_score(True)
    else:
        hangman_visual.display(0)
        print("\nGame Over! The word was:", word)
        score_tracker.update_score(False)

    score = score_tracker.get_score()
    print("Your score:", score)

    # Update leaderboard
    leaderboard.update_leaderboard(player_name, score)
    leaderboard.display_leaderboard()

if __name__ == "__main__":
    hangman_game()
