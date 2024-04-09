import os
import re
import sys
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO

def extract_text_from_pdf(file_path):
    output_string = StringIO()
    with open(file_path, 'rb') as fin:
        try:
            extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='text', codec='utf-8')
        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)
    return output_string.getvalue()

def clean_extracted_text(text):
    text = text.replace('-\n', '')
    text = re.sub(r'\s+', ' ', text)
    return text

def create_clean_text_files(pdf_dir, clean_text_dir):
    if not os.path.exists(clean_text_dir):
        os.makedirs(clean_text_dir)

    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            clean_text_filename = pdf_file.replace('.pdf', '.txt')
            clean_text_path = os.path.join(clean_text_dir, clean_text_filename)

            if not os.path.exists(clean_text_path):
                extracted_text = extract_text_from_pdf(pdf_path)
                clean_text = clean_extracted_text(extracted_text)

                with open(clean_text_path, 'w', encoding='utf-8') as file:
                    file.write(clean_text)
                print(f"Created clean text file for: {pdf_file}")

def search_texts(clean_text_dir, keywords_phrases):
    print(f"Searching for keywords and phrases: {keywords_phrases}")

    for text_file in os.listdir(clean_text_dir):
        if text_file.endswith('.txt'):
            text_path = os.path.join(clean_text_dir, text_file)
            with open(text_path, 'r', encoding='utf-8') as file:
                text = file.read().lower()

                all_found = True
                for kp in keywords_phrases:
                    # フレーズ内の単語間に任意の空白が存在する可能性があるため、
                    # フレーズを構成する単語間に\s+を挟む正規表現を使用します。
                    if ' ' in kp:  # フレーズがスペースを含む場合
                        pattern = r'\b{}\b'.format(r'\s+'.join(re.escape(word) for word in kp.split()))
                    else:  # 単一のキーワードの場合
                        pattern = r'\b{}\b'.format(re.escape(kp))

                    if not re.search(pattern, text, re.IGNORECASE):
                        all_found = False
                        break

                if all_found:
                    print(f"Found in: {text_file.replace('.txt', '.pdf')}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python pdf_search.py <pdf_dir> <search_terms>")
        sys.exit(1)
    
    pdf_dir = sys.argv[1]
    clean_text_dir = os.path.join(os.path.dirname(pdf_dir), os.path.basename(pdf_dir) + '-cache')
    
    create_clean_text_files(pdf_dir, clean_text_dir)
    
    args_str = ' '.join(sys.argv[2:])
    keywords = re.findall(r'"[^"]*"|\S+', args_str)
    keywords = [keyword.strip('"').lower() for keyword in keywords]

    if len(keywords) > 5:
        print("Error: Please specify up to 5 keywords.")
        sys.exit(1)

    search_texts(clean_text_dir, keywords)
