# pip install requests
import requests

# Define constants for the API URL and your API key
API_URL = "https://api.exchangerate-api.com/v4/latest"  # using a public API for example
BASE_CURRENCY = "USD"  # Base currency for conversion

# Available currencies supported by the converter
supported_currencies = ["USD", "INR", "EUR", "JPY", "AUD", "CAD", "CHF", "GBP", "PLN", "RUB", "CNY"]

def get_exchange_rates(base_currency):
    """Fetch the latest exchange rates from the API."""
    response = requests.get(f"{API_URL}/{base_currency}")
    if response.status_code != 200:
        raise Exception("Error fetching data from the API.")
    return response.json()["rates"]

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """Convert amount from one currency to another using exchange rates."""
    if from_currency != BASE_CURRENCY:
        # Convert from the base currency to other currency
        amount = amount / exchange_rates[from_currency]
    
    # Convert to the target currency
    converted_amount = amount * exchange_rates[to_currency]
    return converted_amount

def main():
    """Main function for currency conversion."""
    # Get the exchange rates relative to the base currency
    exchange_rates = get_exchange_rates(BASE_CURRENCY)
    
    print("Available currencies for conversion:")
    print(", ".join(supported_currencies))

    # User input for conversion
    amount = float(input("Enter the amount to convert: "))
    from_currency = input(f"Convert from (choose one: {', '.join(supported_currencies)}): ").strip().upper()
    to_currency = input(f"Convert to (choose one: {', '.join(supported_currencies)}): ").strip().upper()

    if from_currency not in supported_currencies or to_currency not in supported_currencies:
        print("Invalid currency selection.")
        return

    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()