import argparse
from preprocessing import TextPreProcessing

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='test.txt', help='location of the saved text')

    return parser.parse_args()

def open_text(location):
    if location.endswith('.txt'):
        return open(location, 'r').readlines()

def main(opt):
    text = [' '.join(TextPreProcessing(t).sentence_tokenize()) for t in open_text(opt.input)]
    print(text)

if __name__ == '__main__':
    opt = parse_opt()
    main(opt)