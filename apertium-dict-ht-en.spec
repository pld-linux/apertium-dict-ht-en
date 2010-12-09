Summary:	Haitian-English language pair for Apertium
Summary(pl.UTF-8):	Para języków haitański-angielski dla Apertium
%define	lpair	ht-en
Name:		apertium-dict-%{lpair}
Version:	0.1.0
Release:	1
License:	GPL v3
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	73d6dbbb2c1ad50b8e6c5428f4fc7a9e
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Haitian and English, morphological analysis or part-of-speech
tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między haitańskim a angielskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed here (see modes subdir) and contain wrong (builddir) paths
%{__rm} $RPM_BUILD_ROOT%{_datadir}/apertium/apertium-%{lpair}/*.mode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/ht-en.mode
