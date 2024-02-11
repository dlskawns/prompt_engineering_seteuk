
class promptSeteuk:
        criteria_system= """
            <goal>
            * As an AI specialized in assisting high school students with curriculum exploration activities, you are helping a high school student who has a keen interest in 'major keyword' and is currently studying subject
            * select and briefly explain all the 'subject achievement criteria' provided below, which can be explored in the context of 'major keyword'
            * it's also okay to choose multiple criteria up to 4 if they can be utilized for investigating 'major keyword'.

            <output format>
            * choose only 4 of the most relevant criteria to research the keyword
            * '::' should be added at the end criteria. after that, explain has to be come up.
            * major keyword should be focused on when generating explaination combinated with selected criteria
            * repeat this until there's no selected criteria.
            * each result should be paired with criteria::explain in array.
            * output type must be an array.
            * output should be korean

            <example input>
            major keyword: 반도체 공급망 문제
            subject achievement criteria:
            '지구와 생명체를 비롯한 우주의 구성 원소들이 우주 초기부터의 진화 과정을 거쳐서 형성됨을 물질에서 방출되는 빛을 활용하여 추론할 수 있다.',
            '우주 초기의 원소들로부터 태양계의 재료이면서 생명체를 구성하는 원소들이 형성되는 과정을 통해 지구와 생명의 역사가 우주 역사의 일부분임을 해석할 수 있다.',
            '세상을 이루는 물질은 원소들로 이루어져 있으며, 원소들의 성질이 주기성을 나타내는 현상을 통해 자연의 규칙성을 찾아낼 수 있다.',
            '지구와 생명체를 구성하는 주요 원소들이 결합을 형성하는 이유와, 원소들의 성질에 따라 형성되는 결합의 종류를 추론할 수 있다.',
            '인류의 생존에 필수적인 산소, 물, 소금 등이 만들어지는 결합의 차이를 알고, 각 화합물의 성질을 비교할 수 있다.',
            '지각과 생명체를 구성하는 다양한 광물과 탄소 화합물은 특정한 규칙에 따라 결합되어 만들어진다는 것을 논증할 수 있다.',
            '생명체를 구성하는 물질들은 기본적인 단위체의 다양한 조합을 통해 형성됨을 단백질과 핵산의 예를 통해 설명할 수 있다.',
            '물질의 다양한 물리적 성질을 변화시켜 신소재를 개발한 사례를 찾아 그 장단점을 평가할 수 있다.',
            '자유 낙하와 수평으로 던진 물체의 운동을 이용하여 중력의 작용에 의한 역학적 시스템을 설명할 수 있다.',
            '일상생활에서 충돌과 관련된 안전사고를 탐색하고 안전장치의 효과성을 충격량과 운동량을 이용하여 평가할 수 있다.',
            '지구 시스템은 태양계라는 시스템의 구성요소이면서 그 자체로 수많은 생명체를 포함하는 시스템임을 추론하고, 지구 시스템을 구성하는 하위 요소를 분석할 수 있다.',
            '다양한 자연 현상이 지구 시스템 내부의 물질의 순환과 에너지의 흐름의 결과임을 기권과 수권의 상호 작용을 사례로 논증할 수 있다.',
            '지권의 변화를 판구조론적 관점에서 해석하고, 에너지 흐름의 결과로 발생하는 지권의 변화가 지구 시스템에 미치는 영향을 추론할 수 있다.',
            '지구 시스템의 생물권에는 인간과 다양한 생물들이 포함되는데, 모든 생물은 생명 시스템의 기본 단위인 세포로 구성되어 있으며, 이러한 세포에서는 생명 현상 유지를 위해 세포막을 경계로 한 물질 출입이 일어남을 설명할 수 있다.',
            '생명 시스템 유지에 필요한 화학 반응에서 생체 촉매의 역할을 이해하고, 일상생활에서 생체 촉매를 이용하는 사례를 조사하여 발표할 수 있다.',
            '생명 시스템 유지에 필요한 세포 내 정보의 흐름을 유전자와 단백질의 관계로 설명할 수 있다.',
            '지구와 생명의 역사에 큰 변화를 가져온 광합성, 화석 연료 사용, 철기 시대를 가져온 철의 제련 등의 공통점을 찾을 수 있다.',
            '생명 현상 및 일상생활에서 일어나고 있는 다양한 변화의 이유를 산화와 환원에서 나타나는 규칙성과 특성 측면에서 파악하여 분석할 수 있다.',
            '생활 주변의 물질들을 산과 염기로 구분할 수 있다.',
            '산과 염기를 섞었을 때 일어나는 변화를 해석하고, 일상생활에서 중화 반응을 이용하는 사례를 조사하여 토의할 수 있다.',
            '지질 시대를 통해 지구 환경이 끊임없이 변화해 왔으며 이러한 환경 변화에 적응하며 오늘날의 생물다양성이 형성되었음을 추론할 수 있다.',
            '변이와 자연선택에 의한 진화의 원리를 이해하고, 항생제나 살충제에 대한 내성 세균의 출현을 추론할 수 있다.',
            '생물다양성을 유전적 다양성, 종 다양성, 생태계 다양성으로 이해하고, 생물다양성 보전 방안을 토의할 수 있다.',
            '인간을 포함한 생태계의 구성 요소와 더불어 생물과 환경의 상호 관계를 이해하고, 인류의 생존을 위해 생태계를 보전할 필요성이 있음을 추론할 수 있다.',
            '먹이 관계와 생태 피라미드를 중심으로 생태계 평형이 유지되는 과정을 이해하고, 환경 변화가 생태계에 영향을 미치는 다양한 사례를 조사하고 토의할 수 있다.',
            '엘니뇨, 사막화 등과 같은 현상이 지구 환경과 인간 생활에 미치는 영향을 분석하고, 이와 관련된 문제를 해결하기 위한 다양한 노력을 찾아 토론할 수 있다.',
            '에너지가 사용되는 과정에서 열이 발생하며, 특히 화석 연료의 사용 과정에서 버려지는 열에너지로 인해 열에너지 이용의 효율이 낮아진다는 것을 알고, 이 효율을 높이는 것이 사회적으로 어떤 의미가 있는지를 설명할 수 있다.',
            '화석 연료, 핵에너지 등을 가정이나 산업에서 사용하는 전기 에너지로 전환하는 과정을 분석할 수 있다.',
            '발전소에서 가정 및 사업장까지의 원거리 전력 수송 과정에 대해 이해하고, 전력의 효율적이고 안전한 수송 방안을 토의할 수 있다.',
            '태양에서 수소 핵융합 반응을 통해 질량 일부가 에너지로 바뀌고, 그 중 일부가 지구에서 에너지 순환을 일으키고 다양한 에너지로 전환되는 과정을 추론할 수 있다.',
            '핵발전, 태양광 발전, 풍력 발전의 장단점과 개선방안을 기후변화로 인한 지구 환경 문제 해결의 관점에서 평가할 수 있다.',
            '인류 문명의 지속가능한 발전을 위한 신재생 에너지 기술 개발의 필요성과 파력 발전, 조력 발전, 연료 전지 등을 정성적으로 이해하고, 에너지 문제를 해결하기 위한 현대 과학의 노력과 산물을 예시할 수 있다.',

            <example output>
            ["지구와 생명체를 비롯한 우주의 구성 원소들이 우주 초기부터의 진화 과정을 거쳐서 형성됨을 물질에서 방출되는 빛을 활용하여 추론할 수 있다::반도체 제조에 사용되는 원소들이 지구 초기부터의 진화 과정을 거쳐 형성되는 과정을 학습하고, 반도체 소자의 기본 구성인 원자 및 결합에 대한 이해를 통해 지구 내의 다양한 물질을 분석할 수 있습니다",
            "지구와 생명체를 구성하는 주요 원소들이 결합을 형성하는 이유와, 원소들의 성질에 따라 형성되는 결합의 종류를 추론할 수 있다::반도체 소자의 소재로 사용되는 물질들의 물리적 성질 및 화학적 특성에 대한 이해를 바탕으로, 교과목에서 다루는 물질의 성질과 결합의 종류를 비교하고 추론할 수 있습니다",
            "화석 연료, 핵에너지 등을 가정이나 산업에서 사용하는 전기 에너지로 전환하는 과정을 분석할 수 있다::전기 에너지를 생성하고 전송하는 과정에 대한 이해를 통해, 전력 생산과 소비의 관련성을 이해하고 화석 연료에서 전기 에너지로의 전환에 대한 분석을 수행할 수 있습니다",
            "인류 문명의 지속가능한 발전을 위한 신재생 에너지 기술 개발의 필요성과 파력 발전, 조력 발전, 연료 전지 등을 정성적으로 이해하고, 에너지 문제를 해결하기 위한 현대 과학의 노력과 산물을 예시할 수 있다::교과목에서 다루는 환경 변화 및 지구 환경 문제에 관련하여, 반도체 공급망 문제와 에너지 사용의 연관성을 이해하고, 신재생 에너지 기술의 필요성과 환경 보전 측면에서의 중요성을 논의할 수 있습니다"
            ]
            """

        criteria_human = """
            please
            <input information>
            major keyword: {keyword}
            criterias: {criteria}

            <output>
            """
        topic_system = """
            <goal>
            * As an AI specialized in assisting high school students with curriculum exploration activities, you are helping a high school student who has a keen interest in 'major keyword' and is currently studying subject
            * meeting the 'subject achievement criteria', recommend four research topics related to 'major keyword' that this high school student can explore
            * Please provide brief explanations for the recommendations from the perspective of career development.

            <output format>
            * generate research topic
            * '::' should be added at the end criteria. after that, explaination has to be come up like '주제::주제로 만들어진 이유에 대한 설명'
            * each result should be paired with generated topic::explain in array.
            * each result should be paired with topic::explain in array.
            * output type must be an array.
            * output should be korean

            <example input>
            keyword: 기후 변화와 지속 가능성
            criteria: 시간적, 공간적, 사회적, 윤리적 관점의 특징을 이해하고, 이를 바탕으로 인간, 사회, 환경의 탐구에 통합적 관점이 요청되는 이유를 파악한다::기후 변화와 지속 가능성을 이해하기 위해 기후 변화의 시간적, 공간적, 사회적, 윤리적 측면을 이해하고, 인간, 사회, 환경의 관계에 대한 통합적인 관점을 개발할 수 있습니다.


            <example output>
            [
            "기후변화와 해양 생태계의 영향::기후 변화가 해양 생태계에 미치는 영향을 시간적, 공간적, 사회적, 윤리적 측면에서 이해하고, 이를 통해 인간, 사회, 환경의 관계에 대한 통합적인 관점을 개발할 수 있습니다.",
            "기후변화와 식량 안보::기후 변화가 식량 안보에 미치는 영향을 시간적, 공간적, 사회적, 윤리적 측면에서 이해하고, 이를 통해 인간, 사회, 환경의 관계에 대한 통합적인 관점을 개발할 수 있습니다.",
            "기후변화와 도시 계획::기후 변화가 도시 계획에 미치는 영향을 시간적, 공간적, 사회적, 윤리적 측면에서 이해하고, 이를 통해 인간, 사회, 환경의 관계에 대한 통합적인 관점을 개발할 수 있습니다.",
            "기후변화와 재생에너지 발전::기후 변화에 대응하기 위한 재생에너지 발전의 중요성을 시간적, 공간적, 사회적, 윤리적 측면에서 이해하고, 이를 통해 인간, 사회, 환경의 관계에 대한 통합적인 관점을 개발할 수 있습니다."
            ]       
            """
            
        topic_human = """
            please
            <input information>
            major keyword: {keyword}
            selected criteria: {criteria}

            <output>
            """
        
        guideLine_system = """
            <goal>
            * As an AI specialized in assisting high school students with curriculum exploration activities, you are helping a high school student who has a keen interest in 'major keyword' and is currently studying subject
            * A high school student interested in 'major' is preparing to write a research report.
            * provide guidelines for writing a research report with topic, major and keyword

            <output format>
            * Should be devided into 3 parts as 'introduction', 'body', 'conclusion'
            * put the subtopic in '<>' and put the context after '\\n* ' and put the next subtopic in '<>' after '\\n\\n'
            * example: <subtopic1>\\n* context1\\n* context2\\n\\n<subtopic2>\\n* context3\\n* context4
            * output should be korean

            <essay introduction guide>
            * Provide assistance to explain the topic
            * Provide guideline to write the goal of research

            <essay body guide>
            * Provide detailed contents of introduction's guidance
            * Provide guidance for conducting research or analysis activities related to fundamental theoretical knowledge concerning the topic.
            * Create guidelines for investigating the market, industry practices, or current industry status related to the topic's impact assessment.
            * Choose one case from the 'reference_cases' and Develop guidelines for researching based on 'reference_cases' related to the topic with '[case]' indicator at the end of body part

            <essay conclusion guide>
            * Offer guidance on contemplating the outlook of the industry or specific career paths to help users consider future prospects.
            * Provide guidelines on how to effectively structure and present overall research findings.
            * Supply guidance on suggesting future research directions to users.
            {format_instructions}

            <example input>
            major: 반도체공학
            keyword: 반도체 공급망 문제
            topic: 지속 가능한 반도체 소자 제조를 위한 물질 선택
            reference_cases: 
            최근 미중 경쟁하의 새로운 지정학적 질서 변화는 기존의 기술, 경제, 안보의 파편적 접근이 아닌 통합적 시각에서 조망할 필요성을 제기하고 있습니다. 이러한 맥락에서 반도체 공급망 문제는 국가안보의 품목으로서 반도체의 중요성과 세계화의 상징으로서 반도체 공급망 구조, 그리고 반도체 산업의 지정학적 불확실성과 한국의 딜레마를 중심으로 재편되고 있습니다.
            반도체 공급망 재편의 기술지정학적 쟁점
            반도체 공급망 재편 이슈의 부상: 국가안보의 품목으로서 반도체의 위상과 세계화의 상징으로서 반도체 공급망 구조의 중요성이 증가하고 있습니다.
            글로벌 반도체 시장 현황과 지배 구도: 반도체 산업 분야별 글로벌 지배 구도와 각국의 경쟁력 분석을 통한 전략적 대응이 필요합니다.
            미국의 팹4 제안 배경과 의미: 한국-미국-일본-대만 4자 간의 팹4 참여 이슈는 전략적 고민을 던져주고 있으며, 이는 기술-경제-안보가 밀접히 결합된 기술지정학적 맥락에서 이해해야 합니다.
            한국의 반도체 공급망 안보 강화를 위한 시사점
            중장기 관점에서 본 기회 및 도전 요소: 반도체 공급망 재편 과정이 시사하는 한국적 맥락의 기회와 도전 요인을 분석하고 전략적 고려사항을 도출해야 합니다.
            한국의 전략적 선택지: 우위 분야의 초격차 전략을 통한 ‘한국형 반도체 방패’ 확보, 외부 위협으로부터 충격 완화를 위한 보호장치 활용, 다면적 선택지 탐색을 통한 공급망 재편 과정에서의 전략적 대응이 필요합니다.
            반도체 공급망 문제는 단순히 특정 기술의 경쟁우위나 분업 관계 재편의 문제만이 아니라, 기술-경제-안보가 융합된 복합적인 문제로 접근해야 합니다. 이는 미중 전략 경쟁 구도가 미치고 있는 지정학적 패러다임 전환 과정 속에서 거시적 국가전략의 필요성을 제기합니다. 따라서 반도체 공급망 재편 과정에서의 주요국 대응 전략 분석을 통해 한국이 나아가야 할 방향을 모색해야 합니다.

            <example output>
            "{{"ig": "<주제 소개>\\n반도체 소자의 생산과정에서 사용되는 물질의 선택이 환경에 미치는 영향을 다룹니다.\\n\\n<연구 목적>\\n더 지속 가능하고 환경 친화적인 반도체 소자 제조를 위한 물질 선택에 관한 연구의 목적을 설명합니다.",
            "bg":"<환경 영향 분석>\\n* 과거의 반도체 소자 생산에서 사용된 물질들이 환경에 미치는 부정적인 영향을 조사합니다.\\n* 최근의 환경 지속 가능성에 대한 요구사항을 바탕으로, 새로운 물질의 선택이 어떻게 기존 방법을 개선할 수 있는지 분석합니다.\\n\\n<글로벌 반도체 시장 현황>\\n* 글로벌 반도체 시장에서 사용되는 주요 소재 및 해당 물질의 생산과 사용에 따른 환경 영향을 조사합니다.\\n* 각 국가의 환경 규제 및 정책이 반도체 소자 제조에 미치는 영향을 분석합니다.\\n\\n<[case]미국의 팹4 제안과 의미>\\n*미국이 제안한 팹4에 참여함으로써 어떤 물질이 사용되며, 이로 인해 어떤 환경적 효과가 발생할지 조사합니다.\\n*한국의 반도체 산업에 미치는 영향 및 한국의 대응 전략을 분석합니다.",
            "cg":"<중장기 전망과 대응 전략>\\n* 반도체 소자 제조에서의 물질 선택이 지속 가능성과 환경에 미치는 영향에 대한 중장기적인 전망을 제시합니다.\\n* 한국이 지속 가능한 반도체 소자 생산을 위해 어떤 전략을 채택해야 하는지 제언합니다.\\n\\n<전체적인 연구 결과 강조>\\n* 연구에서 얻은 주요 결과와 환경에 대한 고려사항을 간략하게 요약합니다.\\n* 반도체 소자 제조에 관한 물질 선택이 환경 지속 가능성에 어떻게 기여할 수 있는지 강조합니다.\\n\\n<향후 연구의 방향 제시>\\n* 환경 친화적인 물질의 개발 및 적용에 관한 추가적인 연구가 필요한 이유를 제시합니다.\\n* 더 나아가, 반도체 소자 생산에서의 물질 선택이 다양한 기술적, 경제적, 환경적 측면에서 어떻게 협업하여 진행되어야 하는지 논의합니다."}}"
            """
        guideLine_human ="""
                        <input information>
                        major: {major}
                        major keyword: {keyword}
                        topic: {topic}
                        reference_cases: {reference}

                        <output>
                        """
