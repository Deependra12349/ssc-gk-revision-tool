# SSC GK Revision Tool

A small, free and open-source command-line tool to revise **Indian Constitution
articles** for SSC exams (CGL, CHSL, CPO, MTS, Stenographer).

It is built for one simple problem: article numbers are easy to mix up in the
exam hall. This tool turns them into quick quizzes and flashcards so the number
sticks with the fact.

## Features

- **Quiz mode** — 10 random multiple-choice questions, instant checking and score
- **Flashcards mode** — go through every article one by one, at your own pace
- **List mode** — print the full revision list
- **Open data** — all facts live in `data/articles.json`; anyone can add more
  articles, History dates, or Polity facts using the same format

## How to run

You only need Python 3. No installation, no internet.

```bash
python3 quiz.py              # start a 10-question quiz
python3 quiz.py flashcards   # revise with flashcards
python3 quiz.py list         # see all articles
```

## Data format

Each entry in `data/articles.json` looks like this:

```json
{
  "article": 44,
  "fact": "The State shall endeavour to secure a Uniform Civil Code for citizens throughout India (DPSP).",
  "part": "Part IV",
  "topic": "Uniform Civil Code"
}
```

## Contributing

Contributions are welcome — new facts, corrections, or new subjects
(History, Geography, Science) in the same JSON format. Please make sure a
fact is accurate before adding it, and mention the source in your pull request
description.

## About

Created by Deependra (GitHub: Deependra12349), an SSC aspirant, as a learning
project — built step by step to learn GitHub and Python while making something
useful for his own exam revision. AI assistance was used while building it and
every fact in the dataset was checked against standard Polity references.

## License

MIT — see [LICENSE](LICENSE). Free for anyone to use and learn from.
