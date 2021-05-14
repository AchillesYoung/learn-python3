import sys
import datetime

from numpy.core import long
# viewfs://hadoop-lt-cluster/home/
# hdfs://lt-router.sy/home/ad/yangshu:
if __name__ == '__main__':
    for line in sys.stdin:
        print(line)
        line = line.strip("\r\n")
        segs = line.split("\t")
        print(segs)
        if len(segs) < 3:
            continue
        date_str = segs[2]    # 日期
        key = segs[0]         # key
        values = segs[1].split(",") # value
        date = datetime.datetime.strptime(date_str, '%Y%m%d') + datetime.timedelta(days=1)
        print(date)
        for value in values:
            if value == "NaN":
                value = 0
            value = long(float(value))
            print('\t'.join(key.split("#")) + "\t" + str(value) + "\t" + str(date.strftime('%Y%m%d%H00')))
        date = date + datetime.timedelta(hours=1)
