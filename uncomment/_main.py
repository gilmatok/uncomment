import pathlib
import subprocess
from typing import Any
from typing import Optional
from typing import Sequence
from typing import Set

COMMENTS = {
    '.cs': ['//', '/*', '*/'],
    '.py': ['#', '\'\'\'']
}

class CalledProcessError(RuntimeError):
    pass


def get_staged_files() -> Set[str]:
    cmd = ('git', 'diff', '--staged', '--name-only')
    return set(cmd_output(*cmd).splitlines())


def get_staged_file_changes(filename) -> Set[str]:
    cmd = ('git', 'diff', '--staged', filename)
    return set(cmd_output(*cmd).splitlines())


def cmd_output(*cmd: str, retcode: Optional[int] = 0, **kwargs: Any) -> str:
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def find_commented_code() -> int:
    ret = 0
    relevant_files = get_staged_files()

    for filename in set(relevant_files):
        extension = pathlib.Path(filename).suffix
        
        if not extension in COMMENTS:
            continue
        
        comments = COMMENTS[extension]
        changes = get_staged_file_changes(filename)

        found_comments = False
        for change in set(changes):
            if not change.startswith('+') or change.startswith('+++'):
                continue

            change = change[1:]
            
            if change.startswith(tuple(comments)) or change.endswith(tuple(comments)):
                found_comments = True
            elif found_comments:
                found_comments = False
                break

        if found_comments:
            print(f'Found comments only in file: {filename}')
            ret = 1

    return ret

def main(argv: Optional[Sequence[str]] = None) -> int:
    return find_commented_code()

if __name__ == '__main__':
    raise SystemExit(main())