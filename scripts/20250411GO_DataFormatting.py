import json

with open('../data/go_terms_dict.json', 'r') as f:
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


