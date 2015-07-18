Changelog
=========

2.2.3 (2015-07-18)
~~~~~~~~~~~~~~~~~~

- Add version to setup.py to make zest.releaser happy.
  [timo]

- Compatibility with Chameleon >= 2.14
  [tomgross]


2.2.2 (2014-04-15)
~~~~~~~~~~~~~~~~~~

- Fix test.
  [davisagli]


2.2.1 (2012-01-08)
~~~~~~~~~~~~~~~~~~

Features:

- Whitespace between attributes is now reduced to a single whitespace
  character.

Bugfixes:

- The path traverser now correctly renders callables, applying the
  template namespace as keyword arguments. Previously, only the
  ``request`` name would be passed.

- The content provider expression now correctly applies TAL namespace
  data.

- Avoid duplicate HTML decoding. This fixes an issue which was
  introduced because newer Chameleon releases decode all expression
  inputs by default.

2.2.0 (2011-10-10)
~~~~~~~~~~~~~~~~~~

- Update implementation to use component-based template engine
  configuration, plugging directly into the Zope Toolkit framework.

- Declare RepeatItem as public object with allowed subobjects
  [leorochael]

- Bump minimum versions of dependencies z3c.pt and sourcecodegen to fix
  lp#853731 and lp#848200.
  [leorochael]

- Fixed encoding issue with restricted Python expression. The Python
  2.4 AST parser does not accept unicode input and the expression
  string must be explicitly encoded to a byte string.
  [malthe]

2.1.5 (2011-08-11)
~~~~~~~~~~~~~~~~~~

- Reuse template instance on cook.
  [malthe]

- Use the template source string available in the ``_text`` attribute
  instead of reading the file (again).
  [leorochael, malthe]

- Use secure moduler importer for both Zope 2 and 3 templates. This
  fixes issue #34.
  [malthe]

2.1.4 (2011-07-28)
~~~~~~~~~~~~~~~~~~

- Upgrade to newest Zope integration package.

2.1.3 (2011-07-23)
~~~~~~~~~~~~~~~~~~

- Fixed issue with traversal and dictionary optimization (the
  optimization has been removed).
  [malthe]

- Fixed compatibility issue with the ``UnauthorizedBinding`` class and
  traversal.
  [malthe]

2.1.2 (2011-07-21)
~~~~~~~~~~~~~~~~~~

- Wire in restricted python builtins as imports. Previously these were
  added to the dynamic context.
  [malthe]

- Use the Python expression from the ``z3c.pt`` package for the
  trusted page template engine. This difference between this and the
  standard Python expression from Chameleon is that the pipe character
  (``"|"``) has the meaning of fallback in Chameleon, but not in the
  reference ZPT implementation (where it's only available for path
  expressions).
  [malthe]

2.1.1 (2011-07-15)
~~~~~~~~~~~~~~~~~~

- Added builtins from ``RestrictedPython`` to context for Zope 2
  templates.

  This fixes name error issues on templates that use one or more
  utility function builtins normally available to Python expressions
  in restricted mode.
  [malthe]

2.1 (2011-07-14)
~~~~~~~~~~~~~~~~

- Point release.

- Use trusted path expression for trusted expression engine.
  [malthe]

- Fixed template context issues where a ``request`` would be required
  by the path expression compiler but not provided (typically when in
  a situation where the user is unauthorized to view content).
  [malthe]

2.1-rc1 (2011-07-14)
~~~~~~~~~~~~~~~~~~~~

- Major architectural change.

  The package no longer contains own template classes; instead,
  patches are made to switch from the reference TAL interpreter to the
  Chameleon TAL compiler.
  [malthe]

2.0-rc3 (2011-07-07)
~~~~~~~~~~~~~~~~~~~~

- Refactor custom Python expression implementation to use the
  ``parse`` method. This builds directly on the base implementation
  and its behavior.
  [malthe]

2.0-rc2 (2011-05-24)
~~~~~~~~~~~~~~~~~~~~

- Have the base template class implement ``IPageTemplate`` from
  ``zope.pagetemplate``. This interface is relied on for a number of
  adapter registrations and the missing interface declaration affects
  packages such as ``plone.caching``.
  [malthe]

- Set default reload mode to the Zope 2 application server
  configuration's ``debug_mode`` value.
  [malthe]

2.0-rc1 (2011-02-28)
~~~~~~~~~~~~~~~~~~~~

- Update to Chameleon 2.0.

  This release includes many changes and is a complete rewrite of the
  1.x series.

  Note that Python 2.5+ is now required.
  [malthe]

- Python-expressions are now subject to access-control security.
  [malthe]

1.3.3 - 2010-09-30
~~~~~~~~~~~~~~~~~~

- Apply patches at import time instead of product initialisation.
  [wichert]

1.3.2 - 2010-09-29
~~~~~~~~~~~~~~~~~~

- Add a same_type method to the default namespace.
  [wichert]

1.3.1 - 2010-09-23
~~~~~~~~~~~~~~~~~~

- Added support for eager loading (environment variable
  ``CHAMELEON_EAGER``). This flag should be passed only in development
  mode and will reveal any templates which do not parse.
  [malthe]

1.3 - 2010-09-08
~~~~~~~~~~~~~~~~

- Added support for ``PageTemplate`` and
  ``ZopePageTemplate``.
  [malthe]

1.2 - 2010-08-30
~~~~~~~~~~~~~~~~

- Fixed acquisition-wrapping issue: we need to wrap with the parent to
  avoid a pair of template objects (original and patched).

1.1 - 2010-05-15
~~~~~~~~~~~~~~~~~

- Add DateTime to the base context. Fixes problems with certain ZMI pages.
  [wichert]

1.0 - 2010-05-13
~~~~~~~~~~~~~~~~~

- If template is not an acquirer, wrap it implicitly. [malthe]

- Removed unused ``ViewletManager`` ZCML handler. [malthe]

0.10 - 2010-04-20
~~~~~~~~~~~~~~~~~

- Improve five.grok support [fretin]

- Check if templates are acquisition-aware before trying to wrap them. This
  fixes problems with METAL macros in some ZMI pages. [wichert]

0.9 - 2010-04-14
~~~~~~~~~~~~~~~~

- Basic support for five.grok templates. [wichert]

0.8 - 2010-01-05
~~~~~~~~~~~~~~~~

- Fixed some calling convention oddity that would result in the view
  instance being passed doubly as the template arguments.

0.7 - 2009-05-20
~~~~~~~~~~~~~~~~

- Default encoding of the base template set to UTF-8. [malthe]

- Update to latest Chameleon. [malthe]

- Patch ``macros`` attribute. [malthe]

0.6 - 2009-04-06
~~~~~~~~~~~~~~~~

- Avoid another case of unconditionally attempting to Acquisition wrap
  template files. We do have an interface check for this. [hannosch]

0.5 - 2009-02-17
~~~~~~~~~~~~~~~~

- Added test function to template context. [malthe]

- Fixed edge-case (special case?) where the view of a
  ViewPageTemplateFile is really only the view for a view. [malthe]

- Added patch for ``Products.PageTemplates.PageTemplateFile``. [malthe]

- Rework the "full namespace provided to path expression" change introduced
  in 0.3. We no longer call the expensive locals() function but construct a
  minimal namespace with the context and request ourselves. [hannosch]

- If the ``__get__`` method is called uninstantiated, just return the
  class itself. [malthe]

five.pt 0.4 (released 2/13/2009)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Fixed issue where the ``template`` parameter to a viewlet manager
  directive was effectively ignored. [malthe]

- Fixed acquisition-wrapping issue with the (patched) bound template
  class (could cause infinite loop due to cyclic acquisition
  chain). [malthe]

- Moved evaluate_path and evaluate_exists over to ``z3c.pt``, adding
  support for global ``path()`` and ``exists()`` functions for use in
  ``python:`` expressions to it (LP #317967). [sidnei]

five.pt 0.3 (released 12/17/2008)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Use bobo traversal if ``OFS.interfaces.ITraversable`` interface is
  provided. [malthe]

- Adjusted the path expression to provide the full namespace to the render
  function and not just the request. This matches Zope2 behavior. [hannosch]

five.pt 0.2 (released 11/29/2008)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- From Zope 2.12 onwards, do not acquisition-wrap content
  provider. [malthe]

- Split out CMF-related code to separate package. [malthe]

- Compatibility changes to support Zope 2.10. [malthe]

five.pt 0.1 (released 11/19/2008)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Initial release.

- Simplified template class inheritance. [malthe]

- Added ``path`` and ``exists`` functions to skin template
  namespace. [malthe]

- Added call-support for old-style classes in path
  expressions. [malthe]

- Added monkey-patches to replace template engine for module-level
  view page template instances. [malthe]

- Made `EContext` class more robust. [malthe]

- Register custom file-system page template class for use with CMF
  form controllers. [malthe]

- Register custom file-system page template class for use with CMF
  directory views. [malthe]

- Added meta-directives to register browser views, viewlets and
  viewlet managers using Chameleon templates. [malthe]

- Updated to latest API. [malthe]

- Package structure. [hannosch]
