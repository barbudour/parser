# SendCancellationsMode - перечисление
Defines how meeting cancellations should be sent to attendees when an
appointment is deleted.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum SendCancellationsMode
VB __Копировать
     Public Enumeration SendCancellationsMode
C++ __Копировать
     public enum class SendCancellationsMode
F# __Копировать
     type SendCancellationsMode
##  __Члены
SendToNone| 0|  No meeting cancellation is sent.  
---|---|---  
SendOnlyToAll| 1|  Meeting cancellations are sent to all attendees.  
SendToAllAndSaveCopy| 2|  Meeting cancellations are sent to all attendees and
a copy of the cancellation message is saved in the organizer's Sent Items
folder.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
