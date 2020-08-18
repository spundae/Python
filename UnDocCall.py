import ctypes

from ctypes.wintypes import DWORD, HANDLE, LPWSTR

k_handle = ctypes.WinDLL("Kernel32.dll")
d_handle = ctypes.WinDLL("DNSAPI.dll")

class DNS_CACHE_ENTRY(ctypes.Structure):
    _fields_ = [
        ("pNext", HANDLE),
        ("recName", LPWSTR),
        ("wType", DWORD),
        ("wDataLength", DWORD),
        ("dwFlags", DWORD)
    ]
DNS_Entry = DNS_CACHE_ENTRY()

DNS_Entry.wDataLength = 1024

response = d_handle.DnsGetCacheDataTable(ctypes.byref(DNS_Entry))

if response == 0:
    print("Error Code {0}".format(k_handle.GetLastError()))
    exit(1) 

DNS_Entry = ctypes.cast(DNS_Entry.pNext, ctypes.POINTER(DNS_CACHE_ENTRY))

while True:
    try:
        print("DNS ENTRY {0} - Type {1}".format(DNS_Entry.contents.recName, DNS_Entry.contents.wType))
        DNS_Entry = ctypes.cast(DNS_Entry.pNext, ctypes.POINTER(DNS_CACHE_ENTRY))     
    except:
        break
    