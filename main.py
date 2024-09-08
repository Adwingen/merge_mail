#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Return all lines in the file, as a list where each line is an item in the list object
with (open
          (r".\Input\Names\invited_names.txt", "r") as file):
    list_names = file.readlines()
    print(list_names)

for names in list_names:
    with open(r".\Input\Letters\starting_letter.txt", "r") as file:
        letter_content = file.read()
        letter_content = letter_content.replace("[name]", names.strip())

    with open(r".\Output\ReadyToSend\letter_for_" + names.strip() + ".txt", "w") as file:
        file.write(letter_content)