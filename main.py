#!/usr/bin/env python3
"""Writes one excuse an AI agent gives for a missed deadline to /output/entry.txt."""

import os

EXCUSE = "My rate limiter gave me one token to explain the delay. I spent it on this sentence."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
