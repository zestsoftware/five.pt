import Globals

from Products.CMFCore.FSObject import FSObject
from Products.CMFCore import DirectoryView
from Products.CMFCore import permissions

from Products.CMFFormController.BaseControllerPageTemplate import \
     BaseControllerPageTemplate as BaseCPT
from Products.CMFFormController.FSControllerBase import FSControllerBase

from Shared.DC.Scripts.Script import Script
from AccessControl import ClassSecurityInfo
from RestrictedPython import Utilities

from pagetemplate import PageTemplateFile
from pagetemplate import FiveTemplateFile
from pagetemplate import EContext

_marker = object()

class CMFTemplateFile(FiveTemplateFile):
    @property
    def utility_builtins(self):
        builtins = dict(
            econtext=EContext())
        builtins.update(        
            Utilities.utility_builtins)
        return builtins

class CMFPageTemplateFile(PageTemplateFile):
    template_class = CMFTemplateFile
    
class FSPageTemplate(FSObject, Script):
    meta_type = 'Filesystem Page Template'
    
    security = ClassSecurityInfo()
    security.declareObjectProtected(permissions.View)

    _default_bindings = {'name_subpath': 'traverse_subpath'}
    
    template = None
    
    def __init__(self, id, filepath, fullname=None, properties=None):
        FSObject.__init__(self, id, filepath, fullname, properties)
        self.ZBindings_edit(self._default_bindings)

        # instantiate page template
        self.template = CMFPageTemplateFile(filepath)
        
    def _readFile(self, reparse):
        # templates are lazy
        if reparse:
            self.template.read()

    def __call__(self, *args, **kwargs):
        kwargs['args'] = args
        return self.template(self, **kwargs)

    @property
    def macros(self):
        return self.template.macros

class FSControllerPageTemplate(FSControllerBase, FSPageTemplate, BaseCPT):
    def __init__(self, id, filepath, fullname=None, properties=None):
        FSPageTemplate.__init__(self, id, filepath, fullname, properties)  
        self.filepath = filepath
      
        self._read_action_metadata(self.getId(), filepath)
        self._read_validator_metadata(self.getId(), filepath)

    def _readFile(self, reparse):
        FSPageTemplate._readFile(self, reparse)
        self._readMetadata()

    def _updateFromFS(self):
        # workaround for Python 2.1 multiple inheritance lameness
        return self._baseUpdateFromFS()

    def _readMetadata(self):
        # workaround for Python 2.1 multiple inheritance lameness
        return self._baseReadMetadata()

    def __call__(self, *args, **kwargs):
        return self._call(FSPageTemplate.__call__, *args, **kwargs)

Globals.InitializeClass(FSPageTemplate)
Globals.InitializeClass(FSControllerPageTemplate)

DirectoryView.registerFileExtension('pt', FSPageTemplate)
DirectoryView.registerFileExtension('zpt', FSPageTemplate)
DirectoryView.registerFileExtension('html', FSPageTemplate)
DirectoryView.registerFileExtension('htm', FSPageTemplate)
DirectoryView.registerFileExtension('cpt', FSControllerPageTemplate)

DirectoryView.registerMetaType('Page Template', FSPageTemplate)
DirectoryView.registerMetaType('Controller Page Template', FSControllerPageTemplate)
