from dm.zope.saml2.interfaces import ISamlUserAuthenticated
from zope.interface import implementer
from zope.component.interfaces import ObjectEvent


@implementer(ISamlUserAuthenticated)
class SamlUserAuthenticated(ObjectEvent):
    """
    SAML user got authenticated
    :param user_id: id of authenticated user
    """
