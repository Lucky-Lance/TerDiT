# TerDiT: Ternary Diffusion Models with Transformers

Official Pytorch implementation of TerDiT as presented in paper:

**TerDiT: Ternary Diffusion Models with Transformers**</br>

![](assert/sample_ema_ternary_index.png "Sample Image")

## Installation
Step 1: Please first follow the installation instruction of [Large-DiT-ImageNet](https://github.com/Alpha-VLLM/LLaMA2-Accessory/tree/main/Large-DiT-ImageNet). We use ``cuda-12.1`` and ``gcc 9.4.0``.

Step 2: Install relevant packages
- replace fairscale with our modified package
    ```bash
    cd fairscale
    pip install -e .
    ```
- Install 2-bit kernal function from [hqq](https://github.com/mobiusml/hqq).
    ```bash
    cd kernel
    python3 setup_cuda.py install
    ```

## Checkpoints
Our trained 600M and 4.2B models are provided in [huggingface](https://huggingface.co/lucky-lance/TerDiT) 🤗.

## Sample

Run the code for sampling (assume your ckpt is downloaded in ``checkpoints/3B_1180000``):
```bash
python -u sample.py --ckpt checkpoints/3B_1180000 --local_diffusers_model_root  /path/to/diffusers_models --seed 42
```


