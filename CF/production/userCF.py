import sys
import math
import operator

sys.path.append("..")
import util.reader as reader


# 将用户物品列表转化为物品用户列表
# 得到用户出现的次数，共现的次数
# 相似度计算的分子：惩罚出现次数多的那个 or 纳入同现的时间差

def transfer_user_click(user_click):
    """
    get item by user_click
    Args:
        user_click: key userid, value:[itemid1, itemid2]
    Return:
        dict, key itemid value:[userid1, userid2]
    """
    item_click_by_user = {}
    for user, items in user_click.items():
        for item in items:
            item_click_by_user.setdefault(item, [])
            item_click_by_user[item].append(user)
    return item_click_by_user

def base_contribute():
    return 1

def punish_occu(count):
    return 1 / (1 + math.log10(count))

def punish_time(time1, time2):
    time_diff = (time2 - time1) / (3600 * 24)
    return 1 / (1 + math.log10(time_diff))

def get_top_item(item_click_by_user, user_click_time):
    co_appear = {}
    user_record = {}
    for item, users in item_click_by_user.items():
        for i in range(len(users))
            user = users[i]
            user_record.setdefault(user, 0)
            user_record[user] += 1
            if user + "_" + item not in user_click_time:
                time1 = 0
            else
                time1 = user_click_time[user + "_" + item]
            co_appear.setdefault(user, {})
            for j in range(i + 1, len(users)):
                u = users[j]
                user_record.setdefault(u, 0)
                if u + "_" + item not in user_click_time:
                    time2 = 0
                else
                    time2 = user_click_time[u + "_" + item]
                co_appear[user].setdefault(u, 0)
                co_appear[user][u] += 1
                co_appear[u].setdefault(user, 0)
                co_appear[u][user] += 1


    user_simi_info = {}
    user_simi_info_sort = {}
    for user_i, user_j_dict in co_appear:
        user_simi_info.setdefault(user_i, {})
        for user_j, in_come in user_j_dict:
            # user_simi_info.setdefault(user_j, {})
            simi_calc = in_come / math.sqrt(user_record[user_i] * user_record[j])
            user_simi_info[user_i][user_j] = simi_calc
            # user_simi_info[user_j][user_i] = simi_calc

    for user in user_simi_info:
        user_simi_info_sort[user] =sorted(user_simi_info[user].iteritems(), key=operator.itemgetter(1), reversed=True)

    return  user_simi_info_sort

def call_recom_result(user_click, user_simi_info_sort):
    """
    :param user_click: dict; key: user, value:item_list
    :param user_simi_info: dict; key: user1, value: [user2: similarity]
    :return: user_recom: dict; key: user, value: item_list
    """

    user_recom = {}
    topk_user = 3
    item_num = 5
    for user, item_list in user_click:
        item_temp = {}
        for item in item_list:
            item_temp.setdefault(item, 1)
        user_recom.setdefault(user, {})

        for zuhe in user_simi_info_sort[user][:topk_user]:
            user_j, simi_score = zuhe
            if user_j not in user_click:
                continue
            for item_j in user_click[user_j][:item_num]:
                if item_j in item_temp:
                    continue
                user_recom[user].setdefault(item_j, simi_score)
    return user_recom




if __name__ == '__main__':
    reader.sayHello()