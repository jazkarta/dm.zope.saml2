# Copyright (C) 2011-2012 by Dr. Dieter Maurer <dieter@handshake.de>
"""SAML2 support."""

def initialize(context):
  from dm.zope.saml2.authority import SamlAuthority
  from dm.zope.saml2.permission import manage_saml
  from dm.zope.schema.z2.constructor import add_form_factory, SchemaConfiguredZmiAddForm

  context.registerClass(
    SamlAuthority,
    constructors=(add_form_factory(SamlAuthority, form_class=SchemaConfiguredZmiAddForm),),
    permission=manage_saml,
    )

  from dm.zope.saml2.idpsso.idpsso import initialize; initialize(context)
  from dm.zope.saml2.spsso import initialize; initialize(context)
  from dm.zope.saml2.entity import initialize; initialize(context)
