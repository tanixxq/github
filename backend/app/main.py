from fastapi import FastAPI, HTTPException

from app.github_api import (
    get_repository,
    get_contributors
)


app = FastAPI(
    title="Contributor Retention Analytics",
    description="GitHub contributor onboarding and retention analyzer",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Contributor Retention Analytics API is running"
    }


@app.get("/api/repository/{owner}/{repo}")
def repository(owner: str, repo: str):
    try:
        data = get_repository(owner, repo)

        return {
            "name": data["name"],
            "full_name": data["full_name"],
            "description": data["description"],
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "open_issues": data["open_issues_count"],
            "default_branch": data["default_branch"]
        }

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@app.get("/api/repository/{owner}/{repo}/contributors")
def contributors(owner: str, repo: str):
    try:
        data = get_contributors(owner, repo)

        return {
            "count": len(data),
            "contributors": data
        }

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )