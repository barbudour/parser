# CalendarActionResults - класс
Represents the results of an action performed on a calendar item or meeting
message, such as accepting, tentatively accepting or declining a meeting
request.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CalendarActionResults
VB __Копировать
     Public NotInheritable Class CalendarActionResults
C++ __Копировать
     public ref class CalendarActionResults sealed
F# __Копировать
     [<SealedAttribute>]
    type CalendarActionResults = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CalendarActionResults
##  __Свойства
[Appointment](P_Tessa_Exchange_WebServices_Data_CalendarActionResults_Appointment.htm)|
Gets the meeting that was accepted, tentatively accepted or declined.  
---|---  
[MeetingCancellation](P_Tessa_Exchange_WebServices_Data_CalendarActionResults_MeetingCancellation.htm)|
Gets the copy of the meeting cancellation message sent by the organizer to the
attendees of a meeting when the meeting is cancelled.  
[MeetingRequest](P_Tessa_Exchange_WebServices_Data_CalendarActionResults_MeetingRequest.htm)|
Gets the meeting request that was moved to the Deleted Items folder as a
result of an attendee accepting, tentatively accepting or declining a meeting
request. If the meeting request is accepted, tentatively accepted or declined
from the Deleted Items folder, it is permanently deleted and MeetingRequest is
null.  
[MeetingResponse](P_Tessa_Exchange_WebServices_Data_CalendarActionResults_MeetingResponse.htm)|
Gets the copy of the response that is sent to the organizer of a meeting when
the meeting is accepted, tentatively accepted or declined by an attendee.
MeetingResponse is null if the attendee chose not to send a response.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
