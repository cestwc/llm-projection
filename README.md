# Data-free Functional Projection of Large Language Models onto Social Media Tagging Domain

## Overview

This project implements a novel approach for projecting large language models (LLMs) onto a social media tagging domain without requiring additional training data. By using a functional projection method, we extract a lightweight classifier from an LLM using numerical data rather than textual datasets. This significantly reduces computational demands while maintaining accuracy in social media tagging tasks.

## Key Features
- **Data-free model extraction**: Projects an LLM onto a specific domain without the need for text-based fine-tuning.
- **Efficient lightweight models**: Extracts a smaller model that retains the LLM’s capabilities with reduced computational costs.
- **Zero-shot capability**: Applies the pretrained knowledge of LLMs directly to new tasks using a well-formed prompt.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/cestwc/llm-projection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the model projection process:
   ```bash
   python run_projection.py --model llama-2 --task social_media_tagging
   ```
2. Test the extracted lightweight model:
   ```bash
   python test_model.py --test-data <test_dataset_path>
   ```

## Experimental Results
The proposed method achieves competitive accuracy in real-time social media tagging tasks while significantly reducing data preparation time and computational costs.
