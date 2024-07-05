from retrieve_context import embedd_query, get_matches, get_sentence_ids, get_context
from openai_inference import get_answer_to_question

query = input("Input Question:")
embedded_query = embedd_query(query)
matches = get_matches(embedded_query)
ids = get_sentence_ids(matches)
context = get_context(ids)
print(get_answer_to_question(question=query, retrieved_context=context))