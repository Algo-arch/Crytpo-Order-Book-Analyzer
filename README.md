# Project Overview

This project implements a real-time cryptocurrency order book analyzer that measures liquidity imbalance between buyers and sellers using market depth data from the Binance exchange.

The system processes order book data and computes Order Book Imbalance, a market microstructure metric used to estimate short-term directional pressure in electronic markets.

The tool demonstrates how exchange market data can be transformed into actionable liquidity signals for trading and research.

## Features
- Real-time order book monitoring
- Bid vs Ask liquidity calculation
- Order book imbalance metric
- Market pressure detection

## Interpretation
- Positive → Buy pressure
- Negative → Sell pressure
- Near zero → Balanced liquidity

## Tech Stack
- Python
- Pandas
- Binance REST / WebSocket API

## Use Case
This project demonstrates market microstructure analysis and how order book liquidity can be used to build short-term trading signals for algorithmic strategies.
