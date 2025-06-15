import os
from shutil import rmtree
from checkpoint import CheckpointManager, Checkpoint


def test_checkpoint_creation():

    checkpoints_dir = "checkpoints"
    os.makedirs(checkpoints_dir, exist_ok=True)

    manager = CheckpointManager(checkpoints_dir)
    new_checkpoint = manager.get_new_checkpoint()

    new_checkpoint.name1 = "Manage"
    new_checkpoint.file = "my file"
    new_checkpoint.count = 1000
    new_checkpoint.list_view = [12, 3, 4, 100]
    new_checkpoint.code = 10.32
    new_checkpoint.commit()

    assert os.path.isfile(new_checkpoint.filepath)

    new_checkpoint2 = manager.get_new_checkpoint()
    assert new_checkpoint2.filepath != new_checkpoint.filepath
    assert os.path.isfile(new_checkpoint2.filepath)

    new_checkpoint3 = manager.get_new_checkpoint()
    new_checkpoint3.code = 10000
    new_checkpoint3.commit()

    last_checkpoint_file = manager.find_last_checkpoint_file()
    assert isinstance(last_checkpoint_file, str)
    assert last_checkpoint_file == new_checkpoint3.filepath

    rmtree(checkpoints_dir)
