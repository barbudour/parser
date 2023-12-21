# BusinessCalendarService.GetDateDiffAsync - метод
Интерфейс API бизнес календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<long> GetDateDiffAsync(
    	DateTime dateTimeStart,
    	DateTime dateTimeEnd,
    	TimeSpan? zoneOffset = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetDateDiffAsync ( 
    	dateTimeStart As DateTime,
    	dateTimeEnd As DateTime,
    	Optional zoneOffset As TimeSpan? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Long)
C++ __Копировать
     public:
    virtual Task<long long>^ GetDateDiffAsync(
    	DateTime dateTimeStart, 
    	DateTime dateTimeEnd, 
    	Nullable<TimeSpan> zoneOffset = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetDateDiffAsync : 
            dateTimeStart : DateTime * 
            dateTimeEnd : DateTime * 
            ?zoneOffset : Nullable<TimeSpan> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _zoneOffset = defaultArg zoneOffset null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<int64> 
    override GetDateDiffAsync : 
            dateTimeStart : DateTime * 
            dateTimeEnd : DateTime * 
            ?zoneOffset : Nullable<TimeSpan> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _zoneOffset = defaultArg zoneOffset null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<int64> 
#### Параметры
dateTimeStart
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
dateTimeEnd [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
zoneOffset
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)>
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
#### Реализации
[IBusinessCalendarService.GetDateDiffAsync(DateTime, DateTime,
Nullable<TimeSpan>,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_GetDateDiffAsync.htm)  
##  __См. также
#### Ссылки
[BusinessCalendarService -
](T_Tessa_BusinessCalendar_BusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
