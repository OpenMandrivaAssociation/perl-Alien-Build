%define upstream_name    Alien-Build

#global __requires_exclude ^perl(Alien::xz)$
#global __requires_exclude ^perl(FFI::Platypus)$
%global __requires_exclude perl\\((Alien::xz|FFI::Platypus)\\)

%{?perl_default_filter}

Name:		perl-%{upstream_name}
Version:	2.84
Release:	2
Summary:    Build external dependencies for use in CPAN
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(FFI::CheckLib)
BuildRequires: perl(File::Which)
BuildRequires: perl(File::chdir)
BuildRequires: perl(JSON::PP)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Test2::API)
#BuildRequires: perl(Test2::Mock)
#BuildRequires: perl(Test2::Require)
#BuildRequires: perl(Test2::Require::Module)
#BuildRequires: perl(Test2::V0)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl-devel
BuildArch:  noarch

%description
This module provides tools for building external (non-CPAN) dependencies for
CPAN. It is mainly designed to be used at install time of a CPAN client, and
work closely with Alien::Base which is used at runtime.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%doc Changes INSTALL LICENSE META.json META.yml README SUPPORT example
%{_mandir}/man3/*
%perl_vendorlib/alienfile.pm
%perl_vendorlib/Alien/Build
%perl_vendorlib/Alien/Build.pm
%perl_vendorlib/Alien/Base
%perl_vendorlib/Alien/Base.pm
%perl_vendorlib/Alien/Role.pm
%perl_vendorlib/Alien/Util.pm
%perl_vendorlib/Test/Alien.pm
%perl_vendorlib/Test/Alien
