import subprocess


DEV_DEPS = sorted(
    (
        'ipdb',
        'ipython',
        'mypy',
        'pre-commit',
        'pytest',
        'pytest-cov',
        'ruff',
        'toml-sort',
    )
)


def green(msg):
    GREEN = '\033[92m'
    END = '\033[0m'
    return f'{GREEN}{msg}{END}'


def print_green(msg):
    print(green(msg))


def init_repo():
    print_green("\nInit git repo")
    subprocess.check_call(['git', 'init', '--initial-branch', 'main'])


def commit_all():
    print_green("\nCommit changes ...")
    subprocess.check_call(['git', 'add', '.'])
    subprocess.check_call(['git', 'commit', '-m', '🎉 Begin project', '--allow-empty'])
    print_green("\nDone!")


def add_dev_deps():
    print_green("\nAdd development dependencies ...")
    subprocess.check_call(['poetry', 'add', '--group', 'dev', '--lock', *DEV_DEPS])


if __name__ == '__main__':
    init_repo()
    add_dev_deps()
    commit_all()
    print_green(
        "All set. You can check everything and run `cd {{cookiecutter.project_slug}} && git push`."
    )
