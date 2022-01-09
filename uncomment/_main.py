import argparse
from typing import Optional
from typing import Sequence

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    ret = 0
    for filename in args.filenames:
        print(filename)
    return ret

if __name__ == '__main__':
    raise SystemExit(main())