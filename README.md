Please :star: if you've found the project interesting and/or helpful.

# Nasdaq Net New Highs/Lows

This project is based on concepts in [US Markets Net New Highs/Lows](https://www.tradingview.com/script/eP814cAv-US-Markets-Net-New-Highs-Lows/) indicator on TradingView, a project that I worked on with professional trader [Matt Caruso](https://carusoinsights.com/charting). Tracking net highs and lows on the Nasdaq can be helpful to gauge if momentum in tech stocks is on one direction or the other.

In the indicator above, the data to determine the net highs and lows is based on the TradingView symbols: HIGQ (new highs) and LOWQ (new lows). 

Although an indicator is a very effective way to visualize the trend of net highs/lows, I was curious if it was possible to scan the symbols in the Nasdaq and generate a list of net highs and lows by looking at the data for each symbol rather than using a symbol such as HIGQ that does the heavy lifting.


## The Process

At the highest level, here are the steps used to determine the net highs/low:

+ Download list of all symbols in the Nasdaq
+ Filter the list using the following criteria:
   + Is the symbol an equity (not an ETF, SPAC, etc)
   + Is the last close > $2
   + Is the price * volume > 10,000

These criteria are similar to the filter used by Barchart.com for determining net highs/low: [HIGQ](https://www.barchart.com/stocks/quotes/$HIGQ/overview) [LOWQ](https://www.barchart.com/stocks/quotes/$LOWQ/overview)

## Install Python Requirements

```bash
pip install -r requirements
```

## Usage

```bash
$ python main.py -s
```

**Note:**  
Using the **```-s```** option will force the app to use a pre-configured list of Nasdaq symbols which has 200 symbols versus the downloaded master list which includes over 4,500 symbols. To download/process all the symbols, remove the command line option.

I've added the **```-s```** option so you can see the process in action without having to wait for all symbols to be filtered and verified for new highs/lows.

## Output

At the current time, the output is very basic, simply the highs/lows and net using a print() statement, similar to the following.

```
New highs: 3
New lows: 2
Net highs/lows: 1
```

## Unit Tests using Pytest

For completeness, there are unit tests for several of the functions that live in ```functions.py```. Run the tests as follows:

```bash
$ pytest
```

## Acknowledgements

Many thanks to the following:

[Robot Reichel](https://github.com/rreichel3) for the [Nasdaq symbol lists](https://github.com/rreichel3/US-Stock-Symbols).

[Doug Guthrie](https://github.com/dpguthrie) for the amazing [yahooquery](https://github.com/dpguthrie/yahooquery) wrapper for Python.

## Important Note

Although this project will determine the net highs/lows, given there are 4500+ stocks on the Nasdaq, it can be quite slow to run, as there is a call for each symbol to Yahoo Finance to retreive data.

This project is more of an exercise to see what it would take to build a net highs/lows script in Python versus a tool recommended for daily use.

## TradingView Projects

If you're interested in trading/investing, in addition to the indicator mentioned previously, I've written many indicators, both open/closed source that might be of interest:
[TradingView Indicators](https://www.tradingview.com/u/JohnMuchow/#published-scripts).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.