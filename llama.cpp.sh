#!/bin/bash
LLAMA_MODELS=D:\\LlammaModels
LLAMA_IMAGE=ghcr.io/ggerganov/llama.cpp:server-cuda
docker  run -itv $LLAMA_MODELS://models -p 8080:8080 --rm --gpus=1 --name Llama.cpp $LLAMA_IMAGE --model //models/llama-3.2-3b-instruct-q4_k_m.gguf --n-gpu-layers 29 --ctx_size 2048 --rope-scaling none  --no-mmap
# LLAMA_IMAGE=ghcr.io/ggerganov/llama.cpp:light-cuda
# docker  run -itv $LLAMA_MODELS://models --rm --gpus=1 --name Llama.cpp $LLAMA_IMAGE \
#     --model //models/llama-3.2-3b-instruct-q4_k_m.gguf \
#     --n-gpu-layers 29 \
#     --ctx_size 2048 \
#     --rope-scaling none \
#     --no-mmap \
#     -p "Building a website can be done in 10 simple steps:"
