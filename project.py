import requests
import argparse
import csv
from datetime import datetime
import os
import sys
#function for testing only( no real use)
def extract_rate(currency, rates_dict):
    rate = rates_dict.get(currency)
    return rate

def clean_currency(currency):
    return currency.strip().upper()

def validate_currency(currency, rates_dict):
    return currency in rates_dict




def open_csv(base_currency, target_currency, rate):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exist = True
    if not os.path.exists("market_data.csv"):
        file_exist = False

    with open("market_data.csv", "a", newline="") as file:
        writer = csv.writer(file)   
        #if csv does not exist, create it and write the header
        if file_exist == False:            
            writer.writerow(["Timestamp", "Base", "Target", "Rate"])
        #csv already exists         
        writer.writerow([current_time, base_currency, target_currency, rate])
        file_exist = True

def get_target_currency():
    p = argparse.ArgumentParser()
    p.add_argument("-t", "--target", default="THB")
    a = p.parse_args()
    
    target_currency = a.target.upper()

    return target_currency

def get_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"]    
    else:
        sys.exit(f"Failed to connect. Error code: {response.status_code}")
    return rate


def main():
 
    target_currency = get_target_currency()
    rates = get_rates()

    if target_currency in rates:
        base_currency = "USD"
        rate = extract_rate(target_currency, rates)
        
        print("--- Live Market Briefing ---")
        print(f"Base Currency: 1 USD")
        print(f"Target ({target_currency}): {rate:.2f}")
        print("----------------------------")
        
        #Save the data to a CSV file
        open_csv(base_currency, target_currency, rate)
    else:
        sys.exit(f"Error: The currency '{target_currency}' doesn't exist in the database.")
        



if __name__ == "__main__":
    main()

    