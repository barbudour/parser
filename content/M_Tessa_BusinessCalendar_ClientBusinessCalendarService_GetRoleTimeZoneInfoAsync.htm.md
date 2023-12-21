# ClientBusinessCalendarService.GetRoleTimeZoneInfoAsync - метод
Возвращает Смещение временной зоны. для роли.
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
    Роль.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[TimeZoneInfo](T_Tessa_BusinessCalendar_TimeZoneInfo.htm)>  
Возвращает Смещение временной зоны. для роли.
#### Реализации
[IBusinessCalendarService.GetRoleTimeZoneInfoAsync(Guid,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_GetRoleTimeZoneInfoAsync.htm)  
##  __Исключения
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm)|
Ошибка при получении данных с сервера, если метод вызван на клиенте.  
---|---  
##  __См. также
#### Ссылки
[ClientBusinessCalendarService -
](T_Tessa_BusinessCalendar_ClientBusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
