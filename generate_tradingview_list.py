import json
import argparse
import requests

# Download Binance data and save it to a JSON file
def download_binance_data(output_file):
    url = 'https://api.binance.com/api/v3/exchangeInfo'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Binance exchange info saved to {output_file}")
    else:
        print(f"Failed to retrieve Binance data. Status code: {response.status_code}")

# Load the Binance data from a JSON file and generate the TradingView list
def generate_tradingview_list(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Filter for USDT spot pairs and exclude those with status "BREAK"
    usdt_spot_pairs_active = [symbol['symbol'] for symbol in data['symbols'] 
                              if symbol['quoteAsset'] == 'USDT' 
                              and symbol['isSpotTradingAllowed'] 
                              and symbol['status'] != 'BREAK']

    # Prepare the list in TradingView format
    tradingview_list_active = [f"BINANCE:{pair}" for pair in usdt_spot_pairs_active]

    # Write the TradingView list to a file
    with open(output_file, 'w') as f:
        for pair in tradingview_list_active:
            f.write(pair + '\n')

    print(f"TradingView list generated and saved to {output_file}")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Download Binance data and generate TradingView list')
    parser.add_argument('-download', action='store_true', help='Download Binance exchangeInfo and save to JSON')
    parser.add_argument('-input', type=str, help='Input JSON file containing Binance pairs data')
    parser.add_argument('-output', type=str, required=True, help='Output file for the TradingView list')
    
    args = parser.parse_args()

    if args.download:
        # Download the Binance data
        download_binance_data(args.input)

    # Call the function with provided arguments to generate TradingView list
    generate_tradingview_list(args.input, args.output)

if __name__ == "__main__":
    main()
