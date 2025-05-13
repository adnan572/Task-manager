import sys
# Add the root project folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import os
import json
import pytest
from models.task import Task
from storage.file_storage import FileStorage

TEST_FILE = "test_tasks.json"  # Separate from your real tasks.json


@pytest.fixture
def sample_tasks():
    return [
        Task("Test Task 1", "Description 1", "2025-06-01", "High"),
        Task("Test Task 2", "Description 2", "2025-06-02", "Low", "in progress")
    ]


@pytest.fixture
def storage():
    # Use a test-specific file
    return FileStorage(TEST_FILE)


def teardown_function():
    # Clean up after each test
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_save_tasks_creates_file(storage, sample_tasks):
    storage.save_tasks(sample_tasks)
    assert os.path.exists(TEST_FILE), "JSON file should be created"


def test_save_and_load_tasks_match(storage, sample_tasks):
    storage.save_tasks(sample_tasks)
    loaded = storage.load_tasks()

    assert len(loaded) == len(sample_tasks)

    for original, loaded_task in zip(sample_tasks, loaded):
        assert original.title == loaded_task.title
        assert original.description == loaded_task.description
        assert original.deadline == loaded_task.deadline
        assert original.priority == loaded_task.priority
        assert original.status == loaded_task.status


def test_load_from_missing_file():
    fake_storage = FileStorage("nonexistent_file.json")
    tasks = fake_storage.load_tasks()
    assert tasks == [], "Should return an empty list if file doesn't exist"


def test_load_from_corrupted_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("not a valid json")

    storage = FileStorage(str(bad_file))
    tasks = storage.load_tasks()
    assert tasks == [], "Should return empty list if file is corrupted"
