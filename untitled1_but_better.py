import tkinter as tk

class ProfitAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Profit Analysis App")

        self.profit_data = {
            "January": 10000,
            "February": 12000,
            "March": 8000,
            "April": 15000,
            "May": 20000,
            "June": 18000,
            "July": 12000,
            "August": 25000,
            "September": 30000,
            "October": 18000,
            "November": 22000,
            "December": 28000,
        }

        self.max_profit_label = tk.Label(root, text="Max Profit:")
        self.max_profit_display = tk.Label(root, text="")

        self.min_profit_label = tk.Label(root, text="Min Profit:")
        self.min_profit_display = tk.Label(root, text="")

        self.analyze_button = tk.Button(root, text="Analyze Profits", command=self.analyze_profits)

        # Grid layout
        self.max_profit_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.max_profit_display.grid(row=0, column=1, padx=10, pady=10)

        self.min_profit_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.min_profit_display.grid(row=1, column=1, padx=10, pady=10)

        self.analyze_button.grid(row=2, column=0, columnspan=2, pady=10)

    def analyze_profits(self):
        max_profit_month = max(self.profit_data, key=self.profit_data.get)
        max_profit_value = self.profit_data[max_profit_month]

        min_profit_month = min(self.profit_data, key=self.profit_data.get)
        min_profit_value = self.profit_data[min_profit_month]

        self.max_profit_display.config(text=f"{max_profit_month}: ${max_profit_value}")
        self.min_profit_display.config(text=f"{min_profit_month}: ${min_profit_value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfitAnalysisApp(root)
    root.mainloop()
