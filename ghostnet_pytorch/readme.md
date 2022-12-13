# GhostNet

GhostNet: More Features from Cheap Operations. CVPR 2020. [[arXiv]](https://arxiv.org/abs/1911.11907) [[Most Influential CVPR 2020 Papers]](https://www.paperdigest.org/2021/08/most-influential-cvpr-papers-2021-08/)

Brian Tufts, Joseph Loggi, Shihe Wang

- **Training**
To train on raw images, you must convert them to another format first. jpeg is the only known supported image format.
You can use convert.py to do this, just change the 'rootdir' variable to the location of the raw images.
It will save the images into the file designated by 'datadir' which will already be ready to be passed into train.py and validate.py.

MUST have access to a GPU for this to run. Starting a Rivanna gui with a GPU will work. You can also submit a slurm job with a GPU.

### Requirements
The code was verified on Python3.6, PyTorch-1.0+.
Must load the following modules on Rivanna:
module load singularity/3.7.1
module load pytorch/1.8.1
module load nvompic
module load goolfc

### Usage
Run `python train.py` to train using `train` set.
Run `python validate.py` to evaluate on `val` set.

You'll get the accuracy: top-1 acc=`0.74`

### Data Preparation
Data dir should have the following structure:
```
data/
  train/
    Diseased/
      ILSVRC2012_val_00000293.JPEG
      ...
    Healthy/
      ILSVRC2012_val_00000293.JPEG
      ...
    ...
  val/
    Diseased/
      ILSVRC2012_val_00000293.JPEG
      ...
    Healthy/
      ILSVRC2012_val_00000293.JPEG
      ...
```
