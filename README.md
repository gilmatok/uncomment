# uncomment

A pre-commit hook to prevent commits with comment-only code

Commented out a piece of code on your local machine, only to find out you forgot to remove it and it's now on your production environment? No more! This useful pre-commit hook will scan your changes before pushign them to check if you are trying to commit comment-only code.

## Installation

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/Fraysa/uncomment
    rev: v0.0.3
    hooks:
    -   id: uncomment
```

## Supported languages
| Language | Extensions |
|----------|------------|
| C#       | .cs        |
| Python   | .py        |
