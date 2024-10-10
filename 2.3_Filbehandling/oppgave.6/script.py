#!/bin/python

#list
file1 = 'bruker_tekst_op2.txt'
file2 = 'bruker_tekst_op3.txt'

def combine_files(file1, file2, output_file):
    try:
        # Åpne begge input-filene for lesing
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            # Les innholdet fra hver fil
            content1 = f1.read()
            content2 = f2.read()
            
        # Kombiner innholdet fra begge filer
        combined_content = content1 + "\n" + content2
        
        # Åpne output-filen for skriving
        with open(output_file, 'w', encoding='utf-8') as out:
            # Skriv det kombinerte innholdet til output-filen
            out.write(combined_content)
        
        print(f"Kombinert innhold skrevet til {output_file}")
    
    except FileNotFoundError as e:
        print(f"Feil: {e}")

# Eksempel på hvordan scriptet kan brukes
output_file = 'kombinert_bruker_tekst_fil.txt'

combine_files(file1, file2, output_file)
