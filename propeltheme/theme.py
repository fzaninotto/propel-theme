# Created by Noah Kantrowitz on 2007-07-16.
# Copyright (c) 2007 Noah Kantrowitz. All rights reserved.

from trac.core import *

from themeengine.api import ThemeBase

class PropelTheme(ThemeBase):
    """Trac Theme for Propel ORM."""

    template = htdocs = css = screenshot = True
    
