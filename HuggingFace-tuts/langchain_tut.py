from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error

set_verbosity_error()


model = pipeline("summarization",model="facebook/bart-large-cnn")


llm = HuggingFacePipeline(pipeline=model)

template = PromptTemplate.from_template(
     "Summarize the following text in a way a {age} year old would understand:\n\n{text}"
)

summarize_chain = template | llm

text_to_summarizer = input("Enter text to summarize : \n")
age = input("Enter target age for summarizing for : \n")

summary = summarize_chain.invoke({"text":text_to_summarizer, "age":age})

print("\n **Generated Summary :** ")
print(summary)

