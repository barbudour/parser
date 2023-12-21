# LogonProvider - перечисление
##  __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum LogonProvider
VB __Копировать
     Public Enumeration LogonProvider
C++ __Копировать
     public enum class LogonProvider
F# __Копировать
     type LogonProvider
##  __Члены
Default| 0|  Use the standard logon provider for the system. The default
security provider is negotiate, unless you pass NULL for the domain name and
the user name is not in UPN format. In this case, the default provider is
NTLM.  
---|---|---  
WinNT35| 1|  Use the win 3.5 logon provider  
WinNT40| 2|  Use the NTLM logon provider.  
WinNT50| 3|  Use the negotiate logon provider.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
