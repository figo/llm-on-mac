# llm-on-mac
Inferencing Large Language Models on Mac: Mac mini, Macbook...

## Why
- Don't you curious about the magic behind the chatGPT? the first step to deep dive into it is inferencing a LLM model from huggingface.
- Innovation opportunities, there is a lot data we don't want to share outside, but we can let models utilize them if we can inference the model at home (think about more personalized answers).

## How
| Framework | Hardware | Models|
| ------ |  ------ |  ------ |
| https://github.com/ggerganov/llama.cpp is written in CPP, make it possible to run on Mac. https://github.com/ollama/ollama is written in golang (although I havn't experimented it)| Mac Mini M4 | https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF, https://huggingface.co/bartowski/Qwen2.5.1-Coder-7B-Instruct-GGUF or the model supports GGUF https://huggingface.co/models?library=gguf&sort=trending |

### What is GGUF
https://huggingface.co/docs/hub/en/gguf#finding-gguf-files

## Result
My results with Llama-3.1 and Qwen are very impressive, the whole family is enjoying talking to our own chatGPT server from any computer at home.
On the sideline, the new Mac Mini M4 hardware is quiet, capable and affordable. 

## Looking forward
- Will keep updating the model list here that is possible to run on Mac Mini M4 (only text generation models are possible at this moment, but things might evolve)
- So far, the framework is not able to leverage Mac Mini's GPU hardware, has to integrate https://github.com/ml-explore/mlx, the integration is coming (https://github.com/ollama/ollama/issues/1730).
- The concept of LoRA is interesting, https://github.com/ggerganov/llama.cpp/discussions/10123
- Happy to discuss more about the ideas, pls find me at @hui-luo.bsky.social
