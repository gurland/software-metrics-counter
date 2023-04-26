import argparse

# Initialize parser
parser = argparse.ArgumentParser(description="User")
parser.add_argument("repository_link", help="Remote Git repository URL")
parser.add_argument("-d", "--directories", nargs="+", help="Directories to analyze")
parser.add_argument("-e", "--extensions", nargs="+", choices=[".c"], help="File extension to analyze")
parser.parse_args()


def get_source_code(git_repo_url: str):
    raise NotImplementedError
