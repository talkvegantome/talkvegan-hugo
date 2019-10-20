
import re
import os

ERROR = False
matches = [
    {
        'name': 'No non-breaking spaces',
        'pattern': r' '
    },
    {
        'name': 'No relative urls',
        'pattern': r'\.\.\/'
    },
    {
        'name': 'No numbered lists in blockquotes',
        'pattern': r'\s*>\s*\d\.\s'
    }
]


def run_matchers(file_path):
    global ERROR
    file_to_match = open(file_path).read()
    for i in matches:
        any_match = re.search(i['pattern'], file_to_match)
        if any_match:
            matching_text = any_match[0].replace('\n', '')
            print(f"\t{file_path} should have {i['name']}\n\t{matching_text}")
            ERROR = True


root = './content'
for dir_name, sub_dir_list, file_list in os.walk(root):
    for fname in file_list:
        if re.search(r'\.md$', fname):
            print(f"Evaluating: {os.path.join(dir_name, fname)}")
            run_matchers(os.path.join(dir_name, fname))

if ERROR:
    print('Errors found, exit code 1')
    exit(1)
