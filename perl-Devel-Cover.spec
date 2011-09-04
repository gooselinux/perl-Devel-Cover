Name:           perl-Devel-Cover
Version:        0.65
Release:        1%{?dist}
Summary:        Code coverage metrics for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Devel-Cover/
Source0:        http://www.cpan.org/authors/id/P/PJ/PJCJ/Devel-Cover-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(Template)
BuildRequires:  perl(PPI::HTML) >= 1.07
BuildRequires:  perl(Perl::Tidy) >= 20060719
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Pod::Coverage)
Requires:       perl(Test::Differences)
# Optional modules
# Requires:       perl(PPI::HTML) >= 1.07
# Requires:       perl(Perl::Tidy) >= 20060719


%description
This module provides code coverage metrics for Perl.


%prep
%setup -q -n Devel-Cover-%{version}
chmod -c a-x buildperl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc BUGS CHANGES README TODO all_versions buildperl cpancover create_gold session.vim
%{_bindir}/*
%{perl_vendorarch}/Devel/
%{perl_vendorarch}/auto/Devel/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog
* Thu Jan 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.65-1
- update to 0.65

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.64-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.64-1
- update to 0.64

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-3
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.63-2
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-1
- 0.63

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.61-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Jan 11 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.61-1
- Update to 0.61.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.60-1
- Update to 0.60.

* Wed Sep  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.59-1
- Update to 0.59.
- Dropped PPI::HTML from the requirements list (optional module).

* Wed Aug  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.58-1
- Update to 0.58.

* Fri Aug  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.57-1
- Update to 0.57.

* Thu Aug  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.56-1
- Update to 0.56.

* Fri May 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.55-2
- Removed dependencies pulled in by a documentation file (#191110).

* Thu May 04 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.55-1
- First build.
