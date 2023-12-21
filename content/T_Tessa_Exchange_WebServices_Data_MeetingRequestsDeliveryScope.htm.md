# MeetingRequestsDeliveryScope - перечисление
Defines how meeting requests are sent to delegates.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum MeetingRequestsDeliveryScope
VB __Копировать
     Public Enumeration MeetingRequestsDeliveryScope
C++ __Копировать
     public enum class MeetingRequestsDeliveryScope
F# __Копировать
     type MeetingRequestsDeliveryScope
##  __Члены
DelegatesOnly| 0|  Meeting requests are sent to delegates only.  
---|---|---  
DelegatesAndMe| 1|  Meeting requests are sent to delegates and to the owner of
the mailbox.  
DelegatesAndSendInformationToMe| 2|  Meeting requests are sent to delegates
and informational messages are sent to the owner of the mailbox.  
NoForward| 3|  Meeting requests are not sent to delegates. This value is
supported only for Exchange 2010 SP1 or later server versions.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
