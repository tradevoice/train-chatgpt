# pine script v5 user manual




# File Descriptions
download_chapters.py:
> Automates the process of downloading each chapter of the Pine Script Manual v5 from TradingView's website. Saves each chapter as a separate PDF file.
> Each online section is converted to a pdf page.
> MacOS:  Use this to combine files to one pdf.
> https://support.apple.com/guide/mac-help/combine-files-into-a-pdf-mchl21ac2368/mac

combine_pdfs.py:
> Takes all downloaded PDF chapters and combines them into a single text file for easier navigation and search.

PineScript_Manual_v5_Combined.txt:
> A text file containing all the individual chapters combined for your convenience.

PineScript_Manual_v5_Chapters/:
> A folder containing individual PDF chapters of the Pine Script Manual v5, each named according to its chapter title.

# Usage
Run download_chapters.py to download each chapter:
> python download_chapters.py

Run combine_pdfs.py to combine the PDFs into one text file:
> python combine_pdfs.py

Browse the PineScript_Manual_v5_Combined.txt or individual chapters inside PineScript_Manual_v5_Chapters/ for the information you need.
> Upload PineScript_Manual_v5_Combined.txt to ChatGPT-4


# License
This project is licensed under the MIT License. See the LICENSE.md file for details.

# Acknowledgments
Thanks to TradingView for providing the Pine Script Manual v5.
Special thanks to all contributors of this project.