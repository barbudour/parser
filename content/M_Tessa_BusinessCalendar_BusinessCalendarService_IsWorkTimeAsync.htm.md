# BusinessCalendarService.IsWorkTimeAsync - метод
Интерфейс API бизнес календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<BusinessCalendarTimeType> IsWorkTimeAsync(
    	DateTime dateTime,
    	TimeSpan? zoneOffset = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function IsWorkTimeAsync ( 
    	dateTime As DateTime,
    	Optional zoneOffset As TimeSpan? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of BusinessCalendarTimeType)
C++ __Копировать
     public:
    virtual Task<BusinessCalendarTimeType>^ IsWorkTimeAsync(
    	DateTime dateTime, 
    	Nullable<TimeSpan> zoneOffset = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract IsWorkTimeAsync : 
            dateTime : DateTime * 
            ?zoneOffset : Nullable<TimeSpan> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _zoneOffset = defaultArg zoneOffset null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<BusinessCalendarTimeType> 
    override IsWorkTimeAsync : 
            dateTime : DateTime * 
            ?zoneOffset : Nullable<TimeSpan> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _zoneOffset = defaultArg zoneOffset null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<BusinessCalendarTimeType> 
#### Параметры
dateTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
zoneOffset
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)>
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[BusinessCalendarTimeType](T_Tessa_BusinessCalendar_BusinessCalendarTimeType.htm)>
#### Реализации
[IBusinessCalendarService.IsWorkTimeAsync(DateTime, Nullable<TimeSpan>,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_IsWorkTimeAsync.htm)  
##  __См. также
#### Ссылки
[BusinessCalendarService -
](T_Tessa_BusinessCalendar_BusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
