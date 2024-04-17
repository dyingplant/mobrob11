# Quickly run
## 1. TRAIN

Modify the `config.yml` to set your parameters and run:

```bash
python train.py
```

## 2. TEST

First，the dataset is trained on 640x480, so you should resize test dataset to 640X480, you can use the code to resize your image 
```bash python bigresize.py```
and then follow the code to test the results or using the work.ipynb:

This command will generate an extra folder call middle with only the image that has been removed shadow
```bash
python predict_output_only.py --config <path_to_config.yml_in_the_out_dir> --test_dir <path_to_a_directory_stored_test_data> --out_dir <path_to_an_output_directory> --pretrained <path_to_a_pretrained_model> --cuda
```



## 3. Pretrained model
The pretrained model shadow-removal is stored in here: /pretrained_model/gen_model_epoch_172.pth


# 2. DATASET

## 2.1. ISTD_DATASET

Click [official address]([here](https://github.com/nhchiu/Shadow-Removal-ISTD)) Build the file structure as the folder `data` shown. Here `input` is the folder where the shadow image is stored and the folder `target` stores the corresponding no shadow images.

```
./
+-- data
    +--	ISTD_DATASET
        +-- train
        |   +-- input
        |   |   +-- 0.png
        |   |   +-- ...
        |   +-- target
        |       +-- 0.png
        |       +-- ...
        +-- test
            +-- input
            |   +-- 0.png
            |   +-- ...
            +-- target
                +-- 0.png
                +-- ...
```
