from hf_api import * 
question = input("Ask a question about grammar: ")
answer = "".join(question_answering(question))
print(answer)