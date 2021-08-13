import time
import random
import urllib3
import argparse
from urllib3 import Timeout, Retry
from multiprocessing import Pool, freeze_support

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--threads", help="number of threads (15)", type=int, default=15)
parser.add_argument("-o", "--timeout", help="timeout (5)", type=int, default=5)
parser.add_argument("-d", "--delay", help="delay between requests (1)", type=int, default=1)
parser.add_argument("-u", "--url", help="url (http://site.com)", type=str, required=True)
parser.add_argument("-v", "--verbose", help="verbose", action="store_true")
args = parser.parse_args()

ua = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)',
      'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 6.0)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)',
      'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)']


def header_gen():
    header = {
        'User-agent': random.choice(ua),
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive'}
    http = urllib3.PoolManager(headers=header, cert_reqs=False, num_pools=30, retries=Retry(3),
                               timeout=Timeout(args.timeout))
    return http


def enum(id_):
    time.sleep(args.delay)
    try:
        req = header_gen().request("GET", args.url + f"/user/{id_}")
        if args.verbose:
            print(f"Trying id: {id_}")
        if "/users/" in req.geturl():
            print(f"[{id_}] " + req.geturl())
    except Exception as ex:
        if "Max retries exceeded with url" in str(ex) or "NoneType" in str(ex):
            pass
        else:
            print(str(ex))


if __name__ == "__main__":
    print("Starting...")
    ids = [number for number in range(1, 1000)]
    freeze_support()
    pool = Pool(args.threads)
    pool.map(enum, ids)
    pool.close()
    pool.join()
