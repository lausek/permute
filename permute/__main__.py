from argparse import ArgumentParser
from permute.permute import Permute


def build_parser() -> ArgumentParser:
    parser = ArgumentParser()

    parser.add_argument(
        "--min",
        dest="min_len",
        type=int,
        default=0,
        help="only output words with at least MIN_LEN chars",
    )
    parser.add_argument(
        "--max",
        dest="max_len",
        type=int,
        default=None,
        help="only output words with at most MAX_LEN chars",
    )

    parser.add_argument(
        "-c", "--with-capital", dest="with_capital", action="store_true", default=False
    )
    parser.add_argument(
        "-l",
        "--with-lowercase",
        dest="with_lowercase",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-u",
        "--with-uppercase",
        dest="with_uppercase",
        action="store_true",
        default=False,
    )

    return parser


def main():
    import sys

    parser = build_parser()
    args = parser.parse_args()
    words = list(word.strip() for word in sys.stdin.readlines() if word.strip())
    permute = Permute(words=words, **vars(args))

    for word in permute.create_generator():
        print(word)


if __name__ == "__main__":
    main()
