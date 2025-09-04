# FailureBench: Where Do LLMs Still Struggle?

This repository contains the experimental data and analysis tools for the paper "Where Do LLMs Still Struggle? An In-Depth Analysis of Code Generation Benchmarks".

## Overview

Large Language Models (LLMs) have achieved remarkable success in code generation, but understanding their failure patterns remains crucial for model improvement. This work systematically analyzes tasks that consistently cause LLM failures across popular benchmarks.


## Repository Structure

- **`llm-generated-solutions/`** - Generated code from 6 LLMs across 4 benchmarks
  - `HumanEval/` - Solutions for HumanEval benchmark tasks
  - `MBPP/` - Solutions for MBPP benchmark tasks  
  - `LiveCodeBench/` - Solutions for LiveCodeBench tasks
  - `BCB-Hard/` - Solutions for BigCodeBench-Hard tasks

- **`failure-inspection/`** - Detailed analysis of consistently failed tasks

- **`Complexity/`** - Code complexity measurement tools and results
  - `Complexity_Measurement/` - Main script that takes a folder path of solution code as input and generates complexity metrics as CSV output
  - `Comparison_Plots/` - Visualization of complexity metrics across benchmarks

## Benchmarks & Models

**Benchmarks**: HumanEval (164 tasks), MBPP (378 tasks), LiveCodeBench (175 tasks), BCB-Hard (148 tasks)

**Models**: Claude Sonnet-4, DeepSeek-V3, Qwen3-Coder, GPT-4o, Llama-3.3-70B, Mistral-3.2-24B

---

This repository provides experimental data and analysis tools for understanding where state-of-the-art LLMs still struggle in code generation tasks and failure analysis of code generation benchmarks.