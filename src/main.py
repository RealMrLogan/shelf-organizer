import os
from InquirerPy import prompt
from InquirerPy.validator import PathValidator
from organize import organize

questions = [
    {
        'type': 'filepath',
        'name': 'directory',
        "only_directories": True,
        'message': 'Please input which directory to organize (relative path):',
        "validate": PathValidator(is_dir=True, message="Not a valid directory"),
    },
    {
        'type': 'list',
        'name': 'title_style',
        'message': 'Choose the style for the title text:',
        'choices': [
            {'name': '1. Title', 'value': 'title_1'},
            {'name': '1 - Title', 'value': 'title_2'}
        ],
    }
]


def main():
    print("Welcome to Shelf Organizer!\n")
    answers = prompt(questions)

    dir = answers['directory']
    title_style = answers['title_style']

    # TODO: add confirm
    # TODO: add dry run

    print(f"Selected directory: {dir}")
    print(f"Selected title style: {title_style}")

    organize(dir, title_style)



if __name__ == "__main__":
    main()


# ../../../Downloads/shelf-test