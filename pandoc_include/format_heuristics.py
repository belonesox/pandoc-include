import os

extensionFormats = {
    ".adoc"     : "asciidoc",
    ".asciidoc" : "asciidoc",
    ".context"  : "context",
    ".ctx"      : "context",
    ".db"       : "docbook",
    ".doc"      : "doc",
    ".docx"     : "docx",
    ".dokuwiki" : "dokuwiki",
    ".epub"     : "epub",
    ".fb2"      : "fb2",
    ".htm"      : "html",
    ".html"     : "html",
    ".icml"     : "icml",
    ".json"     : "json",
    ".latex"    : "latex",
    ".lhs"      : "markdown+lhs",
    ".ltx"      : "latex",
    ".markdown" : "markdown",
    ".mkdn"     : "markdown",
    ".mkd"      : "markdown",
    ".mdwn"     : "markdown",
    ".mdown"    : "markdown",
    ".Rmd"      : "markdown",
    ".md"       : "markdown",
    ".ms"       : "ms",
    ".muse"     : "muse",
    ".native"   : "native",
    ".odt"      : "odt",
    ".opml"     : "opml",
    ".org"      : "org",
    ".pdf"      : "pdf",
    ".pptx"     : "pptx",
    ".roff"     : "ms",
    ".rst"      : "rst",
    ".rtf"      : "rtf",
    ".s5"       : "s5",
    ".t2t"      : "t2t",
    ".tei"      : "tei",
    ".tei.xml"  : "tei",
    ".tex"      : "latex",
    ".texi"     : "texinfo",
    ".texinfo"  : "texinfo",
    ".text"     : "markdown",
    ".textile"  : "textile",
    ".txt"      : "markdown",
    ".wiki"     : "mediawiki",
    ".xhtml"    : "html",
    ".ipynb"    : "ipynb",
    ".csv"      : "csv",
    ".bib"      : "biblatex",
    ".xml"      : "xml",
    ".xslt"     : "xslt",
}

def formatFromPath(path: str):
    ext = os.path.splitext(path)[1]
    if ext in extensionFormats:
        return extensionFormats[ext]
    return None
