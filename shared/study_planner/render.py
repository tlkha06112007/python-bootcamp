from shared.contract import Block


def render(blocks: list[Block]) -> str:
    total = sum(b.hours for b in blocks)
    lines = [f"Tonight ({total:.1f} h):"]
    names = [f"{i}. {b.task.title}" for i, b in enumerate(blocks, 1)]
    width = max(map(len, names), default=0)

    for name, b in zip(names, blocks):
        dots = "." * (width - len(name) + 6)
        lines.append(f"{name} {dots} {b.hours:.1f} h")

    return "\n".join(lines)
