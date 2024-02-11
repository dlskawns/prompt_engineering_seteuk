from prompts import promptSeteuk
from dotenv import load_dotenv
import pandas as pd
from seteuk_generator import seteukGenerator
import os
import json
load_dotenv()

def seteuk_main(major):
    """
    major: 전공
    subject: 세특 희망 교과목
    """
    ## 데이터 불러오기
    # 사례 데이터셋
    case_df = pd.read_excel(case_path, header = 0)

    # 성취 기준 데이터셋
    criteria_df = pd.read_excel(criteria_path,header = 0, sheet_name='전체(남준용)')
    # 전공 맞춤 과목 데이터셋
    subject_df = pd.read_excel(subject_path, header=0)

    # 선택 전공에 따른 전공 키워드 확인
    issues_lst = case_df[case_df['major']==major]['issue'].reset_index(drop=True)
    for num, issue in enumerate(issues_lst):
        print(f'press {num}: {issue}')

    # 키워드 선택
    print('원하는 원하는 전공 키워드 번호를 입력하세요')
    selected_keyword = issues_lst[int(input())]

    # 선택 전공 키워드에 따른 실제 사례 데이터 추출
    references = case_df[case_df['issue']==selected_keyword]['case'].values

    # 전공에 따른 맞춤형 과목 확인
    subject_major = subject_df[subject_df['전공']==major]
    for col in ['공통','일반선택','진로선택']:
        print(f'{major}전공 - {col}부문: {subject_major[col].values}')
    
    # 과목에 따른 성취기준 선택
    print(f'과목을 선택해 주세요. 정확히 타이핑해야합니다')
    subject = input()
    criterias = list(criteria_df[criteria_df['영역(단원)']==subject]['성취기준명'])
    
    
    # 세특 인스턴스 생성
    sg = seteukGenerator()

    # 성취기준명 설명 생성 GPT 실행
    first_answer, cost_1 = sg.getCriteria(selected_keyword, criterias)
    first_answer = eval(first_answer)

    # 성취기준명 선택    
    for num, each in enumerate(first_answer):
        print(f'press {num} : {each}')
    print('원하는 성취기준명을 골라주세요:')
    selected_criteria = first_answer[int(input())]


    # 선택된 성취기준을 통해 세특 주제를 생성 GPT 실행
    second_answer, cost_2 = sg.getTopic(selected_keyword, selected_criteria)
    print(second_answer)
    print(type(second_answer))
    second_answer = eval(second_answer)

    # 주제 선택
    for num, each in enumerate(list(second_answer)):
        print(f'press {num} : {each}')
    print('원하는 주제를 골라주세요:')
    selected_topic = second_answer[int(input())]    

    # 가이드라인 생성
    third_answer, cost_3 = sg.getGuideLines(selected_topic, major, selected_keyword, references)
    third_answer = json.loads(third_answer)
    print(type(third_answer))
    for part in ['ig','bg','cg']:
        print(third_answer[part])
    print(f'total cost: ${round((cost_1+cost_2+cost_3),2)}')

    

if __name__=='__main__':
    case_path= os.environ['case_path']
    criteria_path=os.environ['criteria_path']
    subject_path=os.environ['subject_path']
    print('희망 전공을 입력하세요.')
    seteuk_main(input())
    



