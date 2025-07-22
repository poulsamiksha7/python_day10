##Q1  Day 10 - 20 Jul 2025: File Handling- Read from a text file
# file= open("example.txt","r")
# content= file.read()
# print("Hello Samiksha Poul")
# print(content)
# file.close()

##Q2 Write to a file
# file=open("example.txt","w")
# file.write("Hello Samiksha\n")
# file.write("This will open in example.txt\n")
# file.close()

##Q3  Append data to file
# file=open("example.txt","a")
# file.write("Hello World\n")
# file.write("This will be also get printed on example.txt")
# file.close()

##Q4  Count lines, words, characters
# file=open("example.txt","r")
# lines=file.readlines()
# line_count=len(lines)
# word_count=0
# char_count=0
# for line in lines:
#     word_count+=len(line.split())
#     char_count+=len(line)
# file.close()

# print("File Analysis")
# print(f"Total lines {line_count}")
# print(f"Total Words {word_count}")
# print(f"Total Char Count {char_count}")

##QQ5 - Copy file content
# source_file=open("example.txt","r")
# destinantion_file = open("copy_example.txt","w")
# content=source_file.read()
# destinantion_file.write(content)
# source_file.close()
# destinantion_file.close()

##Q6  Search a word in file
# search_word=input("Enter the Word you want to Search")
# file=open("example.txt","r")
# lines=file.readlines()
# found=False
# count=0

# for line_num , line in enumerate(lines,start=1):
#     if search_word.lower() in line.lower():
#         print(f"Found the line {line_num}: {line.strip()}")
#         count+=line.lower().count(search_word.lower())
#         found=True
# if not found:
#     print("❌ Word not found in the file.")
# else:
#     print(f"\n🔁 Total occurrences of '{search_word}': {count}")
# file.close()

##Q7- Replace words in file
# with open("example.txt","r") as file:
#     content=file.read()

# old_word="Samiksha"
# new_word="World"
# updated_content=content.replace(old_word,new_word)

# with open("example.txt","w") as file:
#     file.write(updated_content)

# print(f"Replaced all occurrences of '{old_word}' with '{new_word}' in the file.")

##Q8 - Remove blank lines
# with open("example.txt","r") as file:
#     lines=file.readline()

# non_blank_lines=(line for line in lines if line.strip() !="")

# with open("example.txt","w") as file:
#     file.writelines(non_blank_lines)
# print("Blank lines removed successfully!")

##Q9 - File word frequency counter
# from collections import Counter

# with open("example.txt","r") as file:
#     text= file.read()

# words= text.lower().split()

# words=[word.strip(".,!?:;\"()[]") for word in words]
# words_coun=Counter(words)
# for word, count in words_coun.items():
#    print(f"{word}:{count}")

##Q10 - Merge two files
with open("example.txt","r") as file:
    content1=file.read()
with open("example.txt","r") as file:
    content2=file.read()
merged_content=content1+"\n"+content2

with open("example.txt","w") as merged_file:
  merged_file.write(merged_content)
  
print("Files merged successfully into merged.txt!")





