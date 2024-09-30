import json
import argparse

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
    parser = argparse.ArgumentParser(description='Generate TradingView list from Binance pairs data')
    parser.add_argument('-input', type=str, required=True, help='Input JSON file containing Binance pairs data')
    parser.add_argument('-output', type=str, required=True, help='Output file for the TradingView list')
    
    args = parser.parse_args()

    # Call the function with provided arguments
    generate_tradingview_list(args.input, args.output)

if __name__ == "__main__":
    main()
