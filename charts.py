import matplotlib.pyplot as plt
from currency_api import get_historical_rates

def show_historical_chart(base_currency, target_currency, start_date, end_date):
    """
    Fetches historical exchange rates and displays a chart.
    """
    historical_data = get_historical_rates(base_currency, target_currency, start_date, end_date)
    if historical_data:
        dates = list(historical_data.keys())
        rates = list(historical_data.values())
        dates, rates = zip(*sorted(zip(dates, rates)))

        plt.figure(figsize=(10, 6))
        plt.plot(dates, rates, marker='o')
        plt.title(f'{base_currency.upper()} to {target_currency.upper()} Exchange Rate History')
        plt.xlabel('Date')
        plt.ylabel('Exchange Rate')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Could not fetch historical data for the chart.")

if __name__ == '__main__':
    show_historical_chart("USD", "EUR", "2024-03-01", "2024-03-31")