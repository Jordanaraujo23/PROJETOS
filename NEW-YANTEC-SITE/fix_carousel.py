
import sys

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Line 200 in 1-based is index 199
    start_idx = 199 
    
    # Check if we are at the right place
    if 'id="municipios-carousel"' not in lines[start_idx]:
        print(f"Error: Line 200 content mismatch: {lines[start_idx].strip()}")
        # Fallback search for the ID
        found = False
        for i, line in enumerate(lines):
             if 'id="municipios-carousel"' in line:
                 start_idx = i
                 found = True
                 break
        if not found:
            print("Critical Error: Start tag not found.")
            sys.exit(1)

    # Find the closing div. It should be the indented </div>
    # The previous file had it at line 230 (index 229).
    # We will search forward from start_idx
    end_idx = -1
    for i in range(start_idx + 1, len(lines)):
        # Looking for the closing div that matches the indentation approximately or just the next significant </div>
        # Given the mess, the user might have weird indentation.
        # But based on view_file, line 230 was `            </div>`
        if lines[i].strip() == '</div>':
             # Check if it looks like the main closing div.
             # In the file, the next section starts at line 231 (index 230) </div> </div> is possible?
             # Let's assume the first </div> that is alone on the line with same indentation as start?
             # Start has 12 spaces indentation.
             current_indent = len(lines[start_idx]) - len(lines[start_idx].lstrip())
             line_indent = len(lines[i]) - len(lines[i].lstrip())
             if line_indent == current_indent:
                 end_idx = i
                 break
    
    if end_idx == -1:
        print("Error: Could not find closing div.")
        sys.exit(1)

    print(f"Replacing lines {start_idx+1} to {end_idx+1}")

    # Generate new content
    new_content = []
    # Preserve original usage of indentation?
    indent = " " * 12
    new_content.append(lines[start_idx]) # The opening div
    
    for i in range(1, 41):
        # Using <img> as standard, removing <image> error
        # Assuming filename {i}.svg
        new_content.append(f'{indent}    <div class="item"><img src="./YanTec_files/{i}.svg" class="mun-logo mb-2"><h6 class="mt-2 fw-semibold text-muted">Município</h6></div>\n')
    
    new_content.append(lines[end_idx]) # The closing div

    final_lines = lines[:start_idx] + new_content + lines[end_idx+1:] # Replacing the block inclusive of start/end? 
    # Wait, my new_content INCLUDES start and end lines?
    # No, replacement logic:
    # lines[:start_idx] -> 0 to start-1
    # new_content -> start to end
    # lines[end_idx+1:] -> end+1 to END
    # But wait, looking at my code above:
    # new_content has `lines[start_idx]` (header) and `lines[end_idx]` (footer).
    # So I need to replace the range [start_idx, end_idx] inclusive.
    # Python slice replacement: list[start:end+1] = new_content
    # Yes.
    
    # But explicitly constructing list:
    # lines[:start_idx] excludes start_idx. Correct.
    # new_content includes start and end. Correct.
    # lines[end_idx+1:] excludes end_idx. Correct.
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

    print("Success")

except Exception as e:
    print(f"Exception: {e}")
    sys.exit(1)
