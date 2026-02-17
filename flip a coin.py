import random
import time

def display_title():
    """Display the game title"""
    print("\n" + "="*40)
    print("       COIN FLIP GAME")
    print("="*40 + "\n")

def get_player_choice():
    """Get the player's coin flip choice"""
    while True:
        choice = input("Choose HEADS or TAILS: ").strip().upper()
        if choice in ["HEADS", "TAILS"]:
            return choice
        print("Invalid choice! Please enter HEADS or TAILS.")

def flip_coin():
    """Flip the coin and return the result"""
    return random.choice(["HEADS", "TAILS"])

def display_flip_animation():
    """Show a simple flip animation"""
    print("\nFlipping coin", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

def play_round():
    """Play a single round of the game"""
    player_choice = get_player_choice()
    display_flip_animation()
    
    result = flip_coin()
    print(f"Result: {result}")
    
    if player_choice == result:
        print("\nyou won bro")
        return True
    else:
        print(f"\nyou lost bozo")
        return False

def display_stats(wins, losses):
    """Display the game statistics"""
    print("\n" + "="*40)
    print("         GAME STATISTICS")
    print("="*40)
    print(f"Wins:  {wins}")
    print(f"Losses: {losses}")
    total = wins + losses
    if total > 0:
        win_rate = (wins / total) * 100
        print(f"Win Rate: {win_rate:.1f}%")
    print("="*40 + "\n")

def main():
    """Main game loop"""
    display_title()
    wins = 0
    losses = 0
    
    while True:
        result = play_round()
        if result:
            wins += 1
        else:
            losses += 1
        
        play_again = input("\nPlay again? (YES/NO): ").strip().upper()
        if play_again != "YES":
            break
        print("\n")
    
    display_stats(wins, losses)
    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
