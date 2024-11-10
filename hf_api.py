import re
import PyPDF2
from huggingface_hub import InferenceClient

#Model Choosing
model_name = "Qwen/Qwen2.5-72B-Instruct"
client = InferenceClient(model_name, token='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') 

#PDF Parsing
FILE_PATH = "grammar.pdf"
with open(FILE_PATH, mode="rb") as file:
    reader = PyPDF2.PdfReader(file)
    pages = len(reader.pages)
    page = reader.pages[0]
    text_from_pdf = []
    for i in range(len(reader.pages)):
      page = reader.pages[i]
      text_page = page.extract_text()
      text_from_pdf.append(text_page)
text_from_pdf_str = "".join(text_from_pdf)

# Text preprocessing
rag_text = re.sub(r"[^A-Za-z ]", "", text_from_pdf_str)
first_part = rag_text[:100000]

def llm_inference(user_sample): 
    output = client.chat.completions.create(
        messages =  [{"role": "system", "content": "You are an english teacher at the linguistics university.\n"
                                      "Answer the questions based on the english grammar topic"},
                    {"role": "user", "content": f"Explain the concept of {user_sample}"}
        ], 
        stream=False,
        max_tokens=128,
        temperature=0.5,
        top_p=0.1
    )

user_sample = ["gerund", "article", "tense"]

outputs = [llm_inference(item) for item in user_sample]

for output in outputs:
    # print('== OUTPUT ==')
    # print(output.model)
    # print(output.usage)
    # print()
    for choice in output.choices:
        print(choice.get('message')['content'])
        print(choice.get('message')['role'])
        print(choice.get('message')['tool_calls'])
    print()
   
                         