import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        # Length entry
        self.label = tk.Label(root, text="Enter password length:")
        self.label.pack(pady=10)
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=10)
        
        #complexity check
        self.include_letters = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special_chars = tk.BooleanVar(value=True)
        
        self.letters_checkbox = tk.Checkbutton(root, text="Include Letters", variable=self.include_letters)
        self.letters_checkbox.pack()
        
        self.digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=self.include_digits)
        self.digits_checkbox.pack()
        
        self.special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special_chars)
        self.special_chars_checkbox.pack()
        
        #submiyt btn
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        # Result 
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                self.result_label.config(text="Please enter a positive number.")
                return
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a numeric value.")
            return
        
        letters = string.ascii_letters if self.include_letters.get() else ""
        digits = string.digits if self.include_digits.get() else ""
        special_chars = string.punctuation if self.include_special_chars.get() else ""
        all_chars = letters + digits + special_chars
        
        if not all_chars:
            self.result_label.config(text="Please select at least one character set.")
            return
        
        password = ''.join(random.choice(all_chars) for _ in range(length))
        self.result_label.config(text=f"Generated Password: {password}")

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
