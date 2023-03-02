from __future__ import annotations

import pytest

from app.database import add_task


@pytest.mark.asyncio
async def test_add_task():
    task = {'name': 'task1', 'priority': 1, 'status': 'todo'}
    task_return = await add_task(task)
    assert task_return['name'] == task['name']
