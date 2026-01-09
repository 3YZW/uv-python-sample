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

以下のコマンドを実行

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

## 3. Pythonのバージョンをプロジェクト単位で指定

pyproject.tomlのバージョンを 3.11 に変更

```toml
[project]
requires-python = ">=3.11"
```

`uv python pin` を使用し、プロジェクトごとに使用する Python バージョンを固定。

```bash
uv python pin 3.11
```

実行結果

```text
Updated `.python-version` from `3.9.6` -> `3.11`
```

## 4.uv のみを使用して Hello World を実行

実行コマンド

```bash
uv run python main.py
```

実行結果

```text
Using CPython 3.11.14
Creating virtual environment at: .venv
Hello World
```

## 5：依存ライブラリをプロジェクト毎に管理

依存管理の例として、HTTP 通信を行うための外部ライブラリである requests を追加

```bash
uv add requests
```

実行結果

```text
Resolved 6 packages in 248ms
Installed 5 packages in 33ms
 + certifi==2026.1.4
 + charset-normalizer==3.4.4
 + idna==3.11
 + requests==2.32.5
 + urllib3==2.6.3
```
