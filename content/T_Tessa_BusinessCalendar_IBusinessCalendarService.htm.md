# IBusinessCalendarService - интерфейс
Интерфейс API бизнес календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IBusinessCalendarService
VB __Копировать
     Public Interface IBusinessCalendarService
C++ __Копировать
     public interface class IBusinessCalendarService
F# __Копировать
     type IBusinessCalendarService = interface end
##  __Методы
[AddWorkingDaysToDateAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_AddWorkingDaysToDateAsync.htm)|
Получение даты рабочего времени смещением в рабочих днях относительно заданной
даты. Если указан zoneOffset, то dateTime должен быть задан в UTC. Если указан
zoneOffset, возвращаемое значение будет так же в UTC. Иначе - возвращаемое
значение будет в абстрактном времени календаря.  
---|---  
[AddWorkingQuantsToDateAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_AddWorkingQuantsToDateAsync.htm)|
Отсчёт рабочего времени от указанной даты. Если указан zoneOffset, то dateTime
должен быть задан в UTC. Если указан zoneOffset, возвращаемое значение будет
так же в UTC. Иначе - возвращаемое значение будет в абстрактном времени
календаря.  
[CalendarAddWorkingDaysToDateExactAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_CalendarAddWorkingDaysToDateExactAsync.htm)|
Добавление нужного количества рабочих дней к дате. Если указан zoneOffset, то
dateTime должен быть задан в UTC. Если указан zoneOffset, возвращаемое
значение будет так же в UTC. Иначе - возвращаемое значение будет в абстрактном
времени календаря.  
[GetDateDiffAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_GetDateDiffAsync.htm)|
Расчёт рабочего времени между датами. Если указан zoneOffset, то dateTimeStart
и dateTimeEnd должны быть задан в UTC.  
[GetFirstQuantStartAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_GetFirstQuantStartAsync.htm)|
Получение начала первого рабочего кванта рабочего дня, полученного смещением
относительно заданной даты. Если указан zoneOffset, то dateTime должен быть
задан в UTC. Если указан zoneOffset, возвращаемое значение будет так же в UTC.
Иначе - возвращаемое значение будет в абстрактном времени календаря.  
[GetLastQuantEndAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_GetLastQuantEndAsync.htm)|
Получение конца последнего рабочего кванта рабочего дня, полученного смещением
относительно заданной даты. Если указан zoneOffset, то dateTime должен быть
задан в UTC. Если указан zoneOffset, возвращаемое значение будет так же в UTC.
Иначе - возвращаемое значение будет в абстрактном времени календаря.  
[GetRoleTimeZoneInfoAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_GetRoleTimeZoneInfoAsync.htm)|
Возвращает Смещение временной зоны. для роли.  
[IsWorkTimeAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_IsWorkTimeAsync.htm)|
Проверить - является ли рабочим указанное дата\время в абстрактном времени
календаря. Если указан zoneOffset, то dateTime должен быть задан в UTC.  
[RebuildCalendarAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_RebuildCalendarAsync.htm)|
Выполняет перестроение календаря на основании указанных настроек, в т.ч.
списка исключений.  
[ValidateCalendarAsync](M_Tessa_BusinessCalendar_IBusinessCalendarService_ValidateCalendarAsync.htm)|
Проверяет календарь на отсутствие пропусков между квантами. Непредвиденные
ошибки при выполнении на клиенте возвращаются в объекте
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm), а при
выполнении на сервере - выбрасываются в виде исключений.  
## __См. также
#### Ссылки
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
