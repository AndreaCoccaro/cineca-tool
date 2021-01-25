# cineca-tool

Italian researcher need to mantain their list of publications updated in cineca. The cineca portal is not adeguate to handle a large number of publications with a large number of authors, as is typically the case in HEP.

This repository contains
   * a python script to slim the information associated to ATLAS publications, when downloaded from WoS
   * a repository of ATLAS publications, in full and slimmed format, in the ISI WoS format

# workflow

   1) download publications in 'plain text' format from WoS, see [WoS](https://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&SID=C5dwUKRv8irYfJlZtEx&search_mode=GeneralSearch)
   2) enjoy *script-cineca.py* to create a slimmed version of the downloaded file
   3) the resulting file will come with the associated WoS ID, the analogous SCOPUS ID would be nice to have as well, but needs to be searched by hand, for example [here](https://www.lebedev.ru/en/articles.html)

# tips

Some tips collected while interacting with the cineca portal
   * uploading large files won't work. Slimmed files in the ISI WoS format containing 50 publications works nice. If the full list of authors is also uploaded, the number of publications per file needs to be dramatically shorter, typically 10
   * publications in PRD are not automatically recognised by cineca, and a manual search by ISSN is needed to fix the issue. Cineca thinks that these publicaions are in journal with ISSN 1550-7998 which is no longer active since 2015, while the correct ISSN is 2470-0029
