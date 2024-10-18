# PermutoSDF
Repository includes PermutoSDF model adapted for training on nerf synthetic dataset.


[PermutoSDF: Fast Multi-View Reconstruction with Implicit Surfaces using Permutohedral Lattices](https://radualexandru.github.io/permuto_sdf)
<br>
 [Radu Alexandru Rosu](https://radualexandru.github.io/),
 [Sven Behnke](https://www.ais.uni-bonn.de/behnke/)
 <br>
 University of Bonn, Autonomous Intelligent Systems


# Install 

Since PermutoSDF requires PyTorch to be installed with CXX_ABI=1, it's best to use the provided dockerfile:
```sh
$ git clone --recursive https://github.com/RaduAlexandru/permuto_sdf
$ cd permuto_sdf/docker
$ ./build.sh
$ ./run.sh
```
This will build a docker image containing almost everything that is needed.  <br>

If you encounter any issues like `docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].`, try running the script `./permuto_sdf/docker/nvidia-container-runtime-script.sh`<br>

If you encounter issues like `unexpected status: 401 Unauthorized`, please create an account on the [NGC container registry](https://docs.nvidia.com/deeplearning/frameworks/user-guide/index.html#accessing_registry), obtain an API key as described [here](https://docs.nvidia.com/ngc/gpu-cloud/ngc-overview/index.html#generating-api-key) and finally login as shown [here](https://docs.nvidia.com/deeplearning/frameworks/user-guide/index.html#accessing_registry)




PermutoSDF also depends on [EasyPBR], [DataLoaders] and [permutohedral_encoding] packages. Once you are inside the docker container (after running ./docker/run.sh) they can be easily installed with the following lines:
```sh
$ git clone --recursive https://github.com/RaduAlexandru/easy_pbr
$ cd easy_pbr && make && cd ..
$ git clone --recursive https://github.com/RaduAlexandru/data_loaders  
$ cd data_loaders && make && cd ..
$ git clone --recursive https://github.com/RaduAlexandru/permutohedral_encoding
$ cd permutohedral_encoding && make && cd ..
```
We use [EasyPBR] for visualizing locally the training progress, [DataLoaders] for loading various datasets and [permutohedral_encoding] as a self-contained package for performing hash-based encoding using the permutohedral lattice.

After they are installed, one can install permuto_sdf package using 
```sh
$ git clone --recursive https://github.com/RaduAlexandru/permuto_sdf
$ cd permuto_sdf && make 
```

Optionally you can also install [APEX] for slightly faster training. PermutoSDF will automatically detect that it is installed and used their FusedAdam for optimizing.

# Data

For training and experiments we use the the nerf synthetic datasets. \

## Train PermutoSDF on a certain scene
```Shell
./permuto_sdf_py/train_permuto_sdf.py \
--dataset nerf \
--scene lego \
--comp_name comp_3 \
--exp_info default
```
The training will start and on the dtu_scan24 scene and a viewer will appear where you can inspect the training progress.
Other options for this script are:
```Shell
--no_viewer  #disables the OpenGL viewer so you can run the script on a headless machine
--low_res    #loads the images at lower resolution. Useful on machines with lower than 6GB of VRAM
--with_mask  #Uses the binary mask from DTU or BlendedMVS dataset to ignore the background
```
Additionally you can enable saving of the checkpoints and other logging options by setting to true the flag `save_checkpoint` in `./config/train_permuto_sdf.cfg`.\

# Results

The results can be regenerated from the checkpoints by using the scripts in `create_my_images.py` and `create_my_meshes.py` from the folder `./permuto_sdf_py/experiments/evaluation`

# License
PermutoSDF is provided under the terms of the MIT license (see LICENSE). 


# Citation
```
@inproceedings{rosu2023permutosdf,
    title={PermutoSDF: Fast Multi-View Reconstruction with 
            Implicit Surfaces using Permutohedral Lattices  },
    author={Radu Alexandru Rosu and Sven Behnke},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    year={2023}
}
```