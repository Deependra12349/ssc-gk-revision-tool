#!/usr/bin/env python3
"""SSC GK Revision Tool — Constitution Articles quiz and flashcards.

A small command-line tool for SSC (CGL / CHSL / CPO / MTS) aspirants to
revise Indian Constitution articles. It has three modes:

    python3 quiz.py              # 10-question random quiz
    python3 quiz.py flashcards   # go through every article as a flashcard
    python3 quiz.py list         # print the full article list

Data lives in data/articles.json and can be extended by anyone —
just add an entry with article, fact, part and topic.
"""

import json
import random
import sys
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "articles.json"


def load_articles():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def run_quiz(articles, num_questions=10):
    questions = random.sample(articles, min(num_questions, len(articles)))
    score = 0
    print(f"\n--- Quiz: {len(questions)} questions ---\n")
    for i, item in enumerate(questions, 1):
        options = random.sample(
            [a for a in articles if a["article"] != item["article"]], 3
        ) + [item]
        random.shuffle(options)
        print(f"Q{i}. Which article is about: {item['topic']}?")
        print(f"    Fact: {item['fact']}")
        labels = "abcd"
        for j, opt in enumerate(options):
            print(f"    {labels[j]}) Article {opt['article']}")
        answer = input("Your answer (a/b/c/d): ").strip().lower()
        correct_idx = options.index(item)
        if answer == labels[correct_idx]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong — correct answer is {labels[correct_idx]}) Article {item['article']}\n")
    print(f"Score: {score}/{len(questions)}")
    return score


def run_flashcards(articles):
    print("\n--- Flashcards (press Enter for the answer, q to quit) ---\n")
    for item in articles:
        print(f"Article {item['article']} — {item['topic']} ({item['part']})")
        if input() == "q":
            break
        print(f"  -> {item['fact']}\n")


def print_list(articles):
    for item in articles:
        print(f"Article {item['article']}: {item['topic']} — {item['fact']}")


def main():
    articles = load_articles()
    mode = sys.argv[1] if len(sys.argv) > 1 else "quiz"
    if mode == "quiz":
        run_quiz(articles)
    elif mode == "flashcards":
        run_flashcards(articles)
    elif mode == "list":
        print_list(articles)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
