import os


def export(database, collection, output):
    # mongoexport -d database -c collection -o output
    cmd = 'mongoexport -d {} -c {} -o {}'.format(database, collection, output)
    os.system(cmd)


if __name__ == "__main__":
    categorys = ['screenplay', 'netscreenplay', 'telescript', 'nettelescript', 'microfilm', 'novel', 'other', 'famous', 'recommend', 'free']
    for category in categorys:
        export('bianju', category, 'F:/Temp/{}.json'.format(category))