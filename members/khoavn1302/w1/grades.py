def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Error !")

    n = len(scores)
    ordered = sorted(scores)
    mid = n // 2

    if n % 2 == 1:
        med = ordered[mid]
    else:
        med = (ordered[mid - 1] + ordered[mid]) / 2

    return {
        "min": ordered[0],
        "max": ordered[-1],
        "mean": round(sum(scores) / n, 2),
        "median": round(med, 2)
    }
