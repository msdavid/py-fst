import pandas as pd
import os
from pyfst import read_fst, write_fst

# Create a sample DataFrame
df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5],
    'b': ['x', 'y', 'z', 'p', 'q'],
    'c': [True, False, True, False, True]
})

print("Original DataFrame:")
print(df)

# Define output file path
output_file = 'test_data.fst'

try:
    # Write to FST file
    write_fst(df, output_file, compress=50)
    print(f"\nWrote data to {output_file}")
    print(f"File size: {os.path.getsize(output_file)} bytes")
    
    # Read from FST file
    df_read = read_fst(output_file)
    print("\nRead entire DataFrame:")
    print(df_read)
    
    # Read specific columns
    df_cols = read_fst(output_file, columns=['a', 'c'])
    print("\nRead specific columns (a, c):")
    print(df_cols)
    
    # Read specific rows
    df_rows = read_fst(output_file, from_=1, to=3)
    print("\nRead specific rows (1-3):")
    print(df_rows)
    
    # Check if data is preserved correctly
    if df.equals(df_read):
        print("\n✅ Test passed: Data read matches data written")
    else:
        print("\n❌ Test failed: Data read doesn't match data written")
        
except Exception as e:
    print(f"\n❌ Error: {e}")
finally:
    # Clean up
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"\nRemoved test file: {output_file}")