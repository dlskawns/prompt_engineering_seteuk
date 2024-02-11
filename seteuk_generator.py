from langchain.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate,PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate, AIMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback
import time
from prompts import promptSeteuk

class seteukGenerator():
    def __init__(self):
        self.llm_normal = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.8, max_tokens=1500)
        # self.llm_16k = ChatOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0.8, max_tokens=1500)
        self.prom = promptSeteuk()
        response_schemas= [
            ResponseSchema(name="ig", description="content of introduction part"),
            ResponseSchema(name="bg", description="content of body part"),
            ResponseSchema(name="cg", description="content of conclusion part"),
            ]
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        self.format_instructions = output_parser.get_format_instructions()

    def getCriteria(self, keyword, criteria):
        """
        적합한 성취기준명을 골라 이유와 함께 생성 및 출력합니다.
        keyword: 전공 키워드 issue -> String
        criteria: 성취기준명 -> List
        """
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(self.prom.criteria_system),
                HumanMessagePromptTemplate.from_template(self.prom.criteria_human)
                ],
            input_variables = ['keyword', 'criteria'],
        )
        _input = prompt.format_prompt(keyword = keyword, criteria=criteria)
        llm_16k = ChatOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0.8, max_tokens=1500)
        with get_openai_callback() as cb:
            print('---------------------------------------getCriteria 작업시작')
            start = time.time()
            output = llm_16k.invoke(_input.to_messages())
            end = time.time()
            print(f'answer: {output.content}')
            print(cb)
            print(f'{end - start} 경과')
        return output.content, cb.total_cost
    

    def getTopic(self, keyword, criteria):
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(self.prom.topic_system),
                HumanMessagePromptTemplate.from_template(self.prom.topic_human)
                ],
            input_variables = ['keyword', 'criteria'],
        )
        _input = prompt.format_prompt(keyword = keyword, criteria=criteria)
        llm_16k = ChatOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0.8, max_tokens=1500)
        with get_openai_callback() as cb:
            print('---------------------------------------getTopic 작업시작')
            start = time.time()
            output = llm_16k.invoke(_input.to_messages())
            end = time.time()
            print(f'answer: {output.content}')
            print(type(cb))
            print(f'{end - start} 경과')
        return output.content, cb.total_cost


    def getGuideLines(self, topic, major, keyword, reference):
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(self.prom.guideLine_system),
                HumanMessagePromptTemplate.from_template(self.prom.guideLine_human)
                ],
            input_variables = ['keyword', 'topic', 'major', 'reference'],
            partial_variables={"format_instructions": self.format_instructions}
        )
        _input = prompt.format_prompt(major = major, keyword = keyword, topic=topic, reference=reference)
        llm_16k = ChatOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0.8, max_tokens=1500)
        with get_openai_callback() as cb:
            print('---------------------------------------getGuideLines 작업시작')
            start = time.time()
            output = llm_16k.invoke(_input.to_messages())
            end = time.time()
            print(f'answer: {output.content}')
            print(cb)
            print(f'{end - start} 경과')
        return output.content, cb.total_cost
