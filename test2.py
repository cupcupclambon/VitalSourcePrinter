import PyPDF2
import pyautogui
import os
import sys
import time
import warnings
from tkinter import Tk
import tkinter.filedialog as filedialog

def main():
    start_time = time.time()
    warnings.filterwarnings("ignore")

    print("Welcome to the VitalSource Ebook Printer.\n")

    while True:
        try:
            NumberStart = int(input("First page: "))
            NumberEnd = int(input("Last page: "))
            if NumberStart > NumberEnd:
                print("First page must be less than last page.\n")
                continue
            break
        except ValueError:
            print("Please enter valid page numbers.\n")

    NumberList = [str(i) for i in range(NumberStart, NumberEnd + 1)]

    root = Tk()
    root.withdraw()
    filedir = filedialog.askdirectory() + '//'

    if len(NumberList) % 2 != 0:
        NumberList.append(NumberList[-1])

    print("\nClick on the active VitalSource window to get started.\nThe program will start in: 8")
    for seconds in range(8, 0, -1):
        time.sleep(1)
        print(seconds)
    print("Starting now...\n")

    def process_pages(start):
        for page in range(start, len(NumberList), 2):
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'p')
            pyautogui.press(keys='tab', presses=2, interval=0.25)
            pyautogui.press('delete', 5)
            pyautogui.typewrite(NumberList[page], interval=0.25)
            pyautogui.press('tab')
            pyautogui.press('delete', 5)
            pyautogui.typewrite(NumberList[page + 1])
            time.sleep(3)
            pyautogui.typewrite(['tab', 'enter'], interval=0.25)
            time.sleep(12)
            pyautogui.press('tab', presses=4, interval=0.25)
            pyautogui.press('enter', interval=0.50)
            time.sleep(2)
            pyautogui.typewrite("File2", interval=0.5)
            time.sleep(2)
            pyautogui.press('enter', interval=0.5)
            
            while not os.path.isfile(filedir + "Ebook.pdf"):
                time.sleep(2)
            while not os.path.isfile(filedir + "File2.pdf"):
                time.sleep(2)

            pdf1File = open(filedir + 'Ebook.pdf', 'rb')
            pdf2File = open(filedir + 'File2.pdf', 'rb')
            pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
            pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
            pdfWriter = PyPDF2.PdfFileWriter()

            for pageNum in range(pdf1Reader.numPages):
                pdfWriter.addPage(pdf1Reader.getPage(pageNum))
            for pageNum in range(pdf2Reader.numPages):
                pdfWriter.addPage(pdf2Reader.getPage(pageNum))

            pdfOutputFile = open(filedir + 'Ebook1.pdf', 'wb')
            pdfWriter.write(pdfOutputFile)
            pdfOutputFile.close()
            pdf1File.close()
            pdf2File.close()

            os.remove(filedir + 'Ebook.pdf')
            os.remove(filedir + 'File2.pdf')
            os.rename(filedir + 'Ebook1.pdf', filedir + 'Ebook.pdf')
            print(f"Page: {page + 2} of {len(NumberList)}")

    process_pages(0)
    elapsed_time = time.time() - start_time
    print("\nDone!")
    print(f"This took {elapsed_time / 3600:.2f} hours.")

if __name__ == "__main__":
    main()
