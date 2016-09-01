improt requests
from urllib import request

GSPC_url = "http://chart.finance.yahoo.com/table.csv?s=^GSPC&a=6&b=28&c=2016&d=7&e=28&f=2016&g=d&ignore=.csv"


def get_data(company_url):
    response = request.urlopen(company_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")

    dump_data = r"GSPC_stockdata.csv"
    fx = open(dump_data, "w")  # built an open object
    for line in lines:
        fx.write(line + "\n")
    fx.close()

    read_dump = open(dump_data, "r")
    data_dump = read_dump.read()
    lines2 = data_dump.split("\\n")
    for line in lines2:
        print(data_dump)
    read_dump.close()


get_data(GSPC_url)