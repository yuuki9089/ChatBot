from llama_cpp import Llama
import logging

logging.getLogger("llama").setLevel(logging.ERROR)

llm = Llama(
    model_path="C:/Users/yuuki/Desktop/working/ChatBot/models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",
    chat_format="llama-3",
    n_ctx=1024,
)


# question = input("\n入力してください\n＞ ")
def Generate_ans(question):
    response = llm.create_chat_completion(
        messages=[
            {
                "role": "system",
                "content": "あなたは誠実で優秀な日本人のアシスタントです。特に指示が無い場合は、常に日本語で回答してください。",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        max_tokens=1024,
    )
    ans = response["choices"][0]["message"]["content"]
    return ans 

# print(response["choices"][0]["message"]["content"])
