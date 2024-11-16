import re
import PyPDF2
from huggingface_hub import InferenceClient
from web_scrapping import *
from files_parsing import *
from pdf import *

def question_answering_grammar(question):
    #Model Choosing
    model_name = "meta-llama/Llama-3.2-1B"
    client = InferenceClient(model_name, token='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') 

    def llm_inference(question): 
        output = client.chat.completions.create(
            messages =  [{"role": "system", "content": "You are an english teacher at the linguistics university.\n"
                                        f"Answer the questions based on this students' book {pages_str_final}\n"
                                        "Do not use special symbols such as #* in your answer"},
                        {"role": "user", "content": f"Explain the concept of {question_grammar}"}
            ], 
            stream=False,
            max_tokens=128,
            temperature=0.5,
            top_p=0.1
        )
        return output

    outputs = llm_inference(question)
    answer = []
    for output in outputs.choices:
        answer.append(output.get('message')['content'])
    answer = "".join(question_answering_grammar(question))
    return answer

def question_answering_ielts(question):
    #Model Choosing
    model_name = "meta-llama/Llama-3.2-1B"
    client = InferenceClient(model_name, token='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') 

    def llm_inference(question): 
        output = client.chat.completions.create(
            messages =  [{"role": "system", "content": "You are a consultant for international English exam (IELTS).\n"
                                        f"Answer the questions connected with IELTS based on this text {text_final} \n"
                                        "Do not use special symbols such as #* in your answer"},
                        {"role": "user", "content": f"Explain the concept of {question_ielts}"}
            ], 
            stream=False,
            max_tokens=128,
            temperature=0.5,
            top_p=0.1
        )
        return output

    outputs = llm_inference(question)
    answer = []
    for output in outputs.choices:
        answer.append(output.get('message')['content'])
    answer = "".join(question_answering_ielts(question))
    return answer

def question_answering_universities(question):
    #Model Choosing
    model_name = "meta-llama/Llama-3.2-1B"
    client = InferenceClient(model_name, token='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') 

    def llm_inference(question): 
        output = client.chat.completions.create(
            messages =  [{"role": "system", "content": f"You are a consultant. Your aim is to answer questions based on this text {universities_final}\n"
                                        "Answer the questions based on the english universities\n"
                                        "Do not use special symbols such as #* in your answer"},
                        {"role": "user", "content": f"Anwer the following question {question_universities}"}
            ], 
            stream=False,
            max_tokens=128,
            temperature=0.5,
            top_p=0.1
        )
        return output

    outputs = llm_inference(question)
    answer = []
    for output in outputs.choices:
        answer.append(output.get('message')['content'])
    answer = "".join(question_answering_universities(question))
    return answer


question_ielts = input("Ask a question: ")
final = question_answering_ielts(question_ielts)
print(final)