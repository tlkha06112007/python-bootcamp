from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    blocks = []
    remain = float(hours)

    for task in tasks:
        if remain <= 0:
            break
        give = min(task.effort_h, remain)
        if give > 0:
            blocks.append(Block(task, give))
            remain -= give

    return blocks