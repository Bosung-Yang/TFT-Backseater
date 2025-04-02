import os 
from torch import cuda, bfloat16
import torch
import transformers
from transformers import AutoTokenizer
from time import time
from util import load_pretrained, load_model
import pandas as pd 
import json
import ast
import huggingface_hub


def unittest():
    huggingface_hub.login()
    model, tokenizer = load_model()
    model = model.to('mps')
    

    prompts = ['hello gemma3!']
    
    for prompt in prompts:
        input_ids = tokenizer.encode(prompt, return_tensors='pt').to('mps')

        output = model.generate(input_ids, max_length=2000, num_return_sequences=1, do_sample=True)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        print(generated_text[len(prompt):])
unittest()