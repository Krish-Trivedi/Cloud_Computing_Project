import pandas as pd
import json
import os
from datetime import datetime

def process_nutritional_data():
    """
    Simulated serverless function - processes data from simulated blob storage
    """
    print("\n" + "=" * 70)
    print("SERVERLESS FUNCTION EXECUTION")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")
    
    try:
        # Step 1: Connect to simulated blob storage
        print("[1/5] Connecting to simulated Blob Storage...")
        blob_storage_path = "./simulated_blob_storage/datasets/All_Diets.csv"
        
        if not os.path.exists(blob_storage_path):
            raise FileNotFoundError(f"Blob not found: {blob_storage_path}")
        
        print(f"      ✓ Connected to: {os.path.abspath(blob_storage_path)}\n")
        
        # Step 2: Download blob
        print("[2/5] Reading blob data...")
        file_size = os.path.getsize(blob_storage_path)
        print(f"      ✓ Blob size: {file_size:,} bytes\n")
        
        # Step 3: Load into Pandas
        print("[3/5] Processing data with Pandas...")
        df = pd.read_csv(blob_storage_path)
        print(f"      ✓ Loaded {len(df)} recipes")
        print(f"      ✓ Columns: {list(df.columns)}\n")
        
        # Step 4: Calculate nutritional insights
        print("[4/5] Calculating nutritional insights...")
        
        # Average macronutrients per diet type
        avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
        
        # Count recipes per diet
        recipe_counts = df.groupby('Diet_type').size()
        
        # Top protein recipe
        max_protein_idx = df['Protein(g)'].idxmax()
        top_protein_recipe = df.loc[max_protein_idx]
        
        print("\n      --- ANALYSIS RESULTS ---")
        print("\n      Average Macronutrients by Diet Type:")
        print(avg_macros.to_string(float_format='%.2f'))
        print(f"\n      Recipe Counts by Diet Type:")
        print(recipe_counts.to_string())
        print(f"\n      Highest Protein Recipe:")
        print(f"      - Name: {top_protein_recipe['Recipe_name']}")
        print(f"      - Diet: {top_protein_recipe['Diet_type']}")
        print(f"      - Protein: {top_protein_recipe['Protein(g)']}g")
        print(f"      - Carbs: {top_protein_recipe['Carbs(g)']}g")
        print(f"      - Fat: {top_protein_recipe['Fat(g)']}g\n")
        
        # Step 5: Save to simulated NoSQL
        print("[5/5] Saving results to simulated NoSQL database...")
        
        results = {
            'execution_timestamp': datetime.now().isoformat(),
            'storage_simulation': 'file-based blob storage (Azurite alternative)',
            'total_recipes_processed': int(len(df)),
            'average_macronutrients': avg_macros.reset_index().to_dict(orient='records'),
            'recipes_per_diet': recipe_counts.to_dict(),
            'top_protein_recipe': {
                'name': str(top_protein_recipe['Recipe_name']),
                'diet_type': str(top_protein_recipe['Diet_type']),
                'cuisine': str(top_protein_recipe['Cuisine_type']),
                'protein_g': float(top_protein_recipe['Protein(g)']),
                'carbs_g': float(top_protein_recipe['Carbs(g)']),
                'fat_g': float(top_protein_recipe['Fat(g)'])
            }
        }
        
        # Save results
        os.makedirs('simulated_nosql', exist_ok=True)
        output_file = 'simulated_nosql/results.json'
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"      ✓ Results saved to: {output_file}\n")
        
        print("=" * 70)
        print("EXECUTION COMPLETED SUCCESSFULLY")
        print("=" * 70 + "\n")
        
        return results
        
    except Exception as e:
        print(f"\n❌ ERROR OCCURRED: {str(e)}\n")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("\n🚀 Starting Serverless Function Simulation...\n")
    result = process_nutritional_data()
    
    if result:
        print(f"✅ SUCCESS! Processed {result['total_recipes_processed']} recipes")
        print(f"📊 Results stored in simulated NoSQL database")
    else:
        print("❌ Function execution failed!")
