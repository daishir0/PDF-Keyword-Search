# PDF Keyword Search

PDF Keyword Search is a tool developed in Python that extracts text from PDF files, cleans the extracted text, and searches for specified keywords or phrases. It's particularly useful for processing large volumes of documents to quickly find relevant information.

## Installation

To use this tool, first clone the repository:

```
git clone https://github.com/daishir0/PDFKeywordSearch
```

Then, navigate to the cloned directory and install the required Python packages:

```
cd PDFKeywordSearch
pip install -r requirements.txt
```

## Usage

To search PDF documents for keywords or phrases, use the following command:

```
python pdf_search.py <path_to_pdf_directory> "<search_term1>" "<search_term2>" ...
```

Replace `<path_to_pdf_directory>` with the path to the directory containing your PDF files, and `<search_term1>`, `<search_term2>`, etc., with the keywords or phrases you're searching for.

## Notes

- The tool currently supports a maximum of 5 keywords or phrases per search.
- Text is cleaned by removing hyphens and extra spaces to improve search accuracy.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# PDF Keyword Search

PDF Keyword Searchは、PDFファイルからテキストを抽出し、抽出されたテキストをクリーニングし、指定されたキーワードやフレーズを検索するために開発されたPythonツールです。大量のドキュメントを処理し、関連情報を迅速に見つけるのに特に役立ちます。

## インストール方法

このツールを使用するには、まずリポジトリをクローンします：

```
git clone https://github.com/daishir0/PDFKeywordSearch
```

次に、クローンしたディレクトリに移動し、必要なPythonパッケージをインストールします：

```
cd PDFKeywordSearch
pip install -r requirements.txt
```


## 使い方

PDFドキュメントでキーワードやフレーズを検索するには、次のコマンドを使用します：

```
python pdf_search.py <path_to_pdf_directory> "<search_term1>" "<search_term2>" ...
```



`<path_to_pdf_directory>`をPDFファイルが含まれるディレクトリへのパスに置き換え、`<search_term1>`、`<search_term2>`などを検索したいキーワードやフレーズに置き換えてください。

## 注意点

- このツールは、検索ごとに最大5つのキーワードまたはフレーズをサポートしています。
- 検索精度を向上させるために、ハイフンや余分なスペースを除去してテキストをクリーニングします。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細はLICENSEファイルを参照してください。






