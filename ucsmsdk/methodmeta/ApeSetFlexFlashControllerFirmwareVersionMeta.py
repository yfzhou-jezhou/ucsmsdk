"""This module contains the meta information of ApeSetFlexFlashControllerFirmwareVersion ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeSetFlexFlashControllerFirmwareVersion", "apeSetFlexFlashControllerFirmwareVersion", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_ip_addr": MethodPropertyMeta("InIpAddr", "inIpAddr", "Xs:unsignedInt", "Version142b", "Input", False),
    "in_version": MethodPropertyMeta("InVersion", "inVersion", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inIpAddr": "in_ip_addr",
    "inVersion": "in_version",
}
