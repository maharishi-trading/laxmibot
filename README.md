# LaxmiBot
![Icon for Laxmi Bot.png](resources%2FIcon%20for%20Laxmi%20Bot.png)
LaxmiBot is a bot that automatically buys and sells crytpo on multiple exchanges.

## Requirements
- Python 3.6+
- Anaconda 3
## Installation
1. Clone this repository.
2. Install the required packages.
3. create a new conda environment. 
```conda create --name laxmibot python=3.8```
4. Activate the environment.
```conda activate laxmibot```
5. Install the required packages.
```conda env create -f environment.yml```
add new packages to environment.yml if you install new packages.

## Scoring table for Exchanges selection
| Feature               | Points    | Bitstamp                                                                  | Coinbase                                                                 | crypto.com                                                                  | Kraken                                                                  | CEX.io |
|-----------------------|-----------|---------------------------------------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|--------|
| Reserves Data         | MANDATORY | [yes](https://www.geckoterminal.com/proof_of_reserves/exchanges/bitstamp) | [yes](https://investor.coinbase.com/financials/sec-filings/default.aspx) | [yes](https://www.geckoterminal.com/proof_of_reserves/exchanges/crypto_com) | [yes](https://www.geckoterminal.com/proof_of_reserves/exchanges/kraken) | NO     |
| No Tax Haven          | 10 points | 10                                                                        | 10                                                                       | 0                                                                           | 10                                                                      |        |
| EU Residency          | 10 points | 10                                                                        | 0                                                                        | 10                                                                          | 0                                                                       | 10
| No Technical problems | MANDATORY | OK                                                                        | New API key format not clear                                             | Sign-Up process brittle.                                                    | OK                                                                      |
| Lindy Effect          | 10 points | 10                                                                        | 10                                                                       | 3                                                                           | 10                                                                      | 10     |
## Trading fees table
reasonable worst case fees are:

| Exchange     | Maker   | Taker   |
|--------------|---------|---------|
| Bitstamp     | 0.30%   | 0.40%   |
| ~~Coinbase~~ | 0.5%    | 0.5%    | 
| ~~Crypto.com~~   | 0.16%   | 0.26%   |
| Kraken       | 0.16%   | 0.26%   |
| ~~CEX.io~~       | 0.15%   | 0.25%   |
| _Average_    | _0.23%_ | _0.33%_ |

### Bitstamp Requirements
"Minimum order size is 10 EUR."

