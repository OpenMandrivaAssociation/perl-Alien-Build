%define upstream_name    Alien-Build
%define upstream_version 1.78

%global __requires_exclude ^perl(Alien::xz)$
%global __requires_exclude ^perl(FFI::Platypus)$

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2
Summary:    Build external dependencies for use in CPAN
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture::Tiny) >= 0.170.0
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.640.0
BuildRequires: perl(ExtUtils::ParseXS) >= 3.300.0
BuildRequires: perl(FFI::CheckLib) >= 0.110.0
BuildRequires: perl(File::Which) >= 1.100.0
BuildRequires: perl(File::chdir)
BuildRequires: perl(JSON::PP)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Path::Tiny) >= 0.77.0
BuildRequires: perl(Test2::API) >= 1.302.15
#BuildRequires: perl(Test2::Mock) >= 0.0.60
#BuildRequires: perl(Test2::Require) >= 0.0.60
#BuildRequires: perl(Test2::Require::Module) >= 0.0.60
#BuildRequires: perl(Test2::V0) >= 0.0.60
BuildRequires: perl(Text::ParseWords) >= 3.260.0
BuildRequires: perl-devel
BuildArch:  noarch

%description
This module provides tools for building external (non-CPAN) dependencies for
CPAN. It is mainly designed to be used at install time of a CPAN client, and
work closely with Alien::Base which is used at runtime.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%perl_vendorlib/Test/Alien.pm
%perl_vendorlib/Test/Alien
