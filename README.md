# uv-python-sample

Python のモダンなパッケージマネージャー uv の学習用リポジトリ。

## 1. uvのインストール（Mac・M1）

以下のコマンドを実行

```bash
# Homebrew を使ったインストール
brew install uv
# インストール後の確認
uv --version
```

実行結果

```text

uv 0.9.22 (Homebrew 2026-01-06)
```

## 2. uvで新規Pythonプロジェクトを作成

```bash
uv init
```

実行結果

```text
Initialized project `uv-python-sample`
```

作成されたディレクトリ

```css
.
├── pyproject.toml
├── README.md
├── .python-version
└── main.py
```
