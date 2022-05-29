from art import*
import pdfplumber
from gtts import gTTS
from pathlib import Path




def pdf_to_mp3(file_path='test.pdf', language='ru'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':


        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)

        # with open('text1.txt', 'w') as file:
        #     file.write(text)

        text = text.replace("\n", '')

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')


        # with open('text2.txt', 'w') as file:
        #     file.write(text)
        #     return 'File exists!'
    else:
        return 'File not exists, check the file path'

def main():
    tprint('PDF_>>_MP3')
    print(pdf_to_mp3(file_path='C:\\Users\iphed\PycharmProjects\pythonProject\pdftomp3\pdf_files\pdf.pdf'))

if __name__ =='__main__':
    main()
