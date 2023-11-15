from graphlib import TopologicalSorter
from typing import Optional
from simpleflow.base import Task


class Workflow(TopologicalSorter):

    def execute(self, context: Optional[dict] = None) -> dict:
        task: Task

        if context is None:
            context = {}

        for task in self.static_order():
            task.execute(context=context)

        return context
