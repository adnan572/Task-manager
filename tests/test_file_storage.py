import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from models.task import Task
from storage.file_storage import FileStorage




TEST_FILE = "test_tasks.json"

@pytest.fixture
def sample_tasks():
    return [
        Task("Test 1", "Desc 1", "2025-05-15", "High"),
        Task("Test 2", "Desc 2", "2025-05-16", "Low", "in progress")
    ]

@pytest.fixture
def storage():
    return FileStorage(TEST_FILE)

def teardown_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_save_creates_file(storage, sample_tasks):
    storage.save_tasks(sample_tasks)
    assert os.path.exists(TEST_FILE)

def test_save_and_load(storage, sample_tasks):
    storage.save_tasks(sample_tasks)
    loaded = storage.load_tasks()

    assert len(loaded) == len(sample_tasks)
    for t1, t2 in zip(sample_tasks, loaded):
        assert t1.title == t2.title
        assert t1.description == t2.description
        assert t1.deadline == t2.deadline
        assert t1.priority == t2.priority
        assert t1.status == t2.status

def test_load_missing_file():
    bad = FileStorage("file_that_doesnt_exist.json")
    tasks = bad.load_tasks()
    assert tasks == []
