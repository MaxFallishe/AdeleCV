<div align="center">
 
<img src="docs/logo.png" alt="drawing" width="200"/>

**Python library and dashboard for hyperparameter search and model training for computer vision tasks
based on [PyTorch](https://pytorch.org/), [Optuna](https://optuna.org/),
    [FiftyOne](https://docs.voxel51.com/), [Dash](https://dash.plotly.com/),
    [Segmentation Model Pytorch](https://github.com/qubvel/segmentation_models.pytorch).**  

[![Generic badge](https://img.shields.io/badge/License-MIT-<COLOR>.svg?style=for-the-badge)](https://github.com/AsakoKabe/AdeleCV/blob/main/LICENSE) 

[//]: # ([![GitHub Workflow Status &#40;branch&#41;]&#40;https://img.shields.io/github/actions/workflow/status/qubvel/segmentation_models.pytorch/tests.yml?branch=master&style=for-the-badge&#41;]&#40;https://github.com/qubvel/segmentation_models.pytorch/actions/workflows/tests.yml&#41; )
[![Read the Docs](https://img.shields.io/readthedocs/smp?style=for-the-badge&logo=readthedocs&logoColor=white)](https://adelecv.readthedocs.io/en/latest/) 

[//]: # (<br>)

[//]: # ([![PyPI]&#40;https://img.shields.io/pypi/v/segmentation-models-pytorch?color=blue&style=for-the-badge&logo=pypi&logoColor=white&#41;]&#40;https://pypi.org/project/segmentation-models-pytorch/&#41; )
[//]: # ([![PyPI - Downloads]&#40;https://img.shields.io/pypi/dm/segmentation-models-pytorch?style=for-the-badge&color=blue&#41;]&#40;https://pepy.tech/project/segmentation-models-pytorch&#41; )
[//]: # (<br>)
</div>

The main features of this library are:

 - Fiftyone dataset integration with prediction visualization
 - Uploading your dataset in one of the popular formats, currently supported - 2
 - Adding your own python class for convert dataset
 - Displaying training statistics in tensorboard
 - Support for all samples from optuna
 - Segmentation use smp: 9 model architectures, popular losses and metrics, see [doc smp](https://github.com/qubvel/segmentation_models.pytorch)
 - convert weights to another format, currently supported - 0
 
### [📚 Project Documentation 📚](https://adelecv.readthedocs.io/en/latest/)

Visit [Read The Docs Project Page](https://adelecv.readthedocs.io/en/latest/) or read following README to know more about Auto Deap Learning Computer Vision (AdeleCV for short) library

### 📋 Table of content
 1. [Examples](#examples)
 2. [Installation](#installation)
 3. [Architecture](#architecture) 
 4. [Citing](#citing)
 5. [License](#license)


### 💡 Examples <a name="examples"></a>
 - Example api [notebook](example/example_api.ipynb) and [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](example/example_api.ipynb)
 - See [video](youtube.com) on the example of using dashboard

### 🛠 Installation <a name="installation"></a>
Install torch cuda if not installed:
```bash
$ pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```

PyPI version:
```bash
$ pip install adelecv
````
Poetry:
```bash
$ poetry add adelecv
````

### 🏰 Architecture <a name="architecture"></a>
![architecture](docs/architecture.png) 

The user can use the api or dashboard(web app). 
The api is based on 5 modules:
- data: contains an internal representation of the dataset, classes for converting datasets, fiftyone dataset
- _models: torch model, its hyperparams, functions for training
- optimize: set of hyperparams, optuna optimizer
- modification model: export and conversion of weights
- logs: python logging 

The Dash library was used for dashboard. It is based on components and callbacks on these component elements.

### 📝 Citing
```
@misc{Mamatin:2023,
  Author = {Denis Mamtin},
  Title = {AdeleCV},
  Year = {2023},
  Publisher = {GitHub},
  Journal = {GitHub repository},
  Howpublished = {\url{https://github.com/AsakoKabe/AdeleCV}}
}
```

### 🛡️ License <a name="license"></a>
Project is distributed under [MIT License](https://github.com/AsakoKabe/AdeleCV/blob/main/LICENSE)