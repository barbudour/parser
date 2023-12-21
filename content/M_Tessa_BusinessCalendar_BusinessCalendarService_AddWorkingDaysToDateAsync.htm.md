# BusinessCalendarService.AddWorkingDaysToDateAsync - метод
Интерфейс API бизнес календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<DateTime> AddWorkingDaysToDateAsync(
    	DateTime dateTime,
    	double daysOffset,
    	TimeSpan? zoneOffset = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function AddWorkingDaysToDateAsync ( 
    	dateTime As DateTime,
    	daysOffset As Double,
    	Optional zoneOffset As TimeSpan? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of DateTime)
C++ __Копировать
     public:
    virtual Task<DateTime>^ AddWorkingDaysToDateAsync(
    	DateTime dateTime, 
    	double daysOffset, 
    	Nullable<TimeSpan> zoneOffset = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
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
    override AddWorkingDaysToDateAsync : 
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
daysOffset [Double](https://learn.microsoft.com/dotnet/api/system.double)
zoneOffset
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)>
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
#### Реализации
[IBusinessCalendarService.AddWorkingDaysToDateAsync(DateTime, Double,
Nullable<TimeSpan>,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_AddWorkingDaysToDateAsync.htm)  
##  __См. также
#### Ссылки
[BusinessCalendarService -
](T_Tessa_BusinessCalendar_BusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
