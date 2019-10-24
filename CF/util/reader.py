import os


"""
    get user click list
    Args:
        rating_file:input file
    Return:
        dict1, key:userid ,value:[itemid1, itemid2]
        dict2, key:userid_itemid, value: [timestamp]
"""

def get_user_click(rating_file):
    # 判断路径文件是否存在，如果不存在，返回两个空的dict
    # 循环整个文件，将每行数据放入到两个dict中
    if not os.path.exists(rating_file):
        return {}, {}

    f_rating_file = open(rating_file, "r")
    user_click = {}
    user_click_time = {}

    for line in f_rating_file:
        # print(line)
        elements = line.split(',')
        if len(elements) != 4:
            continue
        user_id, item_id, score, timestamp = elements
        if "." not in score or float(score) < 3:
            continue
        # print(user_click)
        user_click.setdefault(user_id, [])
        user_click[user_id].append(item_id)

        user_click_time.setdefault(user_id + "_" + item_id, 0)
        user_click_time[user_id + "_" + item_id] = timestamp.strip()

    return  user_click, user_click_time

"""
    get item info[title, genres]
    Args:
        item_file:input iteminfo file
    Return:
        a dict, key itemid, value:[title, genres]
"""
def get_item_info(item_file):

    if not os.path.exists(item_file):
        return {}

    f_item_file = open(item_file, "r")
    item_info = {}
    num = 0
    for line in f_item_file:
        num += 1
        if num == 1:
            continue
        elements = line.split(",")
        if len(elements) < 3:
            continue
        elif len(elements) == 3:
            item, title, genres = elements
        else:
            item = elements[0]
            genres = elements[-1]
            title = elements[1:-1]
        item_info.setdefault(item, [])
        item_info[item] = [title, genres.strip()]
    return  item_info


def sayHello():
    print("hello syg")




if __name__ == '__main__':
    # rating_file = "/Users/sunyonggang/PycharmProjects/recommendation/CF/data/ratings.txt"
    # print("user_click")
    # print(get_user_click(rating_file)[0])
    # print("user_click_time")
    # print(get_user_click(rating_file)[1])

    # item_file
    item_file = "/Users/sunyonggang/PycharmProjects/recommendation/CF/data/movies.txt"
    print(get_item_info(item_file))










