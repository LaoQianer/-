import os

def Statistics(path):
    i = 0
    for c,s,files in os.walk(path):
        for file in files:
            if file.endswith('_gt.json'):
                i += 1
    return i

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='统计*_gt.json')
    parser.add_argument('--dri',default='./', type=str, help='json文件路径')
    args = parser.parse_args()
    path = args.dri
    num = Statistics(path)
    print(num)
