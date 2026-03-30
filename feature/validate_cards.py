#!/usr/bin/env python3
"""Validate cards.csv for data quality issues."""

import csv
import sys

def validate(filename='cards.csv'):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    discoveries = {r['discovery'].strip() for r in rows}
    errors = []

    for i, row in enumerate(rows, 2):
        # Check required fields
        if not row['discovery'].strip():
            errors.append(f'Line {i}: empty discovery name')

        # Check period.id is valid
        try:
            pid = int(row['period.id'].strip('"'))
            if pid not in range(1, 7):
                errors.append(f'Line {i}: invalid period.id {pid}')
        except ValueError:
            errors.append(f'Line {i}: non-integer period.id')

        # Check dependency references exist
        deps = row['dependson'].strip()
        if deps:
            separator = '; ' if '; ' in deps else ','
            for dep in deps.split(separator):
                dep = dep.strip()
                if dep and dep not in discoveries:
                    errors.append(f'Line {i}: "{row["discovery"]}" depends on "{dep}" which does not exist')

    # Check duplicates
    seen = {}
    for i, row in enumerate(rows, 2):
        name = row['discovery'].strip()
        if name in seen:
            errors.append(f'Line {i}: duplicate discovery "{name}" (first at line {seen[name]})')
        seen[name] = i

    if errors:
        print(f'Found {len(errors)} error(s):')
        for e in errors:
            print(f'  - {e}')
        return 1
    else:
        print('All checks passed!')
        return 0

if __name__ == '__main__':
    sys.exit(validate())
