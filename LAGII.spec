Name:		LAGII
Summary:	Interprets and runs AGI games
Summary(pl):	Interpretuje i uruchamia gry AGI
Version:	0.1.1
Release:	1
Group:		Console/Games
Vendor:		XoXus <xoxus@usa.net>
Copyright:	Freely distributable
Source:		http://www.zip.com.au/~gsymonds/LAGII/LAGII-0.1.1.tar.bz2
URL:		http://www.zip.com.au/~gsymonds/LAGII/
Requires:	svgalib
BuildRoot:	/tmp/%{name}-%{version}-root

%description
LAGII interprets and runs AGI games under SVGALib. AGI games include most
of Sierra's classics, including Kings Quest, Space Quest and Police Quest.
You can also decompile the AGI LOGIC files and see how the game works.

%description -l pl
LAGII interpretuje i uruchamia gry AGI pod SVGALib. Gry AGI zawieraj�
wi�kszo�� klasycznych gier Sierray w��czaj�c Kings Quest, Space Quest 
i Police Quest. Mo�esz tak�e zdekompilowa� pliki AGI LOGIC i zobaczy�
jak dzia�a dana gra.

%prep
%setup -q

%build
%configure \
	--with-no-giflib
make depend
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s src/lagii $RPM_BUILD_ROOT%{_bindir}/
install -s decomp/decomp $RPM_BUILD_ROOT%{_bindir}/

gzip -9nf doc/DRIVER-HOWTO doc/FAQ doc/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{DRIVER-HOWTO,FAQ,README}.gz
%{_bindir}/lagii
%{_bindir}/decomp
