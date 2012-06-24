Name:		LAGII
Summary:	Interprets and runs AGI games
Summary(pl):	Interpretuje i uruchamia gry AGI
Version:	0.1.1
Release:	1
Group:		Console/Games
Vendor:		XoXus <xoxus@usa.net>
Copyright:	Freely distributable
Source:		http://www.zip.com.au/~gsymonds/LAGII/LAGII-0.1.1.tar.gz
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
%setup

%build
./configure \
	--prefix=%prefix \
	--with-no-giflib
make depend
make

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{prefix}/bin/lagii
%{prefix}/bin/decomp

%doc doc/DRIVER-HOWTO
%doc doc/FAQ
%doc doc/README
