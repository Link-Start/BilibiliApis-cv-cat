import requests
from utils.bili_utils import get_common_headers,  trans_cookies, getqvId, get_search_params, getW_rid

class BiliApis():

    """
        搜索一些内容
        :param keyword: 搜索关键字
        :param order: 排序方式  dm 弹幕数排序 click 播放量排序
        :param cookies_str: cookies字符串
        返回搜索结果
    """
    def search_some(self, keyword, order, page, cookies_str):
        success = True
        msg = "成功"
        res_json = None
        try:
            url = 'https://api.bilibili.com/x/web-interface/wbi/search/type'
            cookies = trans_cookies(cookies_str)
            headers = get_common_headers()
            qvId = getqvId()
            m = get_search_params(keyword, order, page, qvId)
            w_rid = getW_rid(m)
            m["w_rid"] = w_rid
            params = m
            response = requests.get(url, params=params, cookies=cookies, headers=headers)
            res_json = response.json()
        except Exception as e:
            success = False
            msg = str(e)
        return success, msg, res_json

    """
        根据数量搜索一些内容
        :param num: 搜索数量
        :param keyword: 搜索关键字
        :param order: 排序方式  dm 弹幕数排序 click 播放量排序
        :param cookies_str: cookies字符串
        返回搜索结果
    """
    def search_some_by_num(self, num, keyword, order, cookies_str):
        success = True
        msg = "成功"
        work_list = []
        try:
            page = 1
            while True:
                success, msg, res_json = self.search_some(keyword, order, page, cookies_str)
                if not success:
                    break
                work_list.extend(res_json["data"]["result"])
                page += 1
                if page > res_json["data"]["pagesize"] or len(work_list) >= num:
                    break
            if len(work_list) > num:
                work_list = work_list[:num]
        except Exception as e:
            success = False
            msg = str(e)
        return success, msg, work_list


if __name__ == '__main__':
    bili_apis = BiliApis()
    cookies_str = r""
    num = 50
    keyword = "娱乐"
    order = "dm"
    success, msg, work_list = bili_apis.search_some_by_num(num, keyword, order, cookies_str)
    print(success, msg, work_list)
    print(len(work_list))


