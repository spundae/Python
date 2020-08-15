import ctypes # This is to import the ctypes classes from windows see 
              # https://github.com/python/cpython/blob/master/Lib/ctypes/wintypes.py

user_handle = ctypes.WinDLL("User32.dll") # this uses the User32.dll which has lots of api calls it can hanle
                                          # when you interfacing with a dll you would also need to load that dll

                                          # So if you want to use the messagebox what type is it?
                                          # See https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw
                                          # it is in user32.dll!
k_handle = ctypes.WinDLL("Kernel32.dll") # This is used for error handling

hWnd = None # if you lookup the https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw
'''
C++

Copy
int MessageBoxW(
  HWND    hWnd,
  LPCWSTR lpText,
  LPCWSTR lpCaption,
  UINT    uType
);


'''
lpText = "De lat zijn wij hoe dik je wordt bepaal jij"
lpCaption = "Phadaphapapa"
uType = 0x00000001

response = user_handle.MessageBoxW(hWnd, lpText,lpCaption, uType) # Capitalization is important!!! in Order Based on the DOCS!!!!!

error = k_handle.GetLastError()
if error !=0:
    print("error Code: {0}".format(error))
    exit(1)

if response == 1:
    print("User clicked ok!")
elif response == 2:
    print("User clicked cancel")