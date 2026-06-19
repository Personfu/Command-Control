#!/usr/bin/env python3
"""Detect beacon-like timing in synthetic or authorized NetFlow exports.

This is a defensive lab utility. It does not generate beacons, deploy agents, or
communicate with remote systems.
"""
from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_events(path: Path) -> list[dict[str, Any]]:
    raw = json.loads(path.read_text(encoding='utf-8'))
    return raw if isinstance(raw, list) else raw.get('events', [])


def detect(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[int]] = defaultdict(list)
    for event in events:
        key = (str(event.get('src', 'unknown')), str(event.get('dst', 'unknown')))
        groups[key].append(int(event.get('ts', 0)))

    findings: list[dict[str, Any]] = []
    for (src, dst), timestamps in groups.items():
        if len(timestamps) < 4:
            continue
        ordered = sorted(timestamps)
        intervals = [b - a for a, b in zip(ordered, ordered[1:])]
        mean = statistics.mean(intervals)
        stdev = statistics.pstdev(intervals)
        if mean > 0 and stdev / mean < 0.15:
            findings.append({
                'src': src,
                'dst': dst,
                'events': len(timestamps),
                'mean_interval_seconds': round(mean, 2),
                'jitter_ratio': round(stdev / mean, 4),
                'classification': 'periodic-beacon-candidate',
            })
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description='Detect periodic timing in synthetic or authorized flow logs.')
    parser.add_argument('input', type=Path)
    parser.add_argument('--pretty', action='store_true')
    args = parser.parse_args()
    print(json.dumps(detect(load_events(args.input)), indent=2 if args.pretty else None))


if __name__ == '__main__':
    main()
