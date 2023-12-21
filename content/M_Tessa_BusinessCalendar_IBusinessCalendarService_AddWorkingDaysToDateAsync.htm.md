# IBusinessCalendarService.AddWorkingDaysToDateAsync - метод
Получение даты рабочего времени смещением в рабочих днях относительно заданной
даты. Если указан zoneOffset, то dateTime должен быть задан в UTC. Если указан
zoneOffset, возвращаемое значение будет так же в UTC. Иначе - возвращаемое
значение будет в абстрактном времени календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<DateTime> AddWorkingDaysToDateAsync(
    	DateTime dateTime,
    	double daysOffset,
    	TimeSpan? zoneOffset = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function AddWorkingDaysToDateAsync ( 
    	dateTime As DateTime,
    	daysOffset As Double,
    	Optional zoneOffset As TimeSpan? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of DateTime)
C++ __Копировать
    Task<DateTime>^ AddWorkingDaysToDateAsync(
    	DateTime dateTime, 
    	double daysOffset, 
    	Nullable<TimeSpan> zoneOffset = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract AddWorkingDaysToDateAsync : 
            dateTime : DateTime * 
            daysOffset : float * 
            ?zoneOffset : Nullable<TimeSpan> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _zoneOffset = defaultArg zoneOffset null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<DateTime> 
#### Параметры
dateTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата в абстрактном времени календаря или в UTC, если указан zoneOffset.
daysOffset [Double](https://learn.microsoft.com/dotnet/api/system.double)
    Смещение в рабочих днях.
zoneOffset
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)>
(Optional)
    Смещение временной зоны.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>  
Возвращает дату рабочего времени в абстрактном времени календаря. Либо в UTC,
если был задан zoneOffset.
##  __Исключения
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm)|
Ошибка при получении данных с сервера, если метод вызван на клиенте.  
---|---  
##  __См. также
#### Ссылки
[IBusinessCalendarService -
](T_Tessa_BusinessCalendar_IBusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
