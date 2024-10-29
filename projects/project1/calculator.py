import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variable to store current calculation
        self.current = ""
        
        # Create display
        self.display = ttk.Entry(root, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^', 5, 2), ('←', 5, 3)
        ]
        
        # Create and place buttons
        for (text, row, col) in buttons:
            button = ttk.Button(root, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            
        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=3)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=3)
    
    def button_click(self, value):
        if value == '=':
            try:
                # Replace special operators
                expression = self.current.replace('^', '**').replace('√', 'math.sqrt')
                
                # Evaluate the expression
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Division by zero")
                self.current = ""
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current = ""
                
        elif value == 'C':
            self.current = ""
            self.display.delete(0, tk.END)
            
        elif value == '←':
            self.current = self.current[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
            
        elif value == '√':
            if self.current:
                try:
                    result = math.sqrt(float(self.current))
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                    self.current = str(result)
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Error")
                    self.current = ""
            else:
                self.current += "math.sqrt("
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.current)
                
        else:
            self.current += value
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
