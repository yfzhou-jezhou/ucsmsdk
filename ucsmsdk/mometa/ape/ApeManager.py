"""This module contains the general information for ApeManager ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeManagerConsts():
    pass


class ApeManager(ManagedObject):
    """This is ApeManager class."""

    consts = ApeManagerConsts()
    naming_props = set([])

    mo_meta = MoMeta("ApeManager", "apeManager", "ape", VersionMeta.Version101e, "InputOutput", 0xfL, [], ["read-only"], [u'topRoot'], [u'apeControllerManager', u'apeDcosAgManager', u'apeHostAgent', u'apeLANBoot', u'apeLocalDiskBoot', u'apeMc', u'apeNicAgManager', u'apeSANBoot', u'apeVirtualMediaBoot'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stats_update_id": MoPropertyMeta("stats_update_id", "statsUpdateId", "uint", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "statsUpdateId": "stats_update_id", 
        "status": "status", 
    }

    def __init__(self, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.stats_update_id = None
        self.status = None

        ManagedObject.__init__(self, "ApeManager", **kwargs)
