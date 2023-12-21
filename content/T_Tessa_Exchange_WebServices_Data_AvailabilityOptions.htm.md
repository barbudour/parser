# AvailabilityOptions - класс
Represents the options of a GetAvailability request.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AvailabilityOptions
VB __Копировать
     Public NotInheritable Class AvailabilityOptions
C++ __Копировать
     public ref class AvailabilityOptions sealed
F# __Копировать
     [<SealedAttribute>]
    type AvailabilityOptions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AvailabilityOptions
##  __Конструкторы
[AvailabilityOptions](M_Tessa_Exchange_WebServices_Data_AvailabilityOptions__ctor.htm)|
Initializes a new instance of the AvailabilityOptions class.  
---|---  
## __Свойства
[CurrentMeetingTime](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_CurrentMeetingTime.htm)|
Gets or sets the start time of a meeting that you want to update with the
suggested meeting times.  
---|---  
[DetailedSuggestionsWindow](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_DetailedSuggestionsWindow.htm)|
Gets or sets the time window for which detailed information about suggested
meeting times should be returned.  
[GlobalObjectId](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_GlobalObjectId.htm)|
Gets or sets the global object Id of a meeting that will be modified based on
the data returned by GetUserAvailability.  
[GoodSuggestionThreshold](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_GoodSuggestionThreshold.htm)|
Gets or sets the percentage of attendees that must have the time period open
for the time period to qualify as a good suggested meeting time.
GoodSuggestionThreshold must be between 1 and 49. The default value is 25.  
[MaximumNonWorkHoursSuggestionsPerDay](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_MaximumNonWorkHoursSuggestionsPerDay.htm)|
Gets or sets the number of suggested meeting times outside regular working
hours per day. MaximumNonWorkHoursSuggestionsPerDay must be between 0 and 48.
The default value is 0.  
[MaximumSuggestionsPerDay](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_MaximumSuggestionsPerDay.htm)|
Gets or sets the number of suggested meeting times that should be returned per
day. MaximumSuggestionsPerDay must be between 0 and 48. The default value is
10.  
[MeetingDuration](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_MeetingDuration.htm)|
Gets or sets the duration, in minutes, of the meeting for which to obtain
suggestions. MeetingDuration must be between 30 and 1440. The default value is
60.  
[MergedFreeBusyInterval](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_MergedFreeBusyInterval.htm)|
Gets or sets the time difference between two successive slots in a
FreeBusyMerged view. MergedFreeBusyInterval must be between 5 and 1440. The
default value is 30.  
[MinimumSuggestionQuality](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_MinimumSuggestionQuality.htm)|
Gets or sets the minimum quality of suggestions that should be returned. The
default is SuggestionQuality.Fair.  
[RequestedFreeBusyView](P_Tessa_Exchange_WebServices_Data_AvailabilityOptions_RequestedFreeBusyView.htm)|
Gets or sets the requested type of free/busy view. The default value is
FreeBusyViewType.Detailed.  
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
