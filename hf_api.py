import re
import PyPDF2
from huggingface_hub import InferenceClient
from web_scrapping import *
from files_parsing import *
from pdf import *

# def question_answering_grammar(question_grammar):
#     #Model Choosing
#     model_name = "Qwen/Qwen2.5-72B-Instruct"
#     client = InferenceClient(model_name, token='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') 

#     def llm_inference(question_grammar): 
#         output = client.chat.completions.create(
#             messages =  [{"role": "system", "content": "You are an english teacher at the linguistics university.\n"
#                                         f"Answer the questions based on this students' book {pages_str_final}\n"
#                                         "Do not use special symbols such as #* in your answer"},
#                         {"role": "user", "content": f"Explain the concept of {question_grammar}"}
#             ], 
#             stream=False,
#             max_tokens=128,
#             temperature=0.5,
#             top_p=0.1
#         )
#         return output

#     outputs = llm_inference(question_grammar)
#     answer = []
#     for output in outputs.choices:
#         answer.append(output.get('message')['content'])
#     answer = "".join(question_answering_grammar(question_grammar))
#     return answer

from huggingface_hub import InferenceClient

model_name = "Qwen/Qwen2.5-72B-Instruct"

client = InferenceClient(model_name)

def llm_inference(user_sample):
  output = client.chat.completions.create(
          messages=[
              {"role": "system", "content": "you are an expert in english texts evaluation\n"
                                            f"evaluate the {user_sample}, focus on these metrics\n"
                                            "General information:\n"
                                            "1. The number of sentences in the text\n"
                                            "2. The number of words in the text\n"
                                            "3. The number of words (without stopwords) in the text\n"
                                            "4. The average number of words in the sentence\n"
                                            "5. The average number of words (without stopwords) in the text\n"
                                            "Phonological level:\n" 
                                            "1. The average number of syllables in the word\n"
                                            "2. The average number of syllables in the sentence\n"
                                            "3. The number of 1-syllable, 2-syllable, 3-syllable and 4-syllable words in the text\n"
                                            "4. The average number of 1-syllable, 2-syllable, 3-syllable and 4-syllable words in the sentence\n"
                                            "Grammatical level:\n"
                                            "1. The number of nouns in the text. Do not write nouns\n"
                                            "2. The number of adjectives in the text. Do not write adjectives\n"
                                            "3. The number of verbs in the text. Do not write verbs\n"
                                            "4. The number of adverbs in the text. Do not write adverbs\n"
                                            "5. The number of pronouns in the text. Do not write pronouns\n"
                                            "6. Text descriptivity: the number of adjectives divide to the whole number of all words in the text\n"
                                            "7. Text nominativity: the number of nouns divide to the whole number of all words in the text\n"
                                            "Lexical level:\n"
                                            "1. The number of A1, A2, B1, B2, C1, C2 words in the text\n"
                                            "2. The average number of A1, A2, B1, B2, C1, C2 words in the sentences\n"
                                            "3. The number of A1, A2, B1, B2, C1, C2 collocations in the text\n"
                                            "4. The average number of A1, A2, B1, B2, C1, C2 collocations in the sentences\n"
                                            "5. Type token ratio (TTR): TTR = (N / total words)\n"
                                            "where N - the number of all unique words in the text\n"
                                            "total words - the number of all words in the text.\n" 
                                            "For intanse: N = 120, total words = 240.\n" 
                                            "TTR = N / total words = 120 / 240 = 0.5\n"
                                            "6. Root Type Token Ratio (RTTR)\n"
                                            "7. Corrected Type Token Ratio (CTTR)\n"
                                            "Topic modeling:\n"
                                            "Name top 5 topics in the text\n"
                                            "Statistical metrics:\n"
                                            "1. Flesh Reading Ease (FRE)\n"
                                            "2. Flesh-Kincaid Grade Level (FKGL)\n"
                                            "3. LIX (Läsbarhetsindex)\n"
                                            "4. SMOG (Simple Measure of Gobbledygook)\n"
              },
              {"role": "user",
              "content": f"evaluate the text in english {user_sample} focusing on the mentioned metrics. If the text is written in other language say that you cannot evaluate this text"},
          ],
          stream=False,
          max_tokens=128,
          temperature=0.5,
          top_p=0.1
          )
  return output.choices[0].get('message')['content']

import gradio as gr

interface = gr.Interface(fn=llm_inference,
                        inputs=gr.Textbox(lines=2, placeholder="Write your text here..."),
                        outputs="text",
                        css=".gradio-container {background-image: url('https://i.pinimg.com/originals/9b/6a/a8/9b6aa8867dbe29f2d475b7a550e06490.jpg')}",
                        title="ENGLISH TEXT EVALUATION")

interface.launch(debug=True)

# def question_answering_universities(question_universities):
#     #Model Choosing
#     model_name = "Qwen/Qwen2.5-72B-Instruct"
#     client = InferenceClient(model_name, token='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') 

#     def llm_inference(question): 
#         output = client.chat.completions.create(
#             messages =  [{"role": "system", "content": f"You are a consultant. Your aim is to answer questions based on this text {universities_final}\n"
#                                         "Answer the questions based on the english universities\n"
#                                         "Do not use special symbols such as #* in your answer"},
#                         {"role": "user", "content": f"Anwer the following question {question_universities}"}
#             ], 
#             stream=False,
#             max_tokens=128,
#             temperature=0.5,
#             top_p=0.1
#         )
#         return output

#     outputs = llm_inference(question_universities)
#     answer = []
#     for output in outputs.choices:
#         answer.append(output.get('message')['content'])
#     answer = "".join(question_answering_universities(question_universities))
#     return answer


question_ielts = input("Ask a question: ")
final = llm_inference(question_ielts)
print(final)