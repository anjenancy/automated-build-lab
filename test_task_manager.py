from task_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    assert tm.add_task("Study Agile") == "Task added"

def test_view_tasks():
    tm = TaskManager()
    tm.add_task("Read book")
    assert len(tm.view_tasks()) == 1

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Finish lab")
    result = tm.complete_task(0)
    assert result == "Task completed"

def test_delete_task():
    tm = TaskManager()
    tm.add_task("Submit assignment")
    result = tm.delete_task(0)
    assert result == "Task deleted"
