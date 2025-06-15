

class Checkpoint:
    ...



class CheckpointManager:
    """
    Checkpoint manager system
    -------------------------

    :arg checkpoints_dir: The path to the checkpoint directory.
    :type checkpoints_dir: `str`
    """
    def __init__(self, checkpoints_dir):
        self.checkpoints_dir = checkpoints_dir
