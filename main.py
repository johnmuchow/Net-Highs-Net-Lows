import os
import sys
import functions as f
from yahooquery import Ticker

# Setup file paths
nasdaq_master_path = os.path.join('data', 'nasdaq-master.txt')
nasdaq_master_path_limited = os.path.join('data', 'nasdaq-master-limited.txt')
nasdaq_qualified_list_path = os.path.join('data', 'nasdaq_qualified_list.txt')

# Lists of net highs and lows
nasdaq_new_highs = []
nasdaq_new_lows = []


#--------------------------------------------------------------------------------------
# filter_by_requirements()
#
# Process all the symbols in the downloaded file, creating a list of symbols that meet
# the requirements. Write the new list to a new file.
#--------------------------------------------------------------------------------------
def filter_by_requirements(path):

    """
    Process all of the downloaded nasdaq symbols, filtering by the required criteria and
    writing symbols meeting the criteria to a new file.

    Parameters:
        path(string): file path to nasdaq symbols

    Returns:
        None
    """

    # List of nasdaq symbols that meet criteria
    tmp_list = []

    with open(path, 'r') as tmp:
        x = 1
        for line in tmp:

            # process the row data
            symbol_name = line.strip()
            ticker_data = Ticker(symbol_name)

            # Is the symbol an 'equity' vs ETF, c
            t1 = f.is_symbol_equity(symbol_name, ticker_data)

            # Is close > $2
            t2 = f.is_last_close_greater_than_min(symbol_name, ticker_data, 2)

            # Is price * volume > 10,000
            t3 = f.is_price_volume_greater_than_min(symbol_name, ticker_data, 10000)

            print(f'processing row {x}: {symbol_name}')        
            x += 1

            if (t1 and t2 and t3):
                tmp_list.append(symbol_name)

    # Write the filtered list to file
    #os.remove(nasdaq_qualified_list_path)    # Remove the previous version if one exists
    if (len(tmp_list) > 0):
        with open(nasdaq_qualified_list_path, 'w') as file:
            for item in tmp_list:
                file.write("%s\n" % item)


#--------------------------------------------------------------------------------------
# create_new_high_low_lists()
#
# Process all the symbols in the nasdaq subset list, appending those symbols that are
# either net highs or lows to the relevant list.
#--------------------------------------------------------------------------------------
def create_new_high_low_lists():

    """
    Process all the symbols in the nasdaq subset list, appending those symbols that are
    either net highs or lows to the relevant list.

    Parameters:
        None

    Returns:
        None
    """

    with open(nasdaq_qualified_list_path, 'r') as file:

        for symbol_name in file:

            symbol_name = symbol_name.strip()
            ticker_data = Ticker(symbol_name)

            print(f'processing symbol {symbol_name}')        

            if (f.is_new_net_high(symbol_name, ticker_data)):
                nasdaq_new_highs.append(symbol_name)
            elif (f.is_new_net_low(symbol_name, ticker_data)):
                nasdaq_new_lows.append(symbol_name)



#--------------------------------------------------------------------------------------
def main(path):

    # Download nasdaq symbol data
    f.download_nasdaq_symbols(nasdaq_master_path)

    # Filter the downloaded list - uncomment first list for testing subset of list above
    filter_by_requirements(path)

    # Create the new high low lists
    create_new_high_low_lists()

    # Print summary
    highs = len(nasdaq_new_highs)
    lows = len(nasdaq_new_lows)
    print(f'New highs: {highs}')
    print(f'New lows: {lows}')
    print(f'Net highs/lows: {highs - lows}')



if __name__ == "__main__":

    # If -s option, used the pre-built, limited length list of nasdaq symbols
    if (len(sys.argv) > 1) and (sys.argv[1] == '-s') or (sys.argv[1] == '/s'):
        main(nasdaq_master_path_limited)
    else:
        main(nasdaq_master_path)
