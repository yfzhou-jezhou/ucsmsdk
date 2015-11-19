"""This module contains the general information for CommSnmpTrap ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CommSnmpTrapConsts():
    NOTIFICATION_TYPE_INFORMS = "informs"
    NOTIFICATION_TYPE_TRAPS = "traps"
    V3_PRIVILEGE_AUTH = "auth"
    V3_PRIVILEGE_NOAUTH = "noauth"
    V3_PRIVILEGE_PRIV = "priv"
    VERSION_V1 = "v1"
    VERSION_V2C = "v2c"
    VERSION_V3 = "v3"


class CommSnmpTrap(ManagedObject):
    """This is CommSnmpTrap class."""

    consts = CommSnmpTrapConsts()
    naming_props = set([u'hostname'])

    mo_meta = MoMeta("CommSnmpTrap", "commSnmpTrap", "snmp-trap[hostname]", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["aaa", "admin"], [u'commSnmp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "community": MoPropertyMeta("community", "community", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[!#$%\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,32}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "hostname": MoPropertyMeta("hostname", "hostname", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8L, None, None, """^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7}|:)$""", [], []), 
        "notification_type": MoPropertyMeta("notification_type", "notificationType", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["informs", "traps"], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["1-65535"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "v3_privilege": MoPropertyMeta("v3_privilege", "v3Privilege", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["auth", "noauth", "priv"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version111j, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["v1", "v2c", "v3"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "community": "community", 
        "dn": "dn", 
        "hostname": "hostname", 
        "notificationType": "notification_type", 
        "port": "port", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "v3Privilege": "v3_privilege", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, hostname, **kwargs):
        self._dirty_mask = 0
        self.hostname = hostname
        self.child_action = None
        self.community = None
        self.notification_type = None
        self.port = None
        self.sacl = None
        self.status = None
        self.v3_privilege = None
        self.version = None

        ManagedObject.__init__(self, "CommSnmpTrap", parent_mo_or_dn, **kwargs)
