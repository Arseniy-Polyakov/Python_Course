import re
import PyPDF2
from huggingface_hub import InferenceClient

def question_answering(question):
    #Model Choosing
    model_name = "Qwen/Qwen2.5-72B-Instruct"
    client = InferenceClient(model_name, token='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') 

    # #PDF Parsing
    # FILE_PATH = "grammar.pdf"
    # with open(FILE_PATH, mode="rb") as file:
    #     reader = PyPDF2.PdfReader(file)
    #     pages = len(reader.pages)
    #     page = reader.pages[0]
    #     text_from_pdf = []
    #     for i in range(len(reader.pages)):
    #         page = reader.pages[i]
    #         text_page = page.extract_text()
    #         text_from_pdf.append(text_page)
    #     text_from_pdf_str = "".join(text_from_pdf)

    # # Text preprocessing
    # rag_text = re.sub(r"[^A-Za-z ]", "", text_from_pdf_str)

    def llm_inference(question): 
        output = client.chat.completions.create(
            messages =  [{"role": "system", "content": "You are an english teacher at the linguistics university.\n"
                                        "Answer the questions based on the english grammar topic\n"
                                        "Do not use special symbols such as #* in your answer"},
                        {"role": "user", "content": f"Explain the concept of {question}"}
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
    answer = "".join(question_answering(question))
    return answer
