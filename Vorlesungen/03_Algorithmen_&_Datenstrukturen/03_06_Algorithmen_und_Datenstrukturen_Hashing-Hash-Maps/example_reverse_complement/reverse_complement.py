"""
This script should provide the function "reverse_complement" that takes a DNA sequence as input and returns the reverse complement of the sequence.
"""

def reverse_complement(dna_sequence: str) -> str:
    translation_dict = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_list = []

    #ATGATCTCGTAA
    for base in dna_sequence:
        if base in translation_dict.keys():
            reverse_list.append(translation_dict[base])
        else:
            reverse_list.append("_")

    reverse_list.reverse()
    return "".join(reverse_list)

if __name__ == "__main__":
    print(reverse_complement("ATGALTCTCGTAA"))