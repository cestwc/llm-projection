# -*- coding: utf-8 -*-
"""run_projection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lOaiaYeMNGT5D4QECrQq4PgnJAawMqwG
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install transformers auto-gptq optimum
# !pip install nltk contractions word2number pyspellchecker emoji==1.4.1

import os
os.environ['TRANSFORMERS_CACHE'] = '.'
os.environ['HF_DATASETS_CACHE'] = '.'

from transformers import AutoTokenizer
import transformers
import torch

model = "NousResearch/Llama-2-13b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

def ask_llama(text, question):
    inputs = f'Text: "{text}" {question}'
    sequences = pipeline(inputs, do_sample=True, top_k=1, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id, max_new_tokens=3)
    outputs = sequences[0]['generated_text']

    index = outputs.find(question)

    if index != -1:
        result = outputs[index + len(question):index + len(question) + 20]
        return result
    else:
        return None

from datasets import load_dataset

twitter = load_dataset('cestwc/SG-subzone-poi-sentiment_1')

# x = 'New exclusive listing clementi best location. 3a Blk 440B Clementi Ave 3. Well-kept. Only 3 years old!  singapore residential hdbresale buysellrent propnexsingapore @ Clementi'
# x = "I came here on two sets of occasions about 10 and 20 years ago, to complete the resale transactions of my current and previous HDB flats.\n\nThese days, I come here to work on making the future generations of HDB homes smarter.\n\n#smartnation #builtenvironment #strongerwithvos "
# x = "睡了二十七年，要搬家了。。。\n从landed回到HDB。。。\nCondo 每年要塞很久，因为visitor carparks很少。。。HDB有MSCP!\n#清明 #清明节 #扫墓 #坟场 @ Lim Chu Kang, Singapore"
q = 'Classify (yes or no) if the text is about Singapore estate maintenance issue. Answer one word only. Answer: '

def label_llama(e):
    e['preprocess-2'] = str(e['preprocess-2'])
    if e['shortlist'] > 0:
        e['llama'] = ask_llama(e['preprocess-2'], q)
    else:
        e['llama'] = 'unknown'
    print('---------------')
    print(e['llama'])
    print('')
    print(e['preprocess-1'])
    return e

t1 = twitter.map(label_llama, batched = False)

t1.sort("labels")

twitter['train'][0]['text']

# label_llama(twitter['train'][0]['text'])
ask_llama(twitter['train'][0]['preprocess-2'], q)