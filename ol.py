import requests
import json
import os
import sys
import shutil


myTopic = sys.argv[1]



# Example usage
file_name = "example.txt"  # Replace with your file name
directory_name = "backup_folder"  # Replace with your target directory



def write_text_to_markdown(folder_name, text):
    # Ensure the folder exists
    os.makedirs(folder_name, exist_ok=True)
    
    # Define the file path
    file_path = os.path.join(folder_name, "markdown.md")
    
    # Write each character to the file
    with open(file_path, "w", encoding="utf-8") as file:
        for char in text:
            file.write(char)
    
    print(f"File 'markdown.md' created in '{folder_name}'.")

# Example usage
file_path = "markdown.md"  # Replace with your file path


# Define the URL and the payload
url = 'http://localhost:11434/api/generate'
payload = {
    "model": "llama3.2",
    "prompt": "create a markdown.md using about " + myTopic + " , use the following rules : dont use single * symbol, # for main headings ( h1) ## for subheadings (h2) , ### for smaller subheadings (h3) , ** bold text ** for bold text , '\n\n' , not literal characters , double new line as a new line character "
}

# Convert the payload to a JSON string
data = json.dumps(payload)

# Make the POST request
response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    list_dict_words = []
    for each_word in response.text.split("\n"):
        try:
            data = json.loads(each_word) 
        except:
            pass
        list_dict_words.append(data)
        
llama_response = " ".join([word['response'] for word in list_dict_words if type(word) == type({})])
write_text_to_markdown(myTopic,llama_response)
print(llama_response)
os.system('cp create.py ' + myTopic)


