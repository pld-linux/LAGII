%define prefix /usr/local

Name: LAGII
Summary: Interprets and runs AGI games
Vendor: XoXus <xoxus@usa.net>
Version: 0.1.1
Release: 1
URL: http://www.zip.com.au/~gsymonds/LAGII/
Copyright: Freely distributable
Packager: XoXus <xoxus@usa.net>
Source: http://www.zip.com.au/~gsymonds/LAGII/LAGII-0.1.1.tar.gz
Group: Console/Games
Requires: svgalib

%description
LAGII interprets and runs AGI games under SVGALib. AGI games include most
of Sierra's classics, including Kings Quest, Space Quest and Police Quest.
You can also decompile the AGI LOGIC files and see how the game works.

%prep
%setup

%build
./configure --prefix=%prefix --with-no-giflib
make depend
make

%install
make install

%files
%{prefix}/bin/lagii
%{prefix}/bin/decomp

%doc doc/DRIVER-HOWTO
%doc doc/FAQ
%doc doc/README
