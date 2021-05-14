# import sys
#
# if __name__ == '__main__':
#
#     type_ori_dict_csv = {}
#     cache_count = 0
#     with open(excelname, 'r') as csv_file:
#         for row in csv_file:
#             array_rows = row.strip().split(',')
#             cache_count = cache_count + 1
#             type_ori_dict_csv[array_rows[0]] = array_rows[1]
#     for line in sys.stdin:
#         print('\t'.join("test1") + "\t" +"test2")
#
#         segs = line.split("\t")
#         if (len(segs) < 3):
#            continue
#         if (segs[0] is None or segs[0]):
#             print(user_id)
#             continue
#         if (segs[1] is None or segs[1]):
#             segs[1] = "0"
#         print('\t'.join(segs[0]) + "\t" + str(segs[1]))
#
#         user_id = segs[0]  # 日期
#         orientations = segs[1]  # key
#         result_dict = {}
#         for orientation_id in orientations:
#             orientation_id = str(orientation_id)
#             type_key_result = type_ori_dict_csv.get(orientation_id)
#                 # //check if already exist
#             if (type_key_result in result_dict.keys()):
#                 result_dict_value = result_dict.get(type_key_result)
#                 result_dict_value.append(orientation_id)
#                 result_dict[type_key_result] = result_dict_value
#             else:
#                 tmp_list = [orientation_id]
#                 result_dict[type_key_result] = tmp_list
#             try:
#                 print('\t'.join(user_id) + "\t" + str(result_dict))
#             except ValueError:
#                 continue
#
