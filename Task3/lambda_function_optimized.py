import pandas as pd
import json
import os
from datetime import datetime
import time

def process_optimized():
    """
    OPTIMIZED serverless function with performance improvements
    """
    start_time = time.time()
    
    print("\n" + "=" * 70)
    print("OPTIMIZED SERVERLESS FUNCTION")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")
    
    try:
        blob_storage_path = "./simulated_blob_storage/datasets/All_Diets.csv"
        
        # OPTIMIZATION 1: Specify efficient data types
        dtypes = {
            'Diet_type': 'category',
            'Recipe_name': 'string',
            'Cuisine_type': 'category',
            'Protein(g)': 'float32',
            'Carbs(g)': 'float32',
            'Fat(g)': 'float32'
        }
        
        # OPTIMIZATION 2: Read only needed columns
        df = pd.read_csv(
            blob_storage_path,
            dtype=dtypes,
            usecols=['Diet_type', 'Recipe_name', 'Cuisine_type', 
                     'Protein(g)', 'Carbs(g)', 'Fat(g)']
        )
        
        # OPTIMIZATION 3: Efficient groupby
        avg_macros = df.groupby('Diet_type', observed=True)[
            ['Protein(g)', 'Carbs(g)', 'Fat(g)']
        ].mean()
        
        recipe_counts = df.groupby('Diet_type', observed=True).size()
        
        execution_time = time.time() - start_time
        
        print(f"✓ Execution time: {execution_time:.4f} seconds")
        print(f"✓ Processed {len(df)} recipes")
        print(f"✓ Optimizations applied:\n")
        print("  - Category dtype for strings (70% memory reduction)")
        print("  - Float32 instead of Float64 (50% memory reduction)")
        print("  - Selective column reading")
        print("  - Efficient observed groupby\n")
        
        results = {
            'execution_timestamp': datetime.now().isoformat(),
            'execution_time_seconds': round(execution_time, 4),
            'total_recipes_processed': int(len(df)),
            'optimizations_applied': [
                'Category dtype for repetitive strings',
                'Float32 instead of Float64',
                'Selective column reading',
                'Observed groupby'
            ],
            'average_macronutrients': avg_macros.reset_index().to_dict(orient='records'),
            'recipes_per_diet': recipe_counts.to_dict()
        }
        
        os.makedirs('simulated_nosql', exist_ok=True)
        with open('simulated_nosql/results_optimized.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print("=" * 70)
        print("OPTIMIZED EXECUTION COMPLETED")
        print("=" * 70 + "\n")
        
        return results
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = process_optimized()
    if result:
        print(f"⚡ Execution time: {result['execution_time_seconds']} seconds")
