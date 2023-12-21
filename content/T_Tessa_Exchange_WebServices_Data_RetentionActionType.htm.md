# RetentionActionType - перечисление
Defines the action of a retention policy tag.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum RetentionActionType
VB __Копировать
     Public Enumeration RetentionActionType
C++ __Копировать
     public enum class RetentionActionType
F# __Копировать
     type RetentionActionType
##  __Члены
None| 0|  Never tags (RetentionEnabled = false) do not have retention action
in the FAI.  
---|---|---  
MoveToDeletedItems| 1|  Expired items will be moved to the Deleted Items
folder.  
MoveToFolder| 2|  Expired items will be moved to the organizational folder
specified in the ExpirationDestination field.  
DeleteAndAllowRecovery| 3|  Expired items will be soft deleted.  
PermanentlyDelete| 4|  Expired items will be hard deleted.  
MarkAsPastRetentionLimit| 5|  Expired items will be tagged as expired.  
MoveToArchive| 6|  Expired items will be moved to the archive.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
