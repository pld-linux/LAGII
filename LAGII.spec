Name:		LAGII
Summary:	Interprets and runs AGI games
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
