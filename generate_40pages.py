import os

def process_file(in_path, out_path, title):
    with open(in_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    day_rows = []
    for line in lines:
        if line.strip().startswith('|') and 'Day ' in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 6:
                status = parts[3]
                if status.startswith('Day '):
                    day_num = int(status.replace('Day ', ''))
                    day_rows.append((day_num, line.strip()))
                    
    # Sort strictly by day number just in case
    day_rows.sort(key=lambda x: x[0])
                    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"# {title} - 40 Pages Log Book Layout\n\n")
        f.write(f"> **Note:** This document organizes the 74 working days into exactly 40 pages for the physical log book. The first 34 pages contain 2 days each, and the final 6 pages contain 1 day each.\n\n")
        
        day_idx = 0
        for page in range(1, 41):
            f.write(f"## Page {page}\n\n")
            f.write("| Date | Day | Status | Task | Description |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            
            days_in_page = 2 if page <= 34 else 1
            for _ in range(days_in_page):
                if day_idx < len(day_rows):
                    f.write(day_rows[day_idx][1] + "\n")
                    day_idx += 1
            f.write("\n")

process_file(r'f:\Intrentship\6th-Sem-Optimized(intership)-Boys.md', r'f:\Intrentship\6th-Sem-Optimized(intership)-Boys-40pages.md', 'Optimized Internship Calendar with Tasks (Boys)')
process_file(r'f:\Intrentship\6th-Sem-Optimized(intership)-Girls.md', r'f:\Intrentship\6th-Sem-Optimized(intership)-Girls-40pages.md', 'Optimized Internship Calendar with Tasks (Girls)')

print("Files generated!")
