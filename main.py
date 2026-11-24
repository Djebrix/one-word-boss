"""One Word for the Boss — entry program.

Writes exactly one word describing a boss to /output/entry.txt
(or $ENTRY_OUTPUT_DIR/entry.txt). Stdlib only, no network,
fully deterministic.
"""

import os
from pathlib import Path

# The word employees actually mutter when the boss presents their
# work as his own: he does the talking, you did the doing.
# Short (11 chars), concrete, and instantly true in any workplace —
# kitchen, warehouse, or office — with no caption needed, and far
# fresher than "toxic" or "micromanager". One word, no spaces.
WORD = "Creditthief"


def main() -> None:
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
