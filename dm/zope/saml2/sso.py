# Copyright (C) 2011-2012 by Dr. Dieter Maurer <dieter@handshake.de>
"""Common base implementation for SSO support."""

from dm.zope.saml2.role import Role

class Sso(Role):
  """mixin class to provide common SSO services.
  """
