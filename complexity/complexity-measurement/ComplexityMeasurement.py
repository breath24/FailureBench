import os
import ast
import pandas as pd
from DifficultyAnalyzer import DifficultyAnalyzer

def analyze_python_file(file_path):
    """Analyze a single Python file and return its metrics"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Skip empty files
        if not code.strip():
            return None
            
        analyzer = DifficultyAnalyzer()
        metrics = analyzer.analyze(code)
        
        # Extract task_id from filename (without .py extension)
        task_id = os.path.splitext(os.path.basename(file_path))[0]
        metrics['task_id'] = task_id
        
        return metrics
        
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

def analyze_benchmark_directory(directory_path, output_csv):
    """Analyze all Python files in a directory and save results to CSV"""
    all_metrics = []
    
    # Get all Python files in the directory
    for filename in os.listdir(directory_path):
        if not filename.endswith('.py'):
            continue
            
        file_path = os.path.join(directory_path, filename)
        metrics = analyze_python_file(file_path)
        
        if metrics:
            all_metrics.append(metrics)
    
    if not all_metrics:
        print("No valid Python files found or an error occurred")
        return
    
    # Create DataFrame and reorder columns to match the expected format
    df = pd.DataFrame(all_metrics)
    
    # Ensure all required columns are present
    required_columns = [
        'task_id', 'flow_constructs', 'recursions', 'nesting_depth',
        'data_structures', 'function_calls', 'length', 'CC'
    ]
    
    # Add missing columns with default value 0
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0
    
    # Reorder columns and sort by task_id
    df = df[required_columns].sort_values('task_id')
    
    # Save to CSV
    df.to_csv(output_csv, index=False)
    print(f"Analysis complete. Results saved to {output_csv}")
    print(f"Analyzed {len(df)} files")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze difficulty of Python tasks in a directory')
    parser.add_argument('input_dir', help='Directory containing Python task files')
    parser.add_argument('--output', '-o', default='complexity.csv',
                      help='Output CSV file path (default: complexity.csv)')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.input_dir):
        print(f"Error: Directory not found: {args.input_dir}")
    else:
        analyze_benchmark_directory(args.input_dir, args.output)
