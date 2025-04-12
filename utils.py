def format_currency(amount, currency_code):
    """
    Formats the amount with the currency code.
    """
    return f"{amount:.2f} {currency_code.upper()}"

if __name__ == '__main__':
    formatted_amount = format_currency(123.456, "EUR")
    print(formatted_amount)