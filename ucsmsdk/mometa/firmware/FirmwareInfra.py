"""This module contains the general information for FirmwareInfra ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FirmwareInfraConsts():
    ADMIN_STATE_TRIGGER = "trigger"
    ADMIN_STATE_TRIGGER_IMMEDIATE = "trigger-immediate"
    ADMIN_STATE_TRIGGERED = "triggered"
    ADMIN_STATE_UNTRIGGERED = "untriggered"
    ADMIN_STATE_USER_ACK = "user-ack"
    ADMIN_STATE_USER_DISCARD = "user-discard"
    AUTO_DELETE_FALSE = "false"
    AUTO_DELETE_NO = "no"
    AUTO_DELETE_TRUE = "true"
    AUTO_DELETE_YES = "yes"
    IGNORE_CAP_FALSE = "false"
    IGNORE_CAP_NO = "no"
    IGNORE_CAP_TRUE = "true"
    IGNORE_CAP_YES = "yes"
    INT_ID_NONE = "none"
    OPER_STATE_ACTIVE = "active"
    OPER_STATE_APPLIED = "applied"
    OPER_STATE_APPLY_PENDING = "apply-pending"
    OPER_STATE_EVALUATED = "evaluated"
    OPER_STATE_EVALUATION_PENDING = "evaluation-pending"
    OPER_STATE_EXPIRED = "expired"
    OPER_STATE_NONE = "none"
    OPER_STATE_PENDING = "pending"
    OPER_STATE_UNTRIGGERED = "untriggered"
    OPER_STATE_WAITING_FOR_DEPENDENCY = "waiting-for-dependency"
    OPER_STATE_WAITING_FOR_MAINT_WINDOW = "waiting-for-maint-window"
    OPER_STATE_WAITING_FOR_USER = "waiting-for-user"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class FirmwareInfra(ManagedObject):
    """This is FirmwareInfra class."""

    consts = FirmwareInfraConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareInfra", "firmwareInfra", "fw-infra", VersionMeta.Version211a, "InputOutput", 0x3ffL, [], ["admin"], [u'firmwareSystem'], [u'faultInst', u'trigLocalSched'], ["Get"])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "trigger-immediate", "triggered", "untriggered", "user-ack", "user-discard"], []), 
        "auto_delete": MoPropertyMeta("auto_delete", "autoDelete", "string", VersionMeta.Version211a, MoPropertyMeta.CREATE_ONLY, 0x2L, None, None, None, ["false", "no", "true", "yes"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x4L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "ignore_cap": MoPropertyMeta("ignore_cap", "ignoreCap", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_scheduler": MoPropertyMeta("oper_scheduler", "operScheduler", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["active", "applied", "apply-pending", "evaluated", "evaluation-pending", "expired", "none", "pending", "untriggered", "waiting-for-dependency", "waiting-for-maint-window", "waiting-for-user"], []), 
        "oper_version": MoPropertyMeta("oper_version", "operVersion", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "scheduler": MoPropertyMeta("scheduler", "scheduler", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "autoDelete": "auto_delete", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "ignoreCap": "ignore_cap", 
        "intId": "int_id", 
        "name": "name", 
        "operScheduler": "oper_scheduler", 
        "operState": "oper_state", 
        "operVersion": "oper_version", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "scheduler": "scheduler", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.auto_delete = None
        self.child_action = None
        self.descr = None
        self.ignore_cap = None
        self.int_id = None
        self.name = None
        self.oper_scheduler = None
        self.oper_state = None
        self.oper_version = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.scheduler = None
        self.status = None

        ManagedObject.__init__(self, "FirmwareInfra", parent_mo_or_dn, **kwargs)
