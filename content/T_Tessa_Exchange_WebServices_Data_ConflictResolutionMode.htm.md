# ConflictResolutionMode - перечисление
Defines how conflict resolutions are handled in update operations.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ConflictResolutionMode
VB __Копировать
     Public Enumeration ConflictResolutionMode
C++ __Копировать
     public enum class ConflictResolutionMode
F# __Копировать
     type ConflictResolutionMode
##  __Члены
NeverOverwrite| 0|  Local property changes are discarded.  
---|---|---  
AutoResolve| 1|  Local property changes are applied to the server unless the
server-side copy is more recent than the local copy.  
AlwaysOverwrite| 2|  Local property changes overwrite server-side changes.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
