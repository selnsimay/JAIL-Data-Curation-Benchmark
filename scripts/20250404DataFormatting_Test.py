#imports 
import json

with open('../data/geneset_dict.json', 'r') as f:
    dataset = json.load(f)

#creating a loop function that creates question based on the keys and answers 
def answer_question_pairs(dataset):
    """
    This function takes in the geneset dataset to match keys with specific questions.

    Parameters
    ----------
    dataset: list of dictionaries, containing gene information

    Returns
    -------
    qa_pairs: dict of question and answer pairs
    """

    #question_key_map: mapping from questions to JSON keys
    question_key_map = {
        "What is the ENSEMBL id of {Name}?": "Gene_ID",
        "What is the symbol of {Name}?": "Symbol",
        "What is the name of the gene with the symbol of {Symbol}?": "Name",
        "What are the other aliases for {Symbol}?": "Aliases",
        "What are the synonyms for the gene {Name}?": "Other names",
        "What is the function of the gene {Name}?": "Description"
    }

    #initialize an empty list to store question-answer pairs
    qa_pairs = []

    #iterate through each entry in the dataset
    for entry in dataset:
        for question_template, answer_key in question_key_map.items():
            #some values in the dataset may be empty or "N/A", filter them out
            answer = entry.get(answer_key)
            if not answer or answer == "N/A":
                continue

            #to personalize the question for the llm to separate them easily, format the question to accept keys
            try:
                question = question_template.format(**entry)
            except KeyError:
                #skip if the entry doesn't contain a needed key for formatting
                continue

            #format list-type values to a string
            if isinstance(answer, list):
                answer = ", ".join(answer)
            #append the question-answer pair to the list
            qa_pairs.append({
                "question": question,
                "answer": answer
            })

    return qa_pairs

#call the function to get the question-answer pairs. currently trying the first 3 elements
qa_pairs = answer_question_pairs(dataset)

#save the question-answer pairs to a JSON file
output_file = '../qa_pairs.json'

with open(output_file, 'w') as f:
    json.dump(qa_pairs, f, indent=4)

print(f"QA pairs saved to {output_file}")


 
    
    