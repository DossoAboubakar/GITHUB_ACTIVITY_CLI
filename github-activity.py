import os
import argparse
import json

def authenticate_github():
    os.system("gh auth login")

def fetch_github_data(username, repo, tag):
    command = f"gh api /repos/{username}/{repo}/{tag} --method GET"
    result = os.popen(command).read()
    try:
        data = json.loads(result)
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print("Erreur : Impossible de lire la réponse JSON.")
        print(result)

def main():
    parser = argparse.ArgumentParser(description="Fetch data from GitHub repository")
    parser.add_argument("username", type=str, help="GitHub username")
    parser.add_argument("repo", type=str, help="Repository name")
    parser.add_argument("tag", type=str, choices=["commits", "events", "issues"], help="Tag (commits, events, or issues)")

    args = parser.parse_args()

    authenticate_github()
    fetch_github_data(args.username, args.repo, args.tag)

if __name__ == "__main__":
    main()
