def play_game():
  while True:
    attempts += 1
    guess = get_player_guess()
    result = check_guess(secret_number, guess)
    if result == "correct":
      print(f"Congratulations! You guessed the number in {attempts} attempts.")
      break
    elif result == "high":
      print("Too high! Try again.")
    elif result == "low":
      print("Too low! Try again.")

if __name__ == "__main__":
    play_game()
