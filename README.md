# make_base64_img_link.py
Generate base 64 img tags from png files for inclusion in html

make_base64_img_link.py is Copyright &copy; 2019 by Tony Rein. It is released under a GPL license and is free for anyone to use and/or modify as desired.

There is, of course, no warranty that it will work properly, or that it will not cause problems, including data loss or personal injury. Use it at your own risk and discretion.

I was working recently on an Excel application and decided to use an HTML file to supply documentation for the user. The HTML file has some screenshots, and I wanted to embed those screenshots directly into the HTML code instead of using separate files. I already had the screenshots as PNG files and wanted a shortcut to generate base 64 image tags from the files.

In retrospect, it would have been quicker to manually generate them, but maybe this will come in handy for someone else.

To use the app, just pass the name of the directory containing the image files. For each .png file in the directory, an html image tag will be generated as follows:<br/>
*&lt;img src="data:image/png;base64,[base 64 string]"&gt;*<br/>
 and the tag will be written to a file called<br/> *[source&nbsp;file]_base64.txt*

Caution: If the destination file already exists, it will be overwritten without warning.

Now you can paste the contents of each base 64 file into your HTML document.
