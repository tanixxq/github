import os

import requests
from dotenv import load_dotenv


load_dotenv()

GITHUB_API = "https://api.github.com"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_headers():
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def get_repository(owner: str, repo: str):
    url = f"{GITHUB_API}/repos/{owner}/{repo}"

    response = requests.get(
        url,
        headers=get_headers()
    )

    if response.status_code == 404:
        raise Exception("Repository not found")

    response.raise_for_status()

    return response.json()


def get_paginated_data(url: str, params=None):
    response = requests.get(
        url,
        headers=get_headers(),
        params=params
    )

    response.raise_for_status()

    return response.json()

def get_contributors(owner: str, repo: str):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/contributors"

    return get_paginated_data(
        url,
        params={
            "per_page": 100
        }
    )