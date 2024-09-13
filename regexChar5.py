import re

def find_tag(text):
    regex = re.compile(r'<(\w{5,})>')
    mo = regex.findall(text)
    return mo

html_text = """<html>

<head>

<title>Page Title</title>

</head>

<body>

<div class="tut-list tut-list-new tut-row ">

<div class="tut-list-primary"> <div class="tut-vote">

<video>intro</video>

<span class="count">50</span> <span class="tut-upvotes-text hidden">Upvotes</span> </a> </div> 

<center>k="11" rel="nofollow"></center>

<span class="tutorial-title-txt">The Complete Data Structures and Algorithms Course in Python</span>

<span class="tut-title-link">  <span class="js-tutorial" data-id="3529"

title="The Complete Data Structures and Algorithms Course in Python" target="_blank">(udemy.com)</span> 

</span>  </a></div> <div class="action-footer">

<form class="save-tutorial-form" method="post" <button></button> </form>

</body>

</html>" find_tag(html_text)"""