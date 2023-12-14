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

### Volume Requirements
- Bitstamp: Minimum order size is 10 EUR.
- Kraken: 0.0001 BTC

## Example results

- Current Prices 
```json 
{"kraken": 39414.8, "bitstamp": 39420.0}
```
- Orders 
```json 
{
    "bitstamp": {
        "amount": 0.0003,
        "average": null,
        "clientOrderId": null,
        "cost": null,
        "datetime": "2023-12-14T08:31:30.846Z",
        "fee": null,
        "fees": [],
        "filled": null,
        "id": "1694546805510145",
        "info": {
            "amount": "0.00030000",
            "datetime": "2023-12-14 08:31:30.846000",
            "id": "1694546805510145",
            "market": "BTC/EUR",
            "price": "39420",
            "type": "0"
        },
        "lastTradeTimestamp": null,
        "lastUpdateTimestamp": null,
        "postOnly": null,
        "price": 39420.0,
        "reduceOnly": null,
        "remaining": null,
        "side": "buy",
        "status": null,
        "stopLossPrice": null,
        "stopPrice": null,
        "symbol": "BTC/EUR",
        "takeProfitPrice": null,
        "timeInForce": null,
        "timestamp": 1702542690846,
        "trades": [],
        "triggerPrice": null,
        "type": "market"
    },
    "kraken": {
        "amount": 0.0003,
        "average": null,
        "clientOrderId": null,
        "cost": null,
        "datetime": null,
        "fee": null,
        "fees": [],
        "filled": null,
        "id": "OOT4Y3-OZ5HM-VCJG56",
        "info": {
            "descr": {
                "order": "buy 0.00030000 XBTEUR @ market"
            },
            "txid": [
                "OOT4Y3-OZ5HM-VCJG56"
            ]
        },
        "lastTradeTimestamp": null,
        "lastUpdateTimestamp": null,
        "postOnly": false,
        "price": null,
        "reduceOnly": null,
        "remaining": null,
        "side": "buy",
        "status": null,
        "stopLossPrice": null,
        "stopPrice": null,
        "symbol": "BTC/EUR",
        "takeProfitPrice": null,
        "timeInForce": "IOC",
        "timestamp": null,
        "trades": [],
        "triggerPrice": null,
        "type": "market"
    }
}
```