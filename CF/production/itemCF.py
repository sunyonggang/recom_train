import sys
import math
import operator

sys.path.append("..")
import util.reader as reader


# 用户物品列表；计算物品出现的次数 & 物品同现次数
# 相似度计算的分子：惩罚出现次数多的那个 or 纳入同现的时间差

def get_top_item(user_click, user_click_time):
    item_occur = {}
    item_co_appear = {}
    for user, items in user_click:
        for i in range(len(items)):
            item_i = items[i]
            item_occur.setdefault(item_i, 0)
            item_occur[item_i] += 1
            item_co_appear.setdefault(item_i, {})
            for j in range(i + 1, len(items)):
                item_j = items[j]
                item_co_appear.setdefault(item_j, {})
                item_co_appear[item_i].setdefault(item_j, 0)
                item_co_appear[item_i][item_j] += 1
                item_co_appear[item_j].setdefault(item_i, 0)
                item_co_appear[item_j][item_i] += 1

def get_item(item_occur, item_co_appear):
    item_calc = {}
    item_sorted = {}
    for item_i, item_dict in item_co_appear:
        item_calc.setdefault(item_i, {})
        for item_j, income in item_dict:
            item_calc[item_i][item_j] = income / (item_occur[item_i] * item_occur[item_j])

    for item in item_calc:
        item_sorted[item] = sorted(item_calc[item].iteritems(), key = operator.itemgetter(1), reverse=True)
    return  item_sorted


def cal_recom_result(sim_info, user_click):
    recent_click_num = 3
    topk = 5
    recom_info = {}

    for user, item_list in user_click:
        recom_info.setdefault(user, {})
        for itemid in item_list[:recent_click_num]:
            if itemid not in sim_info:
                continue
            for item_sim in sim_info[itemid][:topk]:
                item_sim_id = item_sim[0]
                item_sim_score = item_sim[1]
                if item_sim_id not in item_list:
                    recom_info[user][item_sim_id] = item_sim_score

    return recom_info






if __name__ == '__main__':
    reader.sayHello()