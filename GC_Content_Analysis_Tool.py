# GC Content Analysis Tool

def calculate_gc_content(dna_sequence):
    sequence = dna_sequence.upper()  # Case-insensitive
    gc_count = sequence.count('G') + sequence.count('C')
    total_count = len(sequence)
    
    if total_count == 0:
        return 0.0

    gc_percentage = (gc_count / total_count) * 100
    return gc_percentage

# Run the tool
if __name__ == "__main__":
    dna_input = input("Enter a DNA sequence: ")
    gc_content = calculate_gc_content(dna_input)
    print(f"GC Content: {gc_content:.2f}%")
