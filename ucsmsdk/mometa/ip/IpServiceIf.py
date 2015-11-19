"""This module contains the general information for IpServiceIf ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class IpServiceIfConsts():
    PREF_ALTERNATE = "alternate"
    PREF_PREFERRED = "preferred"


class IpServiceIf(ManagedObject):
    """This is IpServiceIf class."""

    consts = IpServiceIfConsts()
    naming_props = set([u'addr', u'port'])

    mo_meta = MoMeta("IpServiceIf", "ipServiceIf", "serv-ip-[addr]-port-[port]", VersionMeta.Version211a, "InputOutput", 0x7fL, [], ["admin"], [u'storageEtherIf'], [], [None])

    prop_meta = {
        "addr": MoPropertyMeta("addr", "addr", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x1L, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "port": MoPropertyMeta("port", "port", "uint", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], ["1-65535"]), 
        "pref": MoPropertyMeta("pref", "pref", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["alternate", "preferred"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, """((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "addr": "addr", 
        "childAction": "child_action", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "port": "port", 
        "pref": "pref", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "subnet": "subnet", 
    }

    def __init__(self, parent_mo_or_dn, addr, port, **kwargs):
        self._dirty_mask = 0
        self.addr = addr
        self.port = port
        self.child_action = None
        self.def_gw = None
        self.pref = None
        self.sacl = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "IpServiceIf", parent_mo_or_dn, **kwargs)
