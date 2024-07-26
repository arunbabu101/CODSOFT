import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        
        self.user_choice = ""
        self.computer_choice = ""
        
        self.result_text = tk.StringVar()
        
        self.user_score = 0
        self.computer_score = 0
        
        # Instructions label
        self.instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.instruction_label.pack(pady=10)
        
        # Button for choices
        self.rock_button = tk.Button(root, text="Rock", width=10, command=lambda: self.user_select("rock"))
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(root, text="Paper", width=10, command=lambda: self.user_select("paper"))
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: self.user_select("scissors"))
        self.scissors_button.pack(pady=5)
        
        # Displa choices
        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack(pady=20)
        
        self.user_choice_label = tk.Label(self.choices_frame, text="Your Choice: ")
        self.user_choice_label.grid(row=0, column=0, padx=10)
        
        self.computer_choice_label = tk.Label(self.choices_frame, text="Computer's Choice: ")
        self.computer_choice_label.grid(row=1, column=0, padx=10)
        
        self.user_choice_display = tk.Label(self.choices_frame, text="")
        self.user_choice_display.grid(row=0, column=1, padx=10)
        
        self.computer_choice_display = tk.Label(self.choices_frame, text="")
        self.computer_choice_display.grid(row=1, column=1, padx=10)
        
        # Result display
        self.result_label = tk.Label(root, textvariable=self.result_text, font=('Arial', 14, 'bold'), fg="blue")
        self.result_label.pack(pady=20)
        
        # Score display 
        self.score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=('Arial', 12))
        self.score_label.pack(pady=10)
        
        # Play again
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)
        
        # calling resett function
        self.reset_game()
    
    def user_select(self, choice):
        self.user_choice = choice
        self.user_choice_display.config(text=choice.capitalize())
        self.computer_choice = random.choice(["rock", "paper", "scissors"])
        self.computer_choice_display.config(text=self.computer_choice.capitalize())
        self.determine_winner()
    
    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            self.result_text.set("It's a tie!")
        elif (self.user_choice == "rock" and self.computer_choice == "scissors") or \
             (self.user_choice == "paper" and self.computer_choice == "rock") or \
             (self.user_choice == "scissors" and self.computer_choice == "paper"):
            self.result_text.set("You win!")
            self.user_score += 1
        else:
            self.result_text.set("Computer wins!")
            self.computer_score += 1
        
        # Updation scor
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")
    
    def reset_game(self):
        self.user_choice = ""
        self.computer_choice = ""
        self.user_choice_display.config(text="")
        self.computer_choice_display.config(text="")
        self.result_text.set("")
        self.score_label.config(text="Score: You 0 - 0 Computer")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
