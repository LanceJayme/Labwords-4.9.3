import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

from currency_api import get_exchange_rate, get_historical_rates
from charts import show_historical_chart

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Currency Converter")

        # --- Input Area ---
        self.amount_label = ttk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry = ttk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.from_currency_label = ttk.Label(master, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.from_currency_entry = ttk.Entry(master)
        self.from_currency_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.to_currency_label = ttk.Label(master, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.to_currency_entry = ttk.Entry(master)
        self.to_currency_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.convert_button = ttk.Button(master, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # --- Output Area ---
        self.result_label = ttk.Label(master, text="Result:")
        self.result_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.result_value = ttk.Label(master, text="")
        self.result_value.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        # --- Feature Buttons ---
        self.history_button = ttk.Button(master, text="View History", command=self.open_history_dialog)
        self.history_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.multi_compare_button = ttk.Button(master, text="Multi-Currency Compare", command=self.open_multi_compare_dialog)
        self.multi_compare_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.travel_budget_button = ttk.Button(master, text="Travel Budget", command=self.open_travel_budget_dialog)
        self.travel_budget_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # self.set_alert_button = ttk.Button(master, text="Set Rate Alert", command=self.open_set_alert_dialog)
        # self.set_alert_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    def convert_currency(self):
        amount_str = self.amount_entry.get()
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()

        try:
            amount = float(amount_str)
            rate = get_exchange_rate(from_currency, to_currency)
            if rate is not None:
                converted_amount = amount * rate
                self.result_value.config(text=f"{converted_amount:.2f} {to_currency}")
            else:
                self.result_value.config(text="Error fetching exchange rate.")
        except ValueError:
            self.result_value.config(text="Invalid amount.")

    def open_history_dialog(self):
        dialog = HistoryDialog(self.master)
        self.master.wait_window(dialog.top)

    def open_multi_compare_dialog(self):
        dialog = MultiCompareDialog(self.master)
        self.master.wait_window(dialog.top)

    def open_travel_budget_dialog(self):
        dialog = TravelBudgetDialog(self.master)
        self.master.wait_window(dialog.top)

    # def open_set_alert_dialog(self):
    #     dialog = SetAlertsDialog(self.master)
    #     self.master.wait_window(dialog.top)

class HistoryDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("View Historical Rates")

        ttk.Label(self.top, text="Base Currency:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.base_entry = ttk.Entry(self.top)
        self.base_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.top, text="Target Currency:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.target_entry = ttk.Entry(self.top)
        self.target_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.top, text="Start Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.start_entry = ttk.Entry(self.top)
        self.start_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.top, text="End Date (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.end_entry = ttk.Entry(self.top)
        self.end_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.top, text="Show Chart", command=self.show_chart).grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def show_chart(self):
        base_currency = self.base_entry.get()
        target_currency = self.target_entry.get()
        start_date = self.start_entry.get()
        end_date = self.end_entry.get()

        if base_currency and target_currency and start_date and end_date:
            show_historical_chart(base_currency, target_currency, start_date, end_date)
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

class MultiCompareDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Multi-Currency Comparison")

        ttk.Label(self.top, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry = ttk.Entry(self.top)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.top, text="Base Currency:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.base_entry = ttk.Entry(self.top)
        self.base_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.top, text="Target Currencies (comma-separated):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.targets_entry = ttk.Entry(self.top)
        self.targets_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.result_text = tk.Text(self.top, height=5, width=30)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.result_text.config(state=tk.DISABLED)

        ttk.Button(self.top, text="Compare", command=self.compare_currencies).grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def compare_currencies(self):
        amount_str = self.amount_entry.get()
        base_currency = self.base_entry.get().upper()
        targets_str = self.targets_entry.get().upper()
        target_currencies = [curr.strip() for curr in targets_str.split(',')]

        try:
            amount = float(amount_str)
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            for target in target_currencies:
                if base_currency and target:
                    rate = get_exchange_rate(base_currency, target)
                    if rate is not None:
                        converted_amount = amount * rate
                        self.result_text.insert(tk.END, f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target}\n")
                    else:
                        self.result_text.insert(tk.END, f"Error fetching rate for {base_currency} to {target}\n")
            self.result_text.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")

class TravelBudgetDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Travel Budget Conversion")

        ttk.Label(self.top, text="Budget Amount:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.budget_entry = ttk.Entry(self.top)
        self.budget_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.top, text="Home Currency:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.home_currency_entry = ttk.Entry(self.top)
        self.home_currency_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.top, text="Destination Currency:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.dest_currency_entry = ttk.Entry(self.top)
        self.dest_currency_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.result_label = ttk.Label(self.top, text="Estimated Budget in Destination Currency:")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        self.budget_result_value = ttk.Label(self.top, text="")
        self.budget_result_value.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        ttk.Button(self.top, text="Calculate", command=self.calculate_budget).grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def calculate_budget(self):
        budget_str = self.budget_entry.get()
        home_currency = self.home_currency_entry.get().upper()
        dest_currency = self.dest_currency_entry.get().upper()

        try:
            budget = float(budget_str)
            if home_currency and dest_currency:
                rate = get_exchange_rate(home_currency, dest_currency)
                if rate is not None:
                    converted_budget = budget * rate
                    self.budget_result_value.config(text=f"{converted_budget:.2f} {dest_currency}")
                else:
                    self.budget_result_value.config(text="Error fetching exchange rate.")
            else:
                messagebox.showerror("Error", "Please enter both home and destination currencies.")
        except ValueError:
            messagebox.showerror("Error", "Invalid budget amount.")

# class SetAlertsDialog:
#     def __init__(self, parent):
#         self.top = tk.Toplevel(parent)
#         self.top.title("Set Rate Change Alert")
#         # Implement UI elements for setting alerts (currency pair, thresholds)
#         pass

root = tk.Tk()
app = CurrencyConverterApp(root)
root.mainloop()