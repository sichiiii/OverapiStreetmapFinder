import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store',
                    dest='count', help='количество')
parser.add_argument('--country', action='store',
                    dest='country', help='страна')

args = parser.parse_args()
print(args.count, args.country)

known_countries = []
if args.country not in known_countries:
    print('Некорректная страна')
    exit()