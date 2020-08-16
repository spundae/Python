# Import the required module to handle Windows API Calls
import ctypes

# Grab a handle to kernel32.dll
u_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

"""
We are going to work in this function first
FindWindowA
Which takes :

HWND FindWindowA(
  LPCSTR lpClassName,
  LPCSTR lpWindowName
);
"""
lpWindowName = ctypes.c_char_p(input("Enter Window Name to Kill: ").encode('UTF-8'))

print(lpWindowName)

hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
    print("Error Code: {0} - Could not grab handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got Handle..")

lpdwProcessId = ctypes.c_ulong()

response = u_handle.GetWindowThreadProcessId(hWnd,ctypes.byref(lpdwProcessId))

print(response)

if response ==0:
    print("Error Code: {0} - Could not grab PID".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got our handle")

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle,dwProcessId  )

if hProcess <= 0:
    print("Error Code: {0} - Could not grab Priviledge Handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("We have the correct Priviledge handle!")

uExitCode = 0x1
response = k_handle.TerminateProcess(hProcess, uExitCode)

if response == 0:
    print("Error Code: {0} - Could not grab Priviledge Handle".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Terminated the process")
    exit(0)

"""

handle  = u_handle.FindWindowA(lpClassName,lpWindowName )
error = k_handle.GetLastError()
print (error)
if error != 0:
    print("Error Code: {0}".format(error))
    exit(1)
else: 
    exit(0)



hWnd = handle
lpdwProcessId = 



"""