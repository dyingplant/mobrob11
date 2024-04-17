# Steps to run YCbCr on KITTI dataset
1. Download the KITTI dataset from [here](https://www.cvlibs.net/datasets/kitti/eval_odometry.php)
2. Download shadow removal algorithm on YCbCr color space from [here](https://github.com/mmostipan/shadow-removal/blob/master/Shadow%20Detection%20and%20Removal%20Based%20on%20YCbCr%20Color%20Space.pdf). Rename and place it at `./checkpoints/ISTD/ShadowRemoval.pth`.
3. Change the path of dataset (`DATA_ROOT` and `TEST_FLIST`) in `./checkpoints/ISTD/config.yml` to the path of KITTI dataset.
4. Change numbers related to the shadow and lit areas if it is needed.
4. `python run.py` to run the model on KITTI dataset.