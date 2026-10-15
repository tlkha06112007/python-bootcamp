"""Format allocated study blocks as a readable plan."""

from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Return a numbered plan with dot leaders and hours to one decimal place.

    Preserve block order. An empty plan contains only ``Tonight (0.0 h):``.
    The returned string has no trailing newline and nothing is printed.
    """
    total_hours = sum(block.hours for block in blocks)
    lines = [f"Tonight ({total_hours:.1f} h):"]
    labels = [f"{index}. {block.task.title}" for index, block in enumerate(blocks, start=1)]
    width = max((len(label) for label in labels), default=0)

    for label, block in zip(labels, blocks):
        dots = "." * (width - len(label) + 6)
        lines.append(f"{label} {dots} {block.hours:.1f} h")

    return "\n".join(lines)
