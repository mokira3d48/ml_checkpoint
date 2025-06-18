

class Checkpoint:

    def __init__(self, repos):
        self._repos = repos

    @property
    def filepath(self):
        """
        Path to checkpoint file where this checkpoint save.
        :return: A string representing the path to this checkpoint.
        :rtype: `str`
        """
        return self._repos.file_path

    def open(self):
        """
        Method of opening of saving file.
        """
        self._repos.open()

    def state_dict(self):
        """
        Method to load all variable and its values.
        :return: A dictionary contained class data.
        """
        state_dict = {}
        for attr, value in self.__dict__.items():
            if attr.startswith('_'):
                continue
            state_dict[attr] = value
        return state_dict

    def _get_data_changed(self):
        """
        Method to filter only changed data.
        :return: A dictionary containing the data that are changed only.
        :rtype: typing.Dict[str, object]
        """
        ...

    def commit(self):
        """
        Method to commit data into file.
        """
        data = self.state_dict()
        data_changed = self._get_data_changed()
        self._repos.save(data_changed)


class CheckpointManager:
    """
    Checkpoint manager system
    -------------------------

    :arg checkpoints_dir: The path to the checkpoint directory.
    :type checkpoints_dir: `str`
    """
    def __init__(self, checkpoints_dir):
        self.checkpoints_dir = checkpoints_dir

    def get_new_checkpoint(self):
        """
        Method of create a new checkpoint instance.

        :return: An instance of Checkpoint
        :rtype: `Checkpoint`
        """
        ...