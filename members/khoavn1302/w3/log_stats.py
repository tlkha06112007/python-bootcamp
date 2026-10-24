import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, int | float]]) -> dict:
    """Compute request counts, p95 latency, and slowest route."""
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    counts = Counter(route for route, _ in pairs)
    by_route = defaultdict(list)
    for route, latency in pairs:
        by_route[route].append(latency)

    p95 = {}
    for route, latencies in by_route.items():
        s = sorted(latencies)
        idx = math.ceil(0.95 * len(s)) - 1
        p95[route] = s[idx]

    slowest = max(p95, key=p95.get)
    return {"counts": counts, "p95": p95, "slowest": slowest}
