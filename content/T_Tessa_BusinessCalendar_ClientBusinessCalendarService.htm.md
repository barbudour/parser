# ClientBusinessCalendarService - класс
##  __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientBusinessCalendarService : IBusinessCalendarService
VB __Копировать
     Public NotInheritable Class ClientBusinessCalendarService
    	Implements IBusinessCalendarService
C++ __Копировать
     public ref class ClientBusinessCalendarService sealed : IBusinessCalendarService
F# __Копировать
     [<SealedAttribute>]
    type ClientBusinessCalendarService = 
        class
            interface IBusinessCalendarService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientBusinessCalendarService
Implements
    [IBusinessCalendarService](T_Tessa_BusinessCalendar_IBusinessCalendarService.htm)
##  __Конструкторы
[ClientBusinessCalendarService](M_Tessa_BusinessCalendar_ClientBusinessCalendarService__ctor.htm)|
Инициализирует новый экземпляр класса ClientBusinessCalendarService  
---|---  
##  __Методы
[AddWorkingDaysToDateAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_AddWorkingDaysToDateAsync.htm)|
Получение даты рабочего времени смещением в рабочих днях относительно заданной
даты. Если указан zoneOffset, то dateTime должен быть задан в UTC. Если указан
zoneOffset, возвращаемое значение будет так же в UTC. Иначе - возвращаемое
значение будет в абстрактном времени календаря.  
---|---  
[AddWorkingQuantsToDateAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_AddWorkingQuantsToDateAsync.htm)|
Отсчёт рабочего времени от указанной даты. Если указан zoneOffset, то dateTime
должен быть задан в UTC. Если указан zoneOffset, возвращаемое значение будет
так же в UTC. Иначе - возвращаемое значение будет в абстрактном времени
календаря.  
[CalendarAddWorkingDaysToDateExactAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_CalendarAddWorkingDaysToDateExactAsync.htm)|
Добавление нужного количества рабочих дней к дате. Если указан zoneOffset, то
dateTime должен быть задан в UTC. Если указан zoneOffset, возвращаемое
значение будет так же в UTC. Иначе - возвращаемое значение будет в абстрактном
времени календаря.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDateDiffAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_GetDateDiffAsync.htm)|
Расчёт рабочего времени между датами. Если указан zoneOffset, то dateTimeStart
и dateTimeEnd должны быть задан в UTC.  
[GetFirstQuantStartAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_GetFirstQuantStartAsync.htm)|
Получение начала первого рабочего кванта рабочего дня, полученного смещением
относительно заданной даты. Если указан zoneOffset, то dateTime должен быть
задан в UTC. Если указан zoneOffset, возвращаемое значение будет так же в UTC.
Иначе - возвращаемое значение будет в абстрактном времени календаря.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLastQuantEndAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_GetLastQuantEndAsync.htm)|
Получение конца последнего рабочего кванта рабочего дня, полученного смещением
относительно заданной даты. Если указан zoneOffset, то dateTime должен быть
задан в UTC. Если указан zoneOffset, возвращаемое значение будет так же в UTC.
Иначе - возвращаемое значение будет в абстрактном времени календаря.  
[GetRoleTimeZoneInfoAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_GetRoleTimeZoneInfoAsync.htm)|
Возвращает Смещение временной зоны. для роли.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsWorkTimeAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_IsWorkTimeAsync.htm)|
Проверить - является ли рабочим указанное дата\время в абстрактном времени
календаря. Если указан zoneOffset, то dateTime должен быть задан в UTC.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RebuildCalendarAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_RebuildCalendarAsync.htm)|
Выполняет перестроение календаря на основании указанных настроек, в т.ч.
списка исключений.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ValidateCalendarAsync](M_Tessa_BusinessCalendar_ClientBusinessCalendarService_ValidateCalendarAsync.htm)|
Проверяет календарь на отсутствие пропусков между квантами. Непредвиденные
ошибки при выполнении на клиенте возвращаются в объекте
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm), а при
выполнении на сервере - выбрасываются в виде исключений.  
## __Методы расширения
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
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
