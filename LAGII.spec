Summary:	Interprets and runs AGI games
Summary(pl):	Interpretuje i uruchamia gry AGI
Name:		LAGII
Version:	0.1.5
Release:	2
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Vendor:		XoXus <xoxus@usa.net>
License:	Freely distributable
Source0:	http://www.zip.com.au/~gsymonds/LAGII/%{name}-%{version}.tar.bz2
URL:		http://www.zip.com.au/~gsymonds/LAGII/
Requires:	svgalib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAGII interprets and runs AGI games under SVGALib. AGI games include
most of Sierra's classics, including Kings Quest, Space Quest and
Police Quest. You can also decompile the AGI LOGIC files and see how
the game works.

%description -l pl
LAGII interpretuje i uruchamia gry AGI pod SVGALib. Gry AGI zawieraj±
wiêkszo¶æ klasycznych gier Sierray w³±czaj±c Kings Quest, Space Quest
i Police Quest. Mo¿esz tak¿e zdekompilowaæ pliki AGI LOGIC i zobaczyæ
jak dzia³a dana gra.

%prep
%setup -q

%build
%configure2_13 \
	--with-no-giflib
%{__make} depend
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/lagii decomp/decomp $RPM_BUILD_ROOT%{_bindir}

gzip -9nf doc/DRIVER-HOWTO doc/FAQ doc/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{DRIVER-HOWTO,FAQ,README}.gz
%attr(755,root,root) %{_bindir}/lagii
%attr(755,root,root) %{_bindir}/decomp
