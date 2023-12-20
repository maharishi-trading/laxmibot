# LaxmiBot
<img alt="Icon for Laxmi Bot.png" width="50" height="50" src="resources%2FIcon%20for%20Laxmi%20Bot.png" />
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
| Feature               | Points    | Bitstamp   | Coinbase   | crypto.com| Kraken      | CEX.io | Binance |
|-----------------------|-----------|------------|------------|------------|------------------------------|--------|---------|
| Reserves Data         | MANDATORY | [yes](https://www.geckoterminal.com/proof_of_reserves/exchanges/bitstamp) | [yes](https://investor.coinbase.com/financials/sec-filings/default.aspx) | [yes](https://www.geckoterminal.com/proof_of_reserves/exchanges/crypto_com) | [yes](https://www.geckoterminal.com/proof_of_reserves/exchanges/kraken) | NO     | NO      |
| No Tax Haven          | 10 points | 10         | 10         | 0          | 10         | 10     | 0    |
| EU License            | 10 points | 10         | 10 Bafin   | 10         | 0          | 10     | 0       |
| No Technical problems | MANDATORY | OK         | API key?   | Sign-Up?   | OK         | OK     | OK      |
| Lindy Effect          | 10 points | 10         | 10         | 3          | 10         | 10     | 5    |
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

### Volume Requirements
- Bitstamp: Minimum order size is 10 EUR.
- Kraken: 0.0001 BTC

## Requirements and Properties
- [x] **Homeostasis:** Withdrawing and depositing assets leads to investment reorganization automatically. For example: if you deposit 1000 EUR, the bot will automatically buy 1000 EUR worth of crypto if the signal is on buy. If you withdraw 0.01 BTC, the bot is in a well-defined state after the withdrawal.
- [x] **Crash resistance:** the bot will automatically buy options to hedge against a substantial crash of x% in t time.
- [x] **Counterparty risk mitigation:** the bot will always trade on N exchanges simultaneously to reduce insolvency risk.


