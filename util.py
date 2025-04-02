import pandas as pd
import ast

def preprocess_augment():
    with open('./data/augment.txt','r') as f:
        lines = f.readlines()
    
    Augment = []
    Tier = []
    Types = []

    DefinedTypes = ['StrategicStrategic', 'GoldEconomy', 'CombatCombat', 'ScalingScaling', 'TraitsTrait', 'ItemsItems']

    idx = 0
    while idx < len(lines):
        types = []
        Augment.append(lines[idx].strip())
        idx +=1
        Tier.append(lines[idx].strip())
        idx +=1

        while idx < len(lines):
            if lines[idx].strip() in DefinedTypes:
                types.append(lines[idx].strip())
                idx += 1
            else:
                #idx +=1
                break
        Types.append(types)
    #print(Augment, Tier, Types)
#    print(len(Augment), len(Tier), len(Type))
    
    df = pd.DataFrame({'Augment':Augment, 'Tier':Tier, 'Type':Types})
    print(df)
    df.to_csv('./data/augment.csv', index=False)

#preprocess_augment()

def remove_redundancy():
    def remove_redundant_name(x):
        return x[:len(x)//2]
    def remove_redundant_type(x):
        new_x = []
        for item in x:
            print(item)
            if item[:len(item)//2] == item[len(item)//2:]:
                new_x.append(item[:len(item)//2])
            else:
                new_x.append('Economy')
        return new_x

    df = pd.read_csv('./data/augment.csv')
    df['Type'] = df['Type'].apply(ast.literal_eval)
    df['Augment'] = df['Augment'].apply(remove_redundant_name)
    df['Type'] = df['Type'].apply(remove_redundant_type)
    print(df)
    df.to_csv('./data/augment-preprocessed.csv', index=False)
    
#remove_redundancy()

from torch import cuda, bfloat16
import torch
import transformers
from transformers import AutoTokenizer, Gemma3ForConditionalGeneration
from time import time
import os 

def load_phi4():
    model_id = 'microsoft/phi-4'
    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=bfloat16
    )
    model_config = transformers.AutoConfig.from_pretrained(
        model_id,
        trust_remote_code=True,
        max_new_tokens=1024
    )
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        #config=model_config,
        #quantization_config=bnb_config,
        #device_map='auto',
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    return model, tokenizer

def load_model():
    model_id = 'google/gemma-3-4b-it' #'microsoft/phi-4'
    
    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=bfloat16
    )

    model_config = transformers.AutoConfig.from_pretrained(
        model_id,
        trust_remote_code=True,
        max_new_tokens=1024
    )
    model = Gemma3ForConditionalGeneration.from_pretrained(
        model_id,
        trust_remote_code=True,
        #config=model_config,
        #quantization_config=bnb_config,
        #device_map='auto',
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    return model, tokenizer

def load_pretrained(model_name):
    model = transformers.AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    return model, tokenizer
