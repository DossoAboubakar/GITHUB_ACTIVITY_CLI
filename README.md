
# GitHub Repository Data Fetcher

This Python script retrieves information from a GitHub repository via the GitHub API. By providing a username, repository name, and data type (`commits`, `events`, or `issues`), the script automatically initiates GitHub CLI authentication and displays the results in JSON format in the console.

## Prerequisites

Before using this script, make sure you have the following installed:

- **Python** (version 3.6 or higher)
- **GitHub CLI (`gh`)**: You can install it by following the instructions [here](https://cli.github.com/).

## Installation

Clone this repository or download the script file.

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

## Usage

### Syntax

```bash
python script.py <username> <repo> <tag>
```

- `<username>`: GitHub username
- `<repo>`: GitHub repository name
- `<tag>`: Type of data to retrieve. Available options: `commits`, `events`, or `issues`

### Example

To retrieve the `commits` from a repository named `example-repo` owned by user `octocat`:

```bash
python script.py octocat example-repo commits
```

### Explanation

1. **GitHub Authentication**: The `authenticate_github()` function executes `gh auth login` to authenticate via GitHub CLI.
2. **Data Retrieval**: The `fetch_github_data()` function uses the GitHub API to fetch the specified repository information.
3. **Data Display**: The data is displayed in the console in JSON format.

### `tag` Options

- **commits**: Retrieves the list of recent commits in the repository.
- **events**: Retrieves recent events associated with the repository.
- **issues**: Retrieves the issues in the repository.

## Sample Output

The JSON output for a `commits` request might look like this:

```json
[
  {
    "sha": "abc123...",
    "commit": {
      "author": {
        "name": "Author",
        "email": "email@example.com",
        "date": "2023-10-01T12:34:56Z"
      },
      "message": "Added a new feature"
    }
  }
]
```

## Possible Errors

If the script fails to read the JSON response, an error message will indicate that the JSON response is invalid.

## Author

Created by [DOSSO ABOUBAKAR](https://github.com/yourgithubprofile).