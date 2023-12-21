# SendInvitationsOrCancellationsMode - перечисление
Defines if/how meeting invitations or cancellations should be sent to
attendees when an appointment is updated.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum SendInvitationsOrCancellationsMode
VB __Копировать
     Public Enumeration SendInvitationsOrCancellationsMode
C++ __Копировать
     public enum class SendInvitationsOrCancellationsMode
F# __Копировать
     type SendInvitationsOrCancellationsMode
##  __Члены
SendToNone| 0|  No meeting invitation/cancellation is sent.  
---|---|---  
SendOnlyToAll| 1|  Meeting invitations/cancellations are sent to all
attendees.  
SendOnlyToChanged| 2|  Meeting invitations/cancellations are sent only to
attendees that have been added or modified.  
SendToAllAndSaveCopy| 3|  Meeting invitations/cancellations are sent to all
attendees and a copy is saved in the organizer's Sent Items folder.  
SendToChangedAndSaveCopy| 4|  Meeting invitations/cancellations are sent only
to attendees that have been added or modified and a copy is saved in the
organizer's Sent Items folder.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
