import csv
a = {'2015-08': 129, '2015-07': 156, '2015-06': 234, '2015-05': 17}
with open("xhw-农产品质量安全.csv","a+",newline="") as f:
  w = csv.DictWriter(f, a.keys())
  w.writeheader()
  w.writerow(a)