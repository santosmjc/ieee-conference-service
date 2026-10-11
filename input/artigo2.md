---
title: "Preparation of a Formatted Conference Paper for an IEEE Power & Energy Society Conference"
author:
  - "Fábio Oliveira"
  - "Ivan Horoshko"
  - "Lucas S."
  - "Márcio Santos"
  - "Ricardo Duarte"

affiliation:
  - "Master's Degree in Cybersecurity"
  - "University of Aveiro"
  - "Aveiro, Portugal"
date: ""
lang: en-US
documentclass: IEEEtran
classoption:
  - conference
  - letterpaper
abstract: |
  Basic guidelines for the preparation of a technical paper for an IEEE Power & Energy Society Conference are presented. This electronic document is a “live” template. The various components of your paper, including title, text, and headings, are already defined, as illustrated by the portions given in this document. The abstract is limited to 150 words and cannot contain equations, figures, tables, or references. It should concisely state what was done, how it was done, principal results, and their significance.
keywords:
  - "Conference papers"
  - "Formatting"
  - "IEEE"
  - "Manuscript preparation"
  - "Templates"
---

<!--
autores simples:

author:
  - "Fábio Oliveira"
  - "Ivan Horoshko"
  - "Lucas S."
  - "Márcio Santos"
  - "Ricardo Duarte"

affiliation:
  - "Master's Degree in Cybersecurity"
  - "University of Aveiro"
  - "Aveiro, Portugal"

-----------

author:
  - name: "Fábio Oliveira"
    program: "Master's in Cybersecurity"
    institution: "University of Aveiro"
    location: "Aveiro, Portugal"
    email: "fabio.oliveira@ua.pt"

  - name: "Ivan Horoshko"
    program: "Master's in Cybersecurity"
    institution: "University of Aveiro"
    location: "Aveiro, Portugal"
    email: "ivan.horoshko@ua.pt"

  - name: "Lucas S."
    program: "Master's in Cybersecurity"
    institution: "University of Aveiro"
    location: "Aveiro, Portugal"
    email: "lucas.s@ua.pt"

  - name: "Márcio Santos"
    new-row: true
    program: "Master's in Cybersecurity"
    institution: "University of Aveiro"
    location: "Aveiro, Portugal"
    email: "marcio.santos@ua.pt"

  - name: "Ricardo Duarte"
    program: "Master's in Cybersecurity"
    institution: "University of Aveiro"
    location: "Aveiro, Portugal"
    email: "ricardo.duarte@ua.pt"
-----------
Converted from the text supplied by the user. This is the instructional
IEEE PES template, not a research article about the Fleet Manager.

The compiler must render title/authors/abstract/keywords from the YAML
metadata. Metadata support depends on the local ieee-conference template.
Do not render the abstract a second time as a normal section.

Use compiler-controlled section numbering. Do not add Roman numerals to
these headings manually. The supplied template specifies US Letter paper.

Replace author placeholders and affiliation information before publication.
The source supplies placeholders, not actual author names or affiliations:

First affiliation:
  Line 1: Authors Name/s per 1st Affiliation
  Line 2: Author’s Name/s per 1st Affiliation
  Line 3: Dept. name of organization
  Line 4: Name of organization, acronyms acceptable
  Line 5: City, Country
  Line 6: E-mail address if desired

Second affiliation:
  Line 1: Authors Name/s per 2nd Affiliation
  Line 2: Author’s Name/s per 1st Affiliation [as supplied in the source]
  Line 3: Dept. name of organization
  Line 4: Name of organization, acronyms acceptable
  Line 5: City, Country
  Line 6: E-mail address if desired

Affiliation rendering must be configured using the local template's schema;
no unverified affiliation metadata schema is assumed here.

Sponsor placeholder from the source: Identify applicable sponsor/s here.
Configure this as an unnumbered first-page footnote if applicable.

The extracted source contains no actual figure. Its figure caption is
preserved as text rather than referencing a nonexistent image.
Bibliographic examples are retained as supplied; they are not verified.
-->

# Introduction

This template provides authors with most of the formatting specifications needed for preparing electronic versions of PES Conference papers. All standard paper components have been specified for three reasons:

1. Ease of use when formatting individual papers.
2. Automatic compliance to electronic requirements that facilitate the concurrent or later production of electronic products.
3. Conformity of style throughout a conference’s proceedings.

Margins, column widths, line spacing, and type styles are built-in. Examples of the type styles are provided throughout this document. Some components, such as multi-leveled equations, graphics, and tables, are not prescribed, although the various table text styles are provided. The formatter will need to create these components, incorporating the applicable criteria that follow.

The author shall provide up to five keywords, in alphabetical order, to help identify the major topics of the paper. The thesaurus of IEEE indexing keywords is available at <https://www.ieee.org/publications/services/thesaurus-access-page.html>.

# Ease of Use

## Template

This template has been tailored for output on US letter-sized paper.

## Maintaining the Integrity of the Specifications

The template is used to format your paper and style the text. All margins, column widths, line spaces, and text fonts are prescribed; please do not alter them.

You may note peculiarities. For example, the heading margin in this template measures proportionately more than is customary. This measurement and others are deliberate, using specifications that anticipate your paper as one part of the entire proceedings, and not as an independent document. Please do not revise any of the current designations.

# Conference Paper Preparation

Conference papers are limited to a maximum of five pages. Please use automatic hyphenation and check your spelling. Additionally, be sure your sentences are complete and that there is continuity within your paragraphs. Check the numbering of your graphics, including figures and tables, and make sure that all appropriate references are included.

Please take note of the following items when proofreading spelling and grammar.

## Abbreviations and Acronyms

Define abbreviations and acronyms the first time they are used in the text, even after they have been defined in the abstract. Abbreviations such as IEEE, SI, ac, dc, and rms do not have to be defined. Do not use abbreviations in the title or section headings unless they are unavoidable.

## Units

- Metric units are preferred for use in IEEE publications in light of their global readership and the inherent convenience of these units in many fields. In particular, the use of the International System of Units (SI) is advocated. This system includes a subsystem of units based on the meter, kilogram, second, and ampere (MKSA). U.S. Customary units, or British units, may be used as secondary units in parentheses. An exception is when U.S. Customary units are used as identifiers in trade, such as a 3.5-inch disk drive.
- Avoid combining SI and U.S. Customary units, such as current in amperes and magnetic field in oersteds. This often leads to confusion because equations do not balance dimensionally. If you must use mixed units, clearly state the units for each quantity that you use in an equation.
- Do not mix complete spellings and abbreviations of units: use “Wb/m²” or “webers per square meter”, not “webers/m²”. Spell out units when they appear in text: “a few henries”, not “a few H”.
- Use a zero before decimal points: “0.25”, not “.25”. Use “cm³”, not “cc”.

## Equations

The equations are an exception to the prescribed specifications of this template. In the Word version, you will need to determine whether your equation should be typed using either the Times New Roman or the Symbol font, with no other font. To create multi-leveled equations, it may be necessary to treat the equation as a graphic and insert it into the text after your paper is styled.

Use of the Microsoft Equation Editor or the MathType commercial add-on for MS Word for math objects in your paper is permissible. “Float over text” should not be selected.

Number equations consecutively. Equation numbers, within parentheses, should be positioned flush right, as in (1). To make your equations more compact, you may use the solidus (/), the exp function, or appropriate exponents. Italicize Roman symbols for quantities and variables, but not Greek symbols. Use a minus sign rather than a hyphen. Punctuate equations with commas or periods when they are part of a sentence, as in

```{=latex}
\begin{equation}
\alpha - \beta + \delta = \chi.
\label{eq:example}
\end{equation}
```

The equation above is centered. Be sure that its symbols have been defined before or immediately following it. Use “(1)”, not “Eq. (1)” or “equation (1)”, except at the beginning of a sentence: “Equation (1) is …”.

## Footnotes

Number footnotes separately in superscripts. Place the actual footnote at the bottom of the column in which it was cited. Do not put footnotes in the reference list. Use letters for table footnotes.

## Some Common Mistakes

- The word “data” is plural, not singular.
- The subscript for the permeability of vacuum, $\mu_0$, and other common scientific constants is zero with subscript formatting, not a lowercase letter “o”.
- In American English, commas, semicolons, periods, question marks, and exclamation marks are located within quotation marks only when a complete thought or name is cited, such as a title or full quotation. When quotation marks are used instead of a bold or italic typeface to highlight a word or phrase, punctuation should appear outside the quotation marks. A parenthetical phrase or statement at the end of a sentence is punctuated outside the closing parenthesis (like this). (A parenthetical sentence is punctuated within the parentheses.)
- A graph within a graph is an “inset”, not an “insert”. The word “alternatively” is preferred to “alternately”, unless you really mean something that alternates.
- Do not use the word “essentially” to mean “approximately” or “effectively”.
- In your paper title, if the words “that uses” can accurately replace the word “using”, capitalize the “u”; if not, keep “using” lowercase.
- Be aware of the different meanings of the homophones “affect” and “effect”, “complement” and “compliment”, “discreet” and “discrete”, and “principal” and “principle”.
- Do not confuse “imply” and “infer”.
- The prefix “non” is not a word; it should be joined to the word it modifies, usually without a hyphen.
- There is no period after “et” in the Latin abbreviation “et al.”.
- The abbreviation “i.e.” means “that is”, and “e.g.” means “for example”.

# Using the Template

This document should be used as a template for preparing your conference paper. You may type over sections of the document, cut and paste into it, and/or use markup styles.

Duplicate the template file using the Save As command, and use the naming convention prescribed by your conference for the name of your paper.

## Authors and Affiliations

The template is designed so that author affiliations are not repeated each time for multiple authors of the same affiliation. Please keep affiliations as succinct as possible; for example, do not differentiate among departments of the same organization. The original Word template was designed for two affiliations.

### Authors of Only One Affiliation

To change the default in the Word template, adjust it as follows:

1. Selection: highlight all author and affiliation lines.
2. Change number of columns: select the Columns icon from the MS Word Standard toolbar and select “1 Column”.
3. Deletion: delete the author and affiliation lines for the second affiliation.

### Authors of More Than Two Affiliations

To change the default in the Word template, adjust it as follows:

1. Selection: highlight all author and affiliation lines.
2. Change number of columns: select the Columns icon from the MS Word Standard toolbar and select the number of columns desired.
3. Highlight the author and affiliation lines of affiliation 1 and copy the selection.
4. Formatting: insert one hard return immediately after the last character of the last affiliation line. Paste the copy of affiliation 1. Repeat as necessary for each additional affiliation.
5. Reassign number of columns: place your cursor to the right of the last character of the last affiliation line of an even-numbered affiliation. For example, if there are five affiliations, place your cursor at the end of the fourth affiliation. Drag the cursor up to highlight all lines above it. Select “2 Columns”. If there is an odd number of affiliations, the final affiliation will be centered on the page; all previous affiliations will be in two columns.

## Identify the Headings

Headings are organizational devices that guide the reader through your paper. There are two types: component headings and text headings.

Component headings identify the different components of your paper and are not topically subordinate to each other. Examples include Acknowledgment and References. In the Word template, the correct style for these is “Heading 5”. Use “figure caption” for figure captions and “table heading” for table titles. Run-in headings, such as “Abstract”, require a style in addition to the style provided by the dropdown menu to differentiate the heading from the text.

Text headings organize the topics on a relational, hierarchical basis. The paper title is the primary text heading because all subsequent material relates to and elaborates on it. If there are two or more subtopics, the next heading level should be used. Conversely, if there are not at least two subtopics, no subheadings should be introduced. Styles named “Heading 1”, “Heading 2”, “Heading 3”, and “Heading 4” are prescribed in the Word template.

## Figures and Tables

### Positioning Figures and Tables

Large figures and tables may span both columns. Figure captions should be below figures; table headings should appear above tables. Insert figures and tables after they are cited in the text, as close to the citation as possible. Use the abbreviation “Fig. 1”, even at the beginning of a sentence.

The following is the sample table from the supplied template, reconstructed from its extracted text.

```{=latex}
\begin{table}[htbp]
\caption{Table Type Styles}
\label{tab:type-styles}
\centering
\small
\begin{tabular}{|l|l|l|l|}
\hline
\shortstack{Table\\Heading} & \multicolumn{3}{c|}{Table Column Heading} \\
\cline{2-4}
 & \shortstack{Table column\\subheading} & Subheading & Subheading \\
\hline
copy & More table copy\textsuperscript{a} & & \\
\hline
\end{tabular}
\par\smallskip
\footnotesize\textsuperscript{a}Example of a table footnote.
\end{table}
```

In the Word version, a text box is suggested for inserting a graphic, ideally a 300 dpi TIFF or EPS file with all fonts embedded, because this is somewhat more stable than directly inserting a picture. To make the frame invisible, select Text Box > Colors and Lines in the Format menu and choose No Fill and No Line.

### Figure Labels

Use 8-point Times New Roman for figure labels in the Word template. Use words rather than symbols or abbreviations for figure axis labels to avoid confusing the reader. For example, write “Magnetization” or “Magnetization, M”, not just “M”.

If units are included, present them in parentheses. Write “Magnetization (A/m)”, not just “A/m”. Do not label axes with a ratio of quantities and units; for example, write “Temperature (K)”, not “Temperature/K”.

Figures and tables should be numbered consecutively. Use Arabic numerals for figures and Roman numerals for tables.

Example caption from the source: “Figure 1. Example of a figure caption.” No corresponding figure was included in the supplied extracted text.

# Acknowledgment {.unnumbered}

The preferred American spelling of “acknowledgment” is without an “e” after the “g”. Avoid expressions such as “One of us (R. B. G.) thanks …”. Instead, try “R. B. G. thanks …”. Put sponsor acknowledgments in an unnumbered footnote on the first page.

The following is an example of an acknowledgment:

The authors gratefully acknowledge the contributions of T. Edison, G. Westinghouse, N. Tesla, A. Volta, and A. Ampere to the electric power industry.

# Reference Preparation Guidelines {.unnumbered}

References are important to the reader; therefore, each citation must be complete and correct. There is no editorial check on references. An incomplete or wrong reference will be published unless caught by a reviewer and will detract from the authority and value of the paper. References should be readily available publications.

List only one reference per reference number. If a reference is available from two sources, each should be listed as a separate reference.

Number citations consecutively within brackets [1]. Sentence punctuation follows the bracket [2]. Multiple references [3], [4] are each numbered with separate brackets; ranges may be written as [4]–[6]. Refer simply to the reference number, as in [7], rather than “Ref. [7]” or “reference [7]”, except at the beginning of a sentence: “Reference [7] was the first …”.

Unless there are six authors or more, give all authors’ names; do not use “et al.”. Papers that have not been published, even if submitted for publication, should be cited as “unpublished” [8]–[10]. Capitalize only the first word in a paper title, except for proper nouns and element symbols. For papers published in translation journals, give the English citation first, followed by the original foreign-language citation [11]. Papers accepted for publication, but not yet published, should be cited as “in press” [12].

Samples of formats for periodicals [1], [2], books [3]–[5], technical reports [6], [7], unpublished papers [8]–[10], translation journals [11], accepted papers [12], conference proceedings [13], dissertations [14], standards [15], and patents [16] follow.

<!-- Raw LaTeX below preserves IEEE reference numbering without requiring
an additional BibTeX file or an unprovided CSL style. The source examples
are reproduced, not independently verified. -->

```{=latex}
\begin{thebibliography}{00}

\bibitem{fuller1988}
J. F. Fuller, E. F. Fuchs, and K. J. Roesler, ``Influence of harmonics on power distribution system protection,'' \emph{IEEE Trans. Power Delivery}, vol. 3, pp. 549--557, Apr. 1988.

\bibitem{vidmar1992}
R. J. Vidmar, ``On the use of atmospheric plasmas as electromagnetic reflectors,'' \emph{IEEE Trans. Plasma Sci.}, vol. 21, no. 3, pp. 876--880, Aug. 1992. [Online]. Available: \url{http://www.halcyon.com/pub/journals/21ps03-vidmar}

\bibitem{clarke1950}
E. Clarke, \emph{Circuit Analysis of AC Power Systems}, vol. I. New York: Wiley, 1950, p. 81.

\bibitem{young1964}
G. O. Young, ``Synthetic structure of industrial plastics,'' in \emph{Plastics}, 2nd ed., vol. 3, J. Peters, Ed. New York: McGraw-Hill, 1964, pp. 15--64.

\bibitem{jones1991}
J. Jones, \emph{Networks}, 2nd ed., May 10, 1991. [Online]. Available: \url{http://www.atm.com}

\bibitem{reber1968}
E. E. Reber, R. L. Mitchell, and C. J. Carter, ``Oxygen absorption in the Earth's atmosphere,'' Aerospace Corp., Los Angeles, CA, Tech. Rep. TR-0200 (4230-46)-3, Nov. 1968.

\bibitem{talleen1996}
S. L. Talleen, ``The Intranet Architecture: Managing information in the new paradigm,'' Amdahl Corp., Sunnyvale, CA, Apr. 1996. [Online]. Available: \url{http://www.amdahl.com/doc/products/bsg/intra/infra/html}

\bibitem{ebehard1984}
D. Ebehard and E. Voges, ``Digital single sideband detection for interferometric sensors,'' unpublished, presented at the 2nd Int. Conf. Optical Fiber Sensors, Stuttgart, Germany, 1984.

\bibitem{process1996}
Process Corp., Framingham, MA, ``Intranets: Internet technologies deployed behind the firewall for corporate productivity,'' unpublished, presented at INET96 Annu. Meeting. [Online]. Available: \url{http://home.process.com/Intranets/wp2.htp}

\bibitem{lester2008}
G. N. Lester and J. H. Nelson, ``History of Circuit Breaker Standards,'' unpublished, presented at the IEEE/PES General Meeting, July 24, 2008. [Online]. Available: \url{http://www.ewh.ieee.org/soc/pes/switchgear/Presentations/2008CBtutorial/speaker1paper.pdf}

\bibitem{yorozu1987}
Y. Yorozu, M. Hirano, K. Oka, and Y. Tagawa, ``Electron spectroscopy studies on magneto-optical media and plastic substrate interface,'' \emph{IEEE Transl. J. Magn. Japan}, vol. 2, pp. 740--741, Aug. 1987 [Digests 9th Annu. Conf. Magnetics Japan, p. 301, 1982].

\bibitem{miller}
E. H. Miller, ``A note on reflector arrays,'' \emph{IEEE Trans. Antennas Propagat.}, in press.

\bibitem{alqueres1991}
J. L. Alqueres and J. C. Praca, ``The Brazilian power system and the challenge of the Amazon transmission,'' in \emph{Proc. 1991 IEEE Power Engineering Society Transmission and Distribution Conf.}, pp. 315--320.

\bibitem{hwang1997}
S. Hwang, ``Frequency domain system identification of helicopter rotor dynamics incorporating models with time periodic coefficients,'' Ph.D. dissertation, Dept. Aerosp. Eng., Univ. Maryland, College Park, 1997.

\bibitem{ieee1036}
\emph{IEEE Guide for Application of Shunt Power Capacitors}, IEEE Std. 1036-2010, Sept. 2010.

\bibitem{brandli1978}
G. Brandli and M. Dick, ``Alternating current fed power supply,'' U.S. Patent 4 084 217, Nov. 4, 1978.

\end{thebibliography}
```
