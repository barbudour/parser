# EventType - перечисление
Defines the types of event that can occur in a folder.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum EventType
VB __Копировать
     Public Enumeration EventType
C++ __Копировать
     public enum class EventType
F# __Копировать
     type EventType
##  __Члены
Status| 0|  This event is sent to a client application by push notifications
to indicate that the subscription is still alive.  
---|---|---  
NewMail| 1|  This event indicates that a new e-mail message was received.  
Deleted| 2|  This event indicates that an item or folder has been deleted.  
Modified| 3|  This event indicates that an item or folder has been modified.  
Moved| 4|  This event indicates that an item or folder has been moved to
another folder.  
Copied| 5|  This event indicates that an item or folder has been copied to
another folder.  
Created| 6|  This event indicates that a new item or folder has been created.  
FreeBusyChanged| 7|  This event indicates that free/busy has changed. This is
only supported in 2010 SP1 or later  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
