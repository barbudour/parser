# DeleteMode - перечисление
Represents deletion modes.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum DeleteMode
VB __Копировать
     Public Enumeration DeleteMode
C++ __Копировать
     public enum class DeleteMode
F# __Копировать
     type DeleteMode
##  __Члены
HardDelete| 0|  The item or folder will be permanently deleted.  
---|---|---  
SoftDelete| 1|  The item or folder will be moved to the dumpster. Items and
folders in the dumpster can be recovered.  
MoveToDeletedItems| 2|  The item or folder will be moved to the mailbox'
Deleted Items folder.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
