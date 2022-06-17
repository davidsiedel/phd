---
documentclass: book
title: "My thesis."
author: David Siedel
date: December 2022
lang: en-EN
geometry:
  - margin=2cm
papersize: a4
numbersections: true
link-citations: true
colorlinks: true
figPrefixTemplate: "$$i$$"
tblPrefixTemplate: "$$i$$"
secPrefixTemplate: "$$i$$"
eqnPrefixTemplate: "($$i$$)"
bibliography: bibliography.bib
csl: iso690-numeric-en.csl
header-includes:
- \newcommand\hmmax{0}
- \newcommand\bmmax{0}
- \usepackage[bbgreekl]{mathbbol}
- \usepackage[eulergreek]{sansmath}
- \usepackage{stmaryrd}
- \usepackage{notations}
- \usepackage{lmodern}
- \usepackage{psl-cover}
- \pslassetspath{img}
- \usepackage{amsmath}
- \usepackage{amsfonts}
- \usepackage{amssymb}
- \usepackage{graphicx}
- \usepackage{siunitx}
- \usepackage{physics}
- \sisetup{math-micro=\text{µ},text-micro=µ}
- \usepackage[euler]{textgreek}
- \usepackage{booktabs}
- \usepackage{soul}
- \usepackage{enumitem}
- \usepackage{bm}
- \usepackage{tcolorbox}
- \newtcolorbox{myquote}{colback=gray!5!white, colframe=gray!75!black}
- \renewenvironment{quote}{\begin{myquote}}{\end{myquote}}
- \institute{MINES ParisTech}
- \doctoralschool{Ingénierie des Systèmes, Matériaux, Mécanique, Energétique}{621}
- \specialty{Voir spécialités ED}
- \jurymember{1}{Prénom NOM}{Titre, établissement}{Président}
- \jurymember{2}{Prénom NOM}{Titre, établissement}{Rapporteur}
- \jurymember{3}{Prénom NOM}{Titre, établissement}{Rapporteur}
- \jurymember{4}{Prénom NOM}{Titre, établissement}{Examinateur}
- \jurymember{5}{Prénom NOM}{Titre, établissement}{Examinateur}
- \jurymember{6}{Prénom NOM}{Titre, établissement}{Examinateur}
- \jurymember{7}{Prénom NOM}{Titre, établissement}{Examinateur}
- \jurymember{8}{Alain THIONNET}{Titre, établissement}{Directeur de thèse}
---

<!--
pandoc -f markdown+tex_math_single_backslash -F pandoc-crossref --citeproc --highlight-style=tango report.md chapters/notations.md chapters/introduction.md chapters/part1.md chapters/industrial-context.md chapters/volumetric-locking.md chapters/phase-field.md chapters/part2.md chapters/hho.md chapters/part3.md chapters/micromorphic-damage.md chapters/micromorphic-damage-fem.md chapters/micromorphic-damage-hho.md chapters/part4.md  chapters/conclusions.md chapters/appendices.md chapters/hho-implementation.md chapters/references.md -o report.pdf
-->

\newcommand{\dtot}{\mathrm{d}}
\newcommand{\absvalue}[1]{{\left|#1\right|}}
\newcommand{\paren}[1]{{\left(#1\right)}}
\newcommand{\tensor}[1]{{\underset{\tilde{}}{\mathbf{#1}}}}
\newcommand{\stensor}[1]{\underline{#1}}
\newcommand{\fotensor}[1]{\underline{\underline{\mathbf{#1}}}}
\newcommand{\tenseurq}[1]{\underline{\underline{\mathbf{#1}}}}
\newcommand{\tenseur}[1]{\underline{#1}}
\newcommand{\tepsilon}{\underline{\epsilon}}
\newcommand{\tepsilonto}{\stensor{\varepsilon}^{\mathrm{to}}}
\newcommand{\tepsilonel}{\stensor{\varepsilon}^{\mathrm{el}}}
\newcommand{\tepsilonvis}{\stensor{\varepsilon}^{\mathrm{vis}}}
\newcommand{\tdepsilonvis}{\stensor{\dot{\varepsilon}}^{\mathrm{vis}}}
\newcommand{\tepsilonp}{\stensor{\varepsilon}^{\mathrm{p}}}
\newcommand{\tdepsilonp}{\stensor{\dot{\varepsilon}}^{\mathrm{p}}}
\newcommand{\tsigma}{\underline{\sigma}}
\newcommand{\tepsilonth}{\underline{\epsilon}^{\mathrm{th}}}
\renewcommand{\trace}[1]{{\mathrm{tr}\paren{#1}}}
\newcommand{\sigmaH}{\sigma_{H}}
\newcommand{\Frac}[2]{{{\displaystyle \frac{\displaystyle #1}{\displaystyle #2}}}}
\newcommand{\deriv}[2]{{\displaystyle \frac{\displaystyle \partial #1}{\displaystyle \partial #2}}}
\newcommand{\derivtot}[2]{{\displaystyle \frac{\displaystyle \mathrm{d}#1}{\displaystyle \mathrm{d} #2}}}
\newcommand{\argmin}{\mathrm{argmin}}
\newcommand{\bts}[1]{\left.#1\right|_{t}}
\newcommand{\mts}[1]{\left.#1\right|_{t+\theta\,\Delta\,t}}
\newcommand{\ets}[1]{\left.#1\right|_{t+\Delta\,t}}
\newcommand{\iter}[2]{\left.#2\right|^{\left(#1\right)}}
\newcommand{\sigmaeq}{\sigma_{\mathrm{eq}}}
\newcommand{\dev}{\operatorname{dev}}
\newcommand{\ppart}[1]{\langle #1 \rangle_{+}}
\newcommand{\npart}[1]{\langle #1 \rangle_{-}}
\newcommand{\freeenergy}{\psi}
\newcommand{\freeenergyel}{{\psi}^{el}}
\newcommand{\freeenergyd}{{\psi}^{d}}
\newcommand{\freeenergyddchi}{{\psi}^{d, d_{\chi}}}
\newcommand{\freeenergygdchi}{{\psi}^{\vnabla\,d_{\chi}}}
\newcommand{\dissipationpotential}{\phi}
\newcommand{\dissipationpotentialdual}{\phi^{\star}}

\tableofcontents
\listoffigures

\input{abstract}

