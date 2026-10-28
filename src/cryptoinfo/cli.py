"""CLI entry point."""
import argparse
from cryptoinfo.data import load_ohlcv
from cryptoinfo.strategies import btc

def demo():
    print("Crypto Trading Information System Demo")
    print("Using synthetic data only. Not financial advice.")
    # Placeholder - in full version load fixture
    print("BTC signal example: LONG (trend)")
    print("See docs for full architecture and security model.")

if __name__ == "__main__":
    demo()
