# Objective

This code is an example of how to upload images to `test.wikipedia.org`. The code shows how metadata templates are just included directly into the `comments` parameter of the `upload` action against the wiki API.

# Justification

The Wiki documentation for wikimedia is not very clear about how to include data during the upload process. I originally discover this by applying edits to an already uploaded image.

In edit the pages (the files page) content can be edited with different argumetns including: `text`, `appendtext`, `prependtext`, or even a combination of `section` with `sectiontitle` and `text`.

## pywikibot

Although I tried to implement the pywikibot to run my objective, the documentation was not as friendly as the wiki [API](TestWikiAPI).

[TestWikiAPI]: https://test.wikipedia.org/w/api.php
