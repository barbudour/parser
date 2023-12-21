# BusinessCalendarService.GetRoleTimeZoneInfoAsync - метод
Интерфейс API бизнес календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<TimeZoneInfo> GetRoleTimeZoneInfoAsync(
    	Guid roleID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetRoleTimeZoneInfoAsync ( 
    	roleID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of TimeZoneInfo)
C++ __Копировать
     public:
    virtual Task<TimeZoneInfo^>^ GetRoleTimeZoneInfoAsync(
    	Guid roleID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetRoleTimeZoneInfoAsync : 
            roleID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<TimeZoneInfo> 
    override GetRoleTimeZoneInfoAsync : 
            roleID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<TimeZoneInfo> 
#### Параметры
roleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[TimeZoneInfo](T_Tessa_BusinessCalendar_TimeZoneInfo.htm)>
#### Реализации
[IBusinessCalendarService.GetRoleTimeZoneInfoAsync(Guid,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_GetRoleTimeZoneInfoAsync.htm)  
##  __См. также
#### Ссылки
[BusinessCalendarService -
](T_Tessa_BusinessCalendar_BusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
