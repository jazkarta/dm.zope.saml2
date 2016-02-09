from dm.zope.saml2.interfaces import ISamlUserAuthenticated
from zope.interface import implements
from zope.component.interfaces import ObjectEvent


class SamlUserAuthenticated(ObjectEvent):
    """
    SAML user got authenticated
    :param user_id: id of authenticated user
    """
    implements(ISamlUserAuthenticated)
