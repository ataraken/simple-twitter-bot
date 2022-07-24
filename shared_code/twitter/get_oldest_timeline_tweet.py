"""タイムラインのもっとも古いツィートを見つける関数

タイムラインのもっとも古いツィートを検索し、そのツィートの ID とテキストを返す
"""

from typing import Tuple

from shared_code.twitter.api.v1 import proxy
from shared_code.twitter.api.v1 import timeline

def get() -> Tuple[str, str]:
    """最も古いツィートを取得する

    Args:
    
    Returns:
        もっとも古いツィートの ID と文章

    Raises:
    """
    cnt = 200
    is_exit = False
    max_id = None

    while not is_exit:
        param = timeline.Param()
        param.set_count(cnt)
        param.set_max_id(max_id)

        res = proxy.request(param, param.get_session())
        is_exit = len(res) != cnt

        record = res[-1]
        max_id = record['id']
  
    return record['id'], record['full_text']
