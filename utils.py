from pathlib import Path
from tempfile import TemporaryDirectory

import pygit2


def get_source_code(git_repo_url: str) -> TemporaryDirectory:
    temp_directory = TemporaryDirectory()
    pygit2.clone_repository(url=git_repo_url, path=temp_directory.name)
    return temp_directory


def get_source_file_paths_to_analyze(sources_path: Path, directories: list[str], extensions: list[str]) -> list[Path]:
    file_paths_to_analyze = []
    for subdirectory in directories:
        for extension in extensions:
            file_paths_to_analyze.extend(
                list(sources_path.glob(f"{subdirectory}/**/*{extension}"))
            )

    return file_paths_to_analyze
