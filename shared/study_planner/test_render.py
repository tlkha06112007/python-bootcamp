from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def make_block(title: str, hours: float) -> Block:
    return Block(
        task=Task(
            title=title,
            importance=3,
            effort_h=hours,
            deadline=date(2026, 10, 20),
        ),
        hours=hours,
    )


def test_render_matches_guide_example_and_preserves_order():
    blocks = [make_block("Assignment", 1.5), make_block("DS exam", 0.5)]

    assert render(blocks) == (
        "Tonight (2.0 h):\n"
        "1. Assignment ...... 1.5 h\n"
        "2. DS exam ......... 0.5 h"
    )


def test_render_empty_list_has_exact_header_without_trailing_newline():
    result = render([])

    assert result == "Tonight (0.0 h):"
    assert not result.endswith("\n")


def test_render_single_block():
    assert render([make_block("DS exam", 1.0)]) == (
        "Tonight (1.0 h):\n"
        "1. DS exam ...... 1.0 h"
    )


def test_render_sums_unrounded_hours_before_formatting():
    result = render([make_block("First", 1.26), make_block("Second", 1.26)])

    assert result.startswith("Tonight (2.5 h):\n")
    assert "1. First" in result and "1.3 h" in result
    assert "2. Second" in result and "1.3 h" in result


def test_render_aligns_entries_when_there_are_more_than_nine_blocks():
    blocks = [make_block(f"Task {index}", 0.5) for index in range(1, 11)]
    lines = render(blocks).splitlines()[1:]

    assert len(lines) == 10
    assert lines[0].startswith("1. Task 1 ")
    assert lines[8].startswith("9. Task 9 ")
    assert lines[9].startswith("10. Task 10 ")

    dotted_ends = []
    for index, line in enumerate(lines, start=1):
        title_prefix = f"{index}. Task {index} "
        assert line.startswith(title_prefix)
        dots = line[len(title_prefix):].split(" ", maxsplit=1)[0]
        assert dots and set(dots) == {"."}
        dotted_ends.append(len(title_prefix) + len(dots))

    assert len(set(dotted_ends)) == 1


def test_render_does_not_print_to_stdout_or_stderr(capsys):
    result = render([make_block("Quiet", 1.0)])

    captured = capsys.readouterr()
    assert isinstance(result, str)
    assert captured.out == ""
    assert captured.err == ""


def test_render_does_not_mutate_blocks_or_tasks():
    blocks = [make_block("Keep me", 1.25), make_block("Also keep me", 0.75)]
    before = [
        (
            block.task.title,
            block.task.importance,
            block.task.effort_h,
            block.task.deadline,
            block.hours,
        )
        for block in blocks
    ]

    render(blocks)

    after = [
        (
            block.task.title,
            block.task.importance,
            block.task.effort_h,
            block.task.deadline,
            block.hours,
        )
        for block in blocks
    ]
    assert after == before
