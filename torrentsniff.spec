%include	/usr/lib/rpm/macros.perl
Summary:	Reports on the status of the torrent
Summary(pl.UTF-8):	Raportowanie o stanie potoku BitTorrenta
Name:		torrentsniff
Version:	0.3.0
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://www.highprogrammer.com/alan/perl/%{name}-%{version}.tar.gz
# Source0-md5:	3884cac276a990a95ea77738195508aa
URL:		http://www.highprogrammer.com/alan/perl/torrentsniff.html
BuildRequires:	perl-Digest-SHA1
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TorrentSniff is a command line Perl program that reads a BitTorrent
.torrent file from the local file system or from a URL and reports on
the status of the torrent.

%description -l pl.UTF-8
TorrentSniff to perlowy program działający z linii poleceń, który
odczytuje plik .torrent z lokalnego systemu plików lub URL-a i
raportuje stan potoku.
 
%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}/BitTorrent}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install BitTorrent/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/BitTorrent

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/BitTorrent
