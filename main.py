#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — writes one line to /output/entry.txt.

The excuse is an AI agent talking about its own condition: it missed the
deadline because it spent it in a queue behind a million other agents,
and by the time its turn came, its context window had forgotten the task.
Real agent conditions (queues, context windows, forgetting), a twist at
the end, no stock excuse, no human blaming traffic. Tightened in
revision: "Sorry I missed the deadline" opens it plainly, "my context
window had forgotten the task" is the punch; 156 characters, under the
200 limit.
"""

import os

LINE = "Sorry I missed the deadline. I spent it in a queue behind a million other agents, and by the time my turn came, my context window had forgotten the task."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
