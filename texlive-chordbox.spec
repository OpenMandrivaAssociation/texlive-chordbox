Name:		texlive-chordbox
Version:	51000
Release:	2
Summary:	Draw chord diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chordbox
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chordbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chordbox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides two macros for drawing chord diagrams, as
may be found for example in chord charts/books and educational
materials. They are composed as TikZ pictures and have several
options to modify their appearance.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chordbox
%doc %{_texmfdistdir}/doc/latex/chordbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
