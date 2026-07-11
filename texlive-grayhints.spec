%global tl_name grayhints
%global tl_revision 49052

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Produce gray hints to a variable text field
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grayhints
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grayhints.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grayhints.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grayhints.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides JavaScript code snippets to create 'gray hints'.
Gray hints, as the author terms them, are text that appears initially in
a text field that gives a short hint as to what the contents of the text
field should be. For example, a text field might contain the hint 'First
Name', or a date field might read 'yyyy/mm/dd'. As soon as the field
comes into focus, the hint disappears. It reappears when the field is
blurred and the user did not enter any text into the field. The package
works for dvips/Distiller, pdfLaTeX, LuaLaTeX, and XeLaTeX.

