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
    # TODO: it'd be cool to allow options
    # {
    #     'type': 'list',
    #     'name': 'title_style',
    #     'message': 'Choose the style for the title text:',
    #     'choices': [
    #         {'name': '1. Title', 'value': 'title_1'},
    #         {'name': '1 - Title', 'value': 'title_2'}
    #     ],
    # }
    {
        'type': 'confirm',
        'name': 'is_dry_run',
        'message': 'Is this a dry run?',
        'default': True
    }
]


def main():
    print("Welcome to Shelf Organizer!\n")
    answers = prompt(questions)

    dir = answers['directory']
    # title_style = answers['title_style']
    is_dry_run = answers['is_dry_run']

    summary = f"""
    Please review your answers:
    1. File path: {dir}
    2. Dry run: {is_dry_run}
    """
    confirm_question = [
        {
            "type": "confirm",
            "message": summary + "\n\nIs this correct?",
            "name": "confirm",
            "default": True,
        }
    ]
    confirmation = prompt(confirm_question)
    if (confirmation["confirm"]):
        organize(dir, is_dry_run)


if __name__ == "__main__":
    main()


# ../../../Downloads/shelf-test