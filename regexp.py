#!/usr/bin/python3
import re

# open the input file for reading
file = open('mountain.html')
# read the entire file
with open('mountain.html', 'r', encoding='utf-8', errors='ignore') as file:
    text = file.read()
# split into lines
lines = text.splitlines()

print("0. Example: All tags.")
matches = re.findall(r'<[^>]+>', text)
for s in matches:
    print(s)
print("total: ", len(matches))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 1. Extract all script tags and their contents.
print("1. Script tags and their contents:")
# Print only first 100 chars for preview
script_matches = re.findall(r'<script[^>]*?>.*?</script>', text, re.DOTALL)
# Print only first 100 chars for preview
print(script_matches[0][:100])
print("Total:", len(script_matches))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 2. Find all meta tags that include a content attribute.
print("\n2. Meta tags with 'content' attribute:")
meta_tags = re.findall(r'<meta[^>]*\scontent\s*=\s*["\'](.*?)["\'][^>]*>', text, re.IGNORECASE)
for s in meta_tags:
    print(s)
print("Total:", len(meta_tags))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 3. Find lines containing at least two tags, where those tags have a name with three or more characters.
print("3. Lines containing at least two tags, where those tags have a name with three or more characters.")
pattern = r'<([a-zA-Z]{3,})[^>]*>'  # Set capturing group to get tags have a name with three or more characters
lines = text.split("\n")
s = 0
for line in lines:
    matches = re.findall(pattern, line)
    if len(set(matches)) >= 2:  # After deduplicating the matches list, ensure that the number of unique tuples is at least two, indicating at least two tags.
        s = s + 1
        print(line)
print("total:", s)

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 4. Find all words in bold.
print("\n4. Words in bold:")
pattern = r'<b[^>]*>(?:<i[^>]*>([a-zA-Z\s].*?)</i>|([a-zA-Z\s]*))</b>|(?:style=["\'].*?font-weight:\s*bold.*?["\'][^>]*>(.*?)<)'
bold_texts = re.findall(pattern, text, re.IGNORECASE)

filtered_bold_texts = []
for match in bold_texts:
    # Three capture groups:
    # i_bold = <b><i>([a-zA-Z\s].*?)</i></b>
    # normal_bold = <b>([a-zA-Z\s]*)</b>
    # style_bold = <span style="font-weight:bold;">(.*?)</span>
    i_bold, normal_bold, style_bold = match
    if i_bold:  # Deal with <b><i>...</i></b>
        filtered_bold_texts.append(i_bold)
    elif normal_bold:  # Deal with normal <b>...</b>
        filtered_bold_texts.append(normal_bold)

for s in filtered_bold_texts:
    print(s)
print("Total:", len(filtered_bold_texts))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 5. Find all Div tags with id that contains *im*."
print("5. Div tags with id that contains *im*.")
# Example: <div id="himg"> or <div class="imgc" id="imgcont">
matches = re.findall(r'<div[^>]*\bid\s*=\s*"[^"]*im[^"]*"[^>]*>', text)
for s in matches:
    print(s)
print("total: ", len(matches))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 6. Find the value of the href attribute in the <a> tags.
print("6. The value of the href attribute in the <a> tags.")
# Print just the values.  
# Example: http://app.dictionary.com/favorites
matches = re.findall(r'<a\s*[^>]*\s*href\s*=\s*["\']+([^"\']*)["\']+[^>]*>', text, re.IGNORECASE)
for s in matches:
    print(s)
print("total: ", len(matches))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 7. Find the Lines containing a <div> tag that has a class attribute with a value containing the string 'tx'.
print("\n7. Lines containing a <div> tag that has a class attribute with a value containing the string 'tx'.")
# Replace tx with TX and preserve other attributes (if any).
# Example: replace <div class="ftxt1" style="display:block;width:350px;"> with <div class="fTXt1" style="display:block;width:350px;">
pattern = r'(<div[^>]*class=["\']*[^"\']*)tx([^"\']*["\']*[^>]*>)'
lines = text.split('\n')
s = 0
for line in lines:
    new_line = re.sub(pattern, r'\1TX\2', line)
    if new_line != line:
        s = s + 1
        print(new_line)
print("total: ", s)

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 8. Find the content of all style tags.
print("\n8. The content of all style tags.")
# Example: 
#   <style type="text/css">
#       ...
#       ...
#   </style>
pattern = r'(<style.*?>)(.*?)(</style>)'
matches = re.findall(pattern, text, re.DOTALL)
for s in matches:
    tag_start, tag_content, tag_end = s
    print(tag_start)
    for line in tag_content.strip().split('\n'):
        print(line.strip())
    print(tag_end)
print("total: ", len(matches))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 9. Find the synonyms of the word mountain listed in the file.
print("\n9. The synonyms of the word mountain listed in the file")
# Load mountain.html into a browser or text editor to see the list of synonyms.
pattern = r'<div\s+id="sY[^"]*[^>]*"><a[^>]*>([^>]+)</a>'
matches = re.findall(pattern, text)
for s in matches:
    print(s)
print("total: ", len(matches))

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

# 10. Replace all occurrences of 'Dictionary.com' with 'MyDictionary'.
print("\n10. Replace 'Dictionary.com' with 'MyDictionary'")
# Print only first 200 chars
modified_text = text.replace("Dictionary.com", "MyDictionary")
print(modified_text[:200])
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
