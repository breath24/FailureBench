# FailureBench: Where Do LLMs Still Struggle?

This repository contains the experimental data and analysis tools for the paper "Where Do LLMs Still Struggle? An In-Depth Analysis of Code Generation Benchmarks".

## Overview

Large Language Models (LLMs) have achieved remarkable success in code generation, but understanding their failure patterns remains crucial for model improvement. This work systematically analyzes tasks that consistently cause LLM failures across popular benchmarks.

## Repository Structure

- **`evaluation-results/`** - Experimental results and generated solutions
  - **`llm-generated-code/`** - Generated code from 6 LLMs across 4 benchmarks
    - `HumanEval/` - Generated code for HumanEval benchmark tasks
    - `MBPP/` - Generated code for MBPP benchmark tasks  
    - `LiveCodeBench/` - Generated code for LiveCodeBench tasks
    - `BCB-Hard/` - Generated code for BigCodeBench-Hard tasks
  - `model-failures-per-task/` - Analysis of model failures organized by task

- **`failure-inspection/`** - Detailed analysis of consistently failed tasks

- **`complexity/`** - Code complexity measurement tools and results
  - `complexity-measurement/` - Main script that takes a folder path of solution code as input and generates complexity metrics as CSV output
  - `comparison-plots/` - Visualization of complexity metrics across benchmarks

## Benchmarks & Models

**Benchmarks**: HumanEval (164 tasks), MBPP (378 tasks), LiveCodeBench (175 tasks), BCB-Hard (148 tasks)

**Models**: Claude Sonnet-4, DeepSeek-V3, Qwen3-Coder, GPT-4o, Llama-3.3-70B, Mistral-3.2-24B

---

This repository provides experimental data and analysis tools for understanding where state-of-the-art LLMs still struggle in code generation tasks and failure analysis of code generation benchmarks.
