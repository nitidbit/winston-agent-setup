#!/usr/bin/env python3

"""
Install symlinks for my dotfiles

Usage:
    ./symlink.py
"""
import os
from pathlib import Path
from functools import reduce

HERE = Path(__file__, '..').resolve()
DOT_CLAUDE = Path(os.environ['HOME']) / '.claude'

dot_files = [
    # src                                link
    (HERE / 'CLAUDE.md',                 DOT_CLAUDE / 'CLAUDE.md'),
    (HERE / 'skills/prd-to-issues/',     DOT_CLAUDE / 'skills/prd-to-issues/'),
    (HERE / 'skills/write-a-prd/',       DOT_CLAUDE / 'skills/write-a-prd/'),
    (HERE / 'skills/grill-with-docs/',   DOT_CLAUDE / 'skills/grill-me-with-docs/'),
]


longest_link = reduce(lambda acc, row: max(acc, len(str(row[1]))),
                      dot_files, 30)
for src, link in dot_files:
    if link.exists():
        print('{link:{length}} already exists. Skipping'.format(link=str(link), length=longest_link))
    else:
        print('{link:{length}} <-- {src}'.format(link=str(link), length=longest_link, src=str(src)))
        link.symlink_to(src)
