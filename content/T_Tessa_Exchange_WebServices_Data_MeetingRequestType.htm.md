# MeetingRequestType - перечисление
Defines the type of a meeting request.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum MeetingRequestType
VB __Копировать
     Public Enumeration MeetingRequestType
C++ __Копировать
     public enum class MeetingRequestType
F# __Копировать
     type MeetingRequestType
##  __Члены
None| 0|  Undefined meeting request type.  
---|---|---  
FullUpdate| 1|  The meeting request is an update to the original meeting.  
InformationalUpdate| 2|  The meeting request is an information update.  
NewMeetingRequest| 3|  The meeting request is for a new meeting.  
Outdated| 4|  The meeting request is outdated.  
SilentUpdate| 5|  The meeting update is a silent update to an existing
meeting.  
PrincipalWantsCopy| 6|  The meeting update was forwarded to a delegate, and
this copy is informational.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
