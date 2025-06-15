<div align="center">
  
### MACHINE LEARNI CHECKPOINT SYSTEM

![](https://img.shields.io/badge/Python-3.8-blue)
![](https://img.shields.io/badge/LICENSE-MIT-%2300557f)
![](https://img.shields.io/badge/lastest-2025--06--15-green)
![](https://img.shields.io/badge/contact-dr.mokira%40gmail.com-blueviolet)

---

</div>

The checkpoint system in machine learning is a crucial mechanism for saving the state of a model during training, serving as a safeguard and optimization tool. You can use this module for the following use cases:

1. Recovery from Failures

- Resume Training: If training is interrupted (e.g., hardware failure, power loss, job preemption), checkpoints allow restarting from the last saved state instead of from scratch.
- Fault Tolerance: Critical for long-running distributed training jobs where failures are common.

2. Model Selection & Early Stopping

- Track Best Performance: Save checkpoints when validation metrics improve (e.g., lowest loss, highest accuracy).
- Avoid Overfitting: Restore the best-performing model if performance plateaus or degrades (via early stopping).

#### Table of Contents
- [Installation](#installation)
  - [For Linux](#for-linux)
  - [For Windows](#for-windows)
- [Usage](#usage)
- [Features](#features)
- [Tests](#tests)
- [To contribute](#to-contribute)
- [Licence](#licence)
- [Contact](#contact)


## Installation

To install the project, make sure you have Python 3.8 or later version
and `pip` installed on your machine. And then run the following command lines.

### For Linux

```bash
git clone git@github.com:mokira3d48/ml_checkpoint.git ml_checkpoint
cd ml_checkpoint
sudo rm -r .git;
git init;  # To create a new instance of git repository
```

And then,

1. `sudo apt install cmake python3-venv` Install *Cmake* and *Virtual env*;
2. `python3 -m venv .venv` create a virtual env into directory
named `env`;
3. `source .venv/bin/activate` activate the virtual environment named `.venv`;
4. `make install` install the requirements of this package;

### For Windows

```bash
git clone git@github.com:mokira3d48/ml_checkpoint.git ml_checkpoint
```

```bash
cd ml_checkpoint
```

And then, delete the hidden directory named `.git` located at the root
of the directory project.

And then,

1. Install python for windows;
2. Open your command prompt;
3. Run `python -m venv .venv` to create a virtual env into directory
named `.venv`;
4 . Run `.venv\Scripts\activate` to activate the virtual environment;
5. Run `pip install -r requirements.txt` to install the requirements
of this module.


---

## Usage


## Features

- Create new checkpoint file;
- Save checkpoint;
- Load existing checkpoint file;
- Find last checkpoint file.

## Tests

To execute the unittest, make sure you have `pytest` package installed,
and then run the following command line:

```bash
make test 
```
or

```shell
pytest
```

---

## To contribute

Contributions are welcome! Please follow these steps:

1. Create a new branch for your feature (`git checkout -b feature/my-feature`);
2. Commit your changes (`git commit -m 'Adding a new feature'`);
3. Push toward the branch (`git push origin feature/my-feature`);
4. Create a new *Pull Request* or *Merge Request*.

## Licence

This project is licensed under the GPL-3.0 License. See the file [LICENSE](LICENSE)
for more details, contact me please.

## Contact

For your question or suggestion, contact me please:

- **Name** : Doctor Mokira
- **Email** : dr.mokira@gmail.com
- **GitHub** : [mokira3d4](https://github.com/mokira3d48)
