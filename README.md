# VitalSourcePrinter(改造版2025年)
Code to legally and automatically print your purchased e-books from VitalSource.com

This program automates the printing of PDF's from the VitalSource Bookshelf. The VitalSource Bookshelf usually only lets the user print 2 pages at a time, and manually doing this for the entire book is tedious and time consuming. This program automatically prints any selection or the entirety of an e-book, page by page, and rapidly concatenates everything into a single PDF file. As this program makes use of keyboard automation, this process assumes that the user is away from the computer for the duration of the process, though the user at any time can stop the script from continuing. 

New scripts have been introduced for situations where the pages appear like "4-1" and situations where the user is required to press Ctrl + Pagedown to go to the next chapter.

Legal disclaimer: 
Usage of any content produced by this script must abide the terms set out by VitalSource at https://support.vitalsource.com/hc/en-us/articles/204612518. In a nutshell this means no commercial usage or distribution, and only personal use is allowed. If you do decide to mass distribute, do so at your own risk since your name and email will appear on the top page of each print out.

## Getting Started

Here's a link to the video tutorial (made for the original script): https://www.youtube.com/watch?v=6TUxpMezwUA

To get started you are going to need a working version of Python 3 because as of this time the only working script is written in Python 3. Visit https://www.python.org/downloads/ to find the desired version for your operating system.

If you're just installing Python 3 for the first time or reinstalling it, I highly recommend using Python 3.4.0 or higher as this version comes built with a feature called pip that easily allows you to install approved third party packages not included with Python by default. To find more information about pip, visit: https://pypi.python.org/pypi/pip. 

Note: If you're on Linux or Ubuntu, pip doesn't come with 3.4.0 or higher. The part of this section involving pip is referenced from https://automatetheboringstuff.com, a book that is a large inspiration for this program and one that I would highly recommend to anyone learning python. To learn how to get pip on Ubuntu or Linux, visit https://automatetheboringstuff.com/appendixa/

You're also going to need the VitalSource Bookshelf software, which you can find at: https://support.vitalsource.com/hc/en-us/articles/201344733-Bookshelf-Download-Page

The next things you need are the following third party packages: 
- PyPDF2
- pyautogui

You of course must have Python 3 to install these packages. The easiest way to securely download and install these packages involves calling pip from your command prompt / terminal. If you don't have pip installed, you will have to manually download and insert these packages:
https://docs.python.org/3/install/

This guide will proceed using pip. Navigate to your terminal and type the following commands one line at a time:


Windows users

```
pip install --upgrade pip
pip install PyPDF2
pip install Pillow
pip install pyautogui
```
OS X and Linux users:

```
pip3 install --upgrade pip
pip3 install PyPDF2
pip3 install Pillow
pip3 install pyautogui
```

The first command is run as a precatuionary step to catch an error with Pillow not installing correctly and a missing dependency. If Pillow still doesn't install correctly, try ```easy_install Pillow  ``` if you're on Windows and ```sudo easy_install Pillow``` if you're on Mac or Linux. 

Now you're ready to get started. In the case that you find the remainder of this tutorial visually hard to follow, be sure to check out the tutorial video.

## Walkthrough 

This section will go through each part of the process step-by-step. 

### Pre-requisites

Even with the necessary packages and software components, a few things need to be set before the script can function correctly.

First open up VitalSource Book Shelf. Double click on the ebook you want to print to get it to pop-out. Now that you have it in place, make a new destination folder for your printed ebook to be located. A simple example could be a folder on your desktop called "Ebook". Make sure this folder doesn't contain a pdf named "Ebook.pdf," as that is used as a temp file name by the script.

The next part is very important. The script will not work unless these three pre-conditions are met:

- You need to have a PDF printer that doesn't automatically open the newly printed PDF
- You need to print a "sample pdf" at the location of your destination ebook folder
- You need sufficient disk space to save, as the output PDF tends to be large in size (possibly up to a GB or more)

Firstly, you need to have a PDF printer that doesn't automatically open the newly printed PDF. For example, Adobe does this. You will need to disable this functionality if want the script to work. In the future, the script can be improved to account for this situation. One working PDF printer that comes with Windows is "Microsoft Print to PDF" and I reccommend using that if you are on Windows. I'm currently not too familiar with PDF printers for OS X and other systems and it would be appreciated if anyone can give an example of the analog for "Microsoft Print to PDF." Otherwise, any PDF printer that doesn't open new PDF's automatically, or one that can turn off this feature, will work.

The second condition is that a "sample pdf" needs to be printed at the location of your ebook folder. This needs to be done to ensure that all intermediary PDF files being printed from VitalSource Bookshelf are in that ebook folder by default, as the script relies on this location. Ctrl + P and print a sample 2 page PDF to your ebook folder and that will set VitalSource to do its default printing there.

The last condition is that you must have enough disk space to save your ebook. A 1270 page ebook took up 673 MB, which translates to about 1.89 MB per page. Bare in mind that ebooks widely differ in their content and hence there is a lot of variance in the possibilities of disk space usage so the final memory of the finished ebook could be widely different. To reduce the memory size of the finished ebook, various free PDF compressers exist such as https://smallpdf.com/compress-pdf, which has no file size limits and can reduce the size by up to 75% (the 1270 page ebook turned from 673 MB into 179 MB!). For safety, I reccommend having at least 1 GB of disk space available.

### Executing the script

If you don't know what you are doing, open VitalSourcePrinter.py in an environment of your choice. Python usually comes with a default environment called IDLE that can be used if you don't have a custom environment that supports Python. This can be easily performed by right clicking the .py file and clicking "edit with IDLE." 

For viewing and operational purposes, it's a good idea to have the code view and the VitalSource ebook window close to each other. Once the script runs, it will automate keyboard actions so you need to be able to call focus to the VitalSource ebook window by clicking on it before the keyboard automations start. This will be touched upon soon.

Now run the script. Follow the prompt and input the desired page ranges for roman numerals and regular numbers. If no roman numerals are desired, input "None" or "none". Only valid numbers and roman numerals work. If you're using another script aside from the original script, you will be prompted for other fields such as chapter count and chapter last page.

Side note: Typing names like "inside front cover" won't be recieved by the script, and hence if you would like pages with specific names to be included, you would need to manually print those out and separately concatenate them to the finished Ebook pdf. This could be another feature to be added in the future.

After the page ranges are entered, the program will prompt you to pick a folder. You must pick the ebook folder you printed your sample PDF in. After picking the folder, a countdown of 8 seconds will begin before the printing automation starts. Click on the active VitalSource window and the script will run. 

Note: To stop the script at any time, mouse over to the console window where the script is running and close it. It will say "the program is still running, do you want to kill it?" Choose "yes".

Once the script runs to completion, you will see the message "done!" and the elapsed time in hours.

## Remarks

A 1270 page ebook takes around 3.5 hours to print. That's about 6 pages a minute. Not too bad, though not perfect. The lengthy time is due to the design of the code, which was informed by trial and error. There were situations where names and keyboard operations would skip or not perform correctly due to happening too fast for VitalSource BookShelf to process. Moreover, intermediary files generated by VitalSource BookShelf were not recognized by the system if there was no waiting time after their generation, so waiting time was introduced to catch this error. At the end of the day (pun intended), you can use this script to print any ebook you want while sleeping, or when you are away from your computer of course.

I hope this program is helpful and if any problems or issues arise, I encourage you to reach out to me and I will do my best to fix them. Any ideas, suggestions, or improvements would also be welcome.

~LifeAlgorithm
