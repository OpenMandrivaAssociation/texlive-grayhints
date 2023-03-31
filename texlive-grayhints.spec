Name:		texlive-grayhints
Version:	49052
Release:	2
Summary:	Produce 'gray hints' to a variable text field
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/grayhints
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grayhints.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grayhints.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grayhints.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides JavaScript code snippets to create 'gray
hints'. Gray hints, as the author terms them, are text that
appears initially in a text field that gives a short hint as to
what the contents of the text field should be. For example, a
text field might contain the hint 'First Name', or a date field
might read 'yyyy/mm/dd'. As soon as the field comes into focus,
the hint disappears. It reappears when the field is blurred and
the user did not enter any text into the field. The package
works for dvips/Distiller, pdfLaTeX, LuaLaTeX, and XeLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/grayhints
%{_texmfdistdir}/tex/latex/grayhints
%doc %{_texmfdistdir}/doc/latex/grayhints

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
