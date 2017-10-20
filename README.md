# Incomprehensible Ex
Sublime Text plugin to read or edit incomprehensible files as docx, odt, pdf, epub and more.

--------------------------------------------------------------------------------------------

About

    Recognized extensions in read mode:
        csv, doc, docx, eml, epub, gif, jpg, json, html, mp3, msg, odt, ogg, pdf, png, pptx, ps, rtf, tiff,
        txt, wav, xlsx, xls

    Extensions that can be dictated in edit mode:
        'asciidoc', 'beamer', 'commonmark', 'context', 'docbook', 'docx', 'dokuwiki', 'dzslides', 'fb2', 'haddock',
        'html', 'html5', 'icml', 'latex', 'man', 'markdown', 'markdown_github', 'markdown_mmd', 'markdown_phpextra',
        'markdown_strict', 'mediawiki', 'native', 'odt', 'opendocument', 'opml', 'org', 'plain', 'revealjs', 'rst',
        'rtf', 's5', 'slideous', 'slidy', 'texinfo', 'textile'

Configuration

    In the configuration you can configure the extensions that will be recognized by the plugin in read mode.
    To configure the extensions do:
        1 - Use command (Ctrl+Shift+p) and type 'Incomprehensible' or 'edit mode'.
        2 - Choose the option "Incomprehensible Ex: Manage Settings".
        3 - Configure the extensions in the file.

    You can set a default operating mode.
    To configure the mode do:
        1 - Use command (Ctrl+Shift+p) and type 'Incomprehensible' or 'edit mode'.
        2 - Choose the option "Incomprehensible Ex: Manage Settings".
        3 - Configure the default mode in the file.

Installation

    The easiest way to install this plugin, is to use the Package Control.

    [READ MODE]
    To use this plugin you must have installed textract in your system
        - To install textract see: http://textract.readthedocs.io/en/latest/installation.html#

    [EDIT MODE]
    To use the edit mode, you must have installed 'pandoc' in your system.
        - To install pandoc see: http://pandoc.org/installing.html

Usage

    Just open a file with the desired extension, as long as it is configured in the plugin settings file,
    a new file with the extension [.inex] will open.

    [EDIT MODE] [!WARNING!]
        In edit mode, if you save a document you will lose the styles and formatting of the document because of the file conversion.
