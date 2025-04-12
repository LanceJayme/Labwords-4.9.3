
import tkinter as tk
from tkinter import messagebox

def show_notification(title, message):
    """
    Displays a simple pop-up notification.
    """
    root = tk.Tk()
    root.withdraw() 
    messagebox.showinfo(title, message)
    root.destroy()

def check_rate_threshold(current_rate, threshold, currency_pair):
    """
    Checks if the current rate has crossed the threshold.
    """
    if current_rate > threshold:
        show_notification("Rate Alert!", f"The exchange rate for {currency_pair} has exceeded {threshold:.2f}")
    elif current_rate < threshold:
import tkinter as tk
from tkinter import messagebox

def show_notification(title, message):
    """
    Displays a simple pop-up notification.
    """
    root = tk.Tk()
    root.withdraw()  
    messagebox.showinfo(title, message)
    root.destroy()

def check_rate_threshold(current_rate, threshold, currency_pair):
    """
    Checks if the current rate has crossed the threshold.
    """
    if current_rate > threshold:
        show_notification("Rate Alert!", f"The exchange rate for {currency_pair} has exceeded {threshold:.2f}")
    elif current_rate < threshold:
        show_notification("Rate Alert!", f"The exchange rate for {currency_pair} has fallen below {threshold:.2f}")

if __name__ == '__main__':
       print("Notification functionality to be integrated into the main app.")
        show_notification("Rate Alert!", f"The exchange rate for {currency_pair} has fallen below {threshold:.2f}")

if __name__ == '__main__':
       print("Notification functionality to be integrated into the main app.")