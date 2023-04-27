from pathlib import Path
from tempfile import TemporaryDirectory

import pygit2
import plotly.graph_objects as go


def get_source_code(git_repo_url: str) -> TemporaryDirectory:
    print("Downloading git repository")
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


def render_repository_metrics(repository_metrics):
    headers = {
        "values": [
            "File Path",
            "LOC",
            "Empty LOC",
            "Physical LOC",
            "Logical LOC",
            "Comment Lines",
            "Comment Level (F)",
            "Highest CC function",
        ]
    }

    cells = {
        "values": []
    }

    for header in headers["values"]:
        row = []

        for file_path, metrics in repository_metrics.items():
            row.append(metrics[header])

        cells["values"].append(row)

    fig = go.Figure(
        data=[
            go.Table(
                header=headers,
                cells=cells
            )
        ]
    )
    fig.show()
