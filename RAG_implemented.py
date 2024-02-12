# 단계 3.5: 토큰 pricing
# 따로 callback으로 확인이 안되므로, 토큰 수를 계산한 뒤, 임베딩 pricing에 따라 토큰 당 금액을 파악한다.

import tiktoken
def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

def embedding_price(docs, model):
    price = { 'text-embedding-3-small': 0.00002,
              'text-embedding-3-large': 0.00013,
              'text-embedding-ada-002': 0.00010,
    }
    emb_price = price[model] * 0.001 # 1,000토큰당 금액이므로
    cost = 0
    token = 0
    for doc in docs:
      cost += num_tokens_from_string(doc.page_content)* emb_price
      token += num_tokens_from_string(doc.page_content)
    return cost, token
