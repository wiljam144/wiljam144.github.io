2023-07-22

# How I made this site

So this version of the website is my third revision of the site.
You can check the old version of the site [here](https://wiljam144.github.io/webpage-v2).

## The Problem

The major problem was that blog posts and articles were completely detached
from the website and felt disjoined, I still don't think I solved the issue completely,
since the articles are still in separate pages, but it should be better.
Also the last issue with the old version is that it was just ugly.

## The Stack

So I wanted to have a plain-text format for my writings and blog posts, and
something html-like to use for other pages. My first thought was jekyll, but
I decided against it, because I didn't feel it gave me enough control, and I
would much rather style my webpage in css than create themes and things like that.
But there wasn't literally any frameworks or tools that I would be satisfied with,
and the only logical conclusion was to create my own! Well that may be an exagerration,
since the whole build system is just a simple python script that copies every file that isn't Markdown,
and converts the Markdown files into HTML with python's markdown module.
Maybe someday I will use it as an inspiration for my own static-site generator like jekyll.
I also decided to use [htmx](https://htmx.org/) to give the site that extra bit of interactivity.

## The Styling

I was studying some more advanced topics and concepts about graphs when I decided to
remake my website. That's why I wanted to have something that looks like a graph.
I found the [particles.js](https://vincentgarreau.com/particles.js/) JS library that
allowed me to do exactly what I wanted with the background of the website.
