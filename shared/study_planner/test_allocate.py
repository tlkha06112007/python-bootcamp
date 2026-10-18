import unittest

from shared.contract import Task
from shared.study_planner.allocate import allocate


class TestAllocate(unittest.TestCase):

    def setUp(self):
        self.task1 = Task(name="Task 1", effort_h=2.0)
        self.task2 = Task(name="Task 2", effort_h=3.0)
        self.task3 = Task(name="Task 3", effort_h=5.0)

    def test_allocate_sufficient_hours(self):
        tasks = [self.task1, self.task2]
        blocks = allocate(tasks, hours=10.0)

        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0].task, self.task1)
        self.assertEqual(blocks[0].hours, 2.0)
        self.assertEqual(blocks[1].task, self.task2)
        self.assertEqual(blocks[1].hours, 3.0)

    def test_allocate_partial_hours(self):
        tasks = [self.task1, self.task2, self.task3]
        blocks = allocate(tasks, hours=4.0)

        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0].hours, 2.0)
        self.assertEqual(blocks[1].hours, 2.0)

    def test_allocate_zero_or_negative_hours(self):
        tasks = [self.task1]
        self.assertEqual(allocate(tasks, hours=0.0), [])
        self.assertEqual(allocate(tasks, hours=-5.0), [])

    def test_allocate_empty_tasks(self):
        self.assertEqual(allocate([], hours=10.0), [])


if __name__ == "__main__":
    unittest.main()