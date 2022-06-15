import os

if __name__ == "__main__":
    print('--- start ---')
    print(os.getenv('TEST_VAR', 'Nope'))
    print('---')
    print(os.getenv('IS_GITHUB_WORKFLOW', 'Nope'))
    print('--- end ---')
