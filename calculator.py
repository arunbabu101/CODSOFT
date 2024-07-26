import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        
        self.equation = tk.StringVar()
        self.entry_value = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        # displayi the input and outputekotak
        entry = tk.Entry(self.root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        #digit buttons
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row = 1
        col = 0
        for button_text in button_texts:
            button = tk.Button(self.root, text=button_text, padx=20, pady=20, font=('Arial', 18), command=lambda txt=button_text: self.on_button_click(txt))
            button.grid(row=row, column=col, sticky="nsew")
            
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == 'C':
            self.entry_value = ""
        elif char == '=':
            try:
                self.entry_value = str(eval(self.entry_value))
            except Exception as e:
                self.entry_value = "Error"
        else:
            self.entry_value += str(char)
        
        self.equation.set(self.entry_value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
