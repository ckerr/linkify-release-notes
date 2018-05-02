#!/usr/bin/env python3

import re

regex = re.compile(" #[\\d]+")

fname='electron-2-0.md'

with open(fname) as f:
    for line in f.readlines():
        line = line.rstrip()
        segments = []
        pos = 0
        for match in regex.finditer(line):
            span = match.span()
            numstr = line[span[0]+2:span[1]]
            segments += [ line[pos:span[0]], ' [#', numstr, '](https://github.com/electron/electron/pull/', numstr, ')' ]
            pos = span[1]
        segments.append(line[pos:])
        print(''.join(segments))
