import os

# path="../../备份 apk下载分析/来自kevin/tv-apps/tv-apps/"
path="../../备份 apk下载分析/来自kevin/latest-apps/final-apps"

def ab(path):
    # 类似于深度优先搜索
    path_list = []
    path_json_list = []
    for root, dirs, files in os.walk(path):
        if (len(dirs)!=0) and (len(dirs)!=2):
            for dir_e in dirs:
                print(dir_e)

        # if (dirs[0].isnumeric()==False):
        # code = code +"""
        #
        # """

        # print("files的内容")
        # print(files)
        # print("dir内容")
        # print(dirs)
        # print("root的内容")
        # print(root)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # for name in files:
        #     if (name.split('.')[-1].endswith('jpg')):
        #         # print("name的内容")
        #         # print(name)
        #         # print("dir内容")
        #         # print(dirs)
        #         # print("root的内容")
        #         # print(root)
        #         # print("合并root+name内容")
        #         print(os.path.join(root, name))
        #         # print("===========================")
        #         path_list.append(os.path.join(root, name))
        #     if (name.split('.')[-1].endswith('json')):
        #         path_json_list.append(os.path.join(root, name))
        #         print(os.path.join(root, name))
    # return path_list, path_json_list


if __name__=='__main__':
    ab(path)
    # ab(path)