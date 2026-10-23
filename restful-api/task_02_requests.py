
#!/usr/bin/python3
"""Fetch and process posts from JSONPlaceholder API."""

import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save selected fields to a CSV file."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()
        posts_list = []

        for post in posts:
            post_dict = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            posts_list.append(post_dict)

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(posts_list)
