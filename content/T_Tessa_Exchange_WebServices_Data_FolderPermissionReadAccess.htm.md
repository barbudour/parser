# FolderPermissionReadAccess - перечисление
Defines a user's read access permission on items in a non-calendar folder.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum FolderPermissionReadAccess
VB __Копировать
     Public Enumeration FolderPermissionReadAccess
C++ __Копировать
     public enum class FolderPermissionReadAccess
F# __Копировать
     type FolderPermissionReadAccess
##  __Члены
None| 0|  The user has no read access on the items in the folder.  
---|---|---  
TimeOnly| 1|  The user can read the start and end date and time of
appointments. (Can only be applied to Calendar folders).  
TimeAndSubjectAndLocation| 2|  The user can read the start and end date and
time, subject and location of appointments. (Can only be applied to Calendar
folders).  
FullDetails| 3|  The user has access to the full details of items.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
