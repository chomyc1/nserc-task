import requests
import json

def main():
    matched_word = "Fix" # This can be changed to a different word
    word_length = len(matched_word)
    repository_name = input("Enter a GitHub repository name: ")
    username = input("Enter the username of the GitHub repository owner: ")
    response = requests.get("https://api.github.com/repos/" + username + "/" + repository_name + "/commits")

    if (response.ok): # If the entered repository is valid
        commit_list = json.loads(response.text)
        output_file = open("output.csv", "w")
        output_file.write("Commit SHA, Commit message\n")

        # Iterate through commit_list, find commits with matched_word in their message, output their SHA and message
        for commit in commit_list:
            commit_message = commit["commit"]["message"]

            # Iterate through the characters in a message, stop if matched_word cannot fit in the remaining portion of the message
            for i in range(0, (len(commit_message) - word_length + 1)):
                matched_characters = 0
                
                # Compare current character in commit_message and first character in matched_word. If they match, check the next character of both
                for j in range(0, word_length):
                    if (commit_message[i+j] == matched_word[j]):
                        matched_characters += 1
                    else:
                        break
                
                if (matched_characters == word_length): # If matched_word is found in commit_message
                    output_file.write(commit["sha"] + "," + commit_message + "\n")
                    break
        output_file.close()
        print("Output written to output.csv.")

    else:
        print("Invalid repository specified.")
        return
    
main()
