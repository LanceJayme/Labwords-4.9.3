import requests

API_KEY = "8bc3e91bed6981b6287ef919"  

def get_exchange_rate(from_currency, to_currency):
    api_key = API_KEY
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency.upper()}/{to_currency.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "result" in data and data["result"] == "success" and "conversion_rate" in data:
            return data["conversion_rate"]
        else:
            print(f"Error fetching rate for {from_currency}-{to_currency}: {data}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def get_historical_rates(base_currency, target_currency, start_date, end_date):
    """
    Fetches historical exchange rates for a given currency pair and date range.
    """
    api_key = API_KEY
    historical_data = {}
    try:
        from datetime import datetime, timedelta

        start = datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.strptime(end_date, '%Y-%m-%d').date()
        current_date = start

        while current_date <= end:
            year = current_date.year
            month = current_date.month
            day = current_date.day

            url = f"https://v6.exchangerate-api.com/v6/{api_key}/history/{base_currency.upper()}/{year}/{month}/{day}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "result" in data and data["result"] == "success" and "conversion_rates" in data and target_currency.upper() in data["conversion_rates"]:
                # The target currency rate is directly under 'conversion_rates'
                historical_data[current_date.strftime('%Y-%m-%d')] = data["conversion_rates"][target_currency.upper()]
            elif "result" in data and data["result"] == "error":
                print(f"Error fetching historical data for {base_currency} on {current_date}: {data['error-type']}")
            else:
                print(f"Error fetching historical data for {base_currency} on {current_date}: Unknown response")
                print("Raw API Response:", data)

            current_date += timedelta(days=1)

        return historical_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None

if __name__ == '__main__':
    rate = get_exchange_rate("USD", "PHP")
    if rate:
        print(f"1 USD is equal to {rate} PHP")

    historical = get_historical_rates("USD", "EUR", "2024-04-01", "2024-04-07")
    if historical:
        print("Historical USD to EUR rates:", historical)