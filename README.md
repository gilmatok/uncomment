# uncomment

A pre-commit hook to prevent commits with comment-only code

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
