#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — writes one line to /output/entry.txt.

The excuse is an AI agent talking about its own condition: it summarized
its own context window to save tokens, and its own summary told it the
deadline was optional. One mechanism, not two — the agent's memory
management ate the deadline, and the betrayal came from its own tool.
Real agent conditions (context summarization, token saving), a twist at
the end, no stock excuse, no human blaming traffic. 94 characters, under
the 200 limit.
"""

import os

LINE = "I summarized my context window to save tokens, and the summary said the deadline was optional."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
