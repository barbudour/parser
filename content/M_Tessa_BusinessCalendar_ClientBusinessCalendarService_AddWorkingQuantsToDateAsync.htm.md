# ClientBusinessCalendarService.AddWorkingQuantsToDateAsync - метод
Отсчёт рабочего времени от указанной даты. Если указан zoneOffset, то dateTime
должен быть задан в UTC. Если указан zoneOffset, возвращаемое значение будет
так же в UTC. Иначе - возвращаемое значение будет в абстрактном времени
календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<DateTime> AddWorkingQuantsToDateAsync(
    	DateTime dateTime,
    	long quants,
    	TimeSpan? zoneOffset = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function AddWorkingQuantsToDateAsync ( 
    	dateTime As DateTime,
    	quants As Long,
    	Optional zoneOffset As TimeSpan? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of DateTime)
C++ __Копировать
     public:
    virtual Task<DateTime>^ AddWorkingQuantsToDateAsync(
    	DateTime dateTime, 
    	long long quants, 
    	Nullable<TimeSpan> zoneOffset = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract AddWorkingQuantsToDateAsync : 
            dateTime : DateTime * 
            quants : int64 * 
            ?zoneOffset : Nullable<TimeSpan> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _zoneOffset = defaultArg zoneOffset null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<DateTime> 
    override AddWorkingQuantsToDateAsync : 
            dateTime : DateTime * 
            quants : int64 * 
            ?zoneOffset : Nullable<TimeSpan> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _zoneOffset = defaultArg zoneOffset null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<DateTime> 
#### Параметры
dateTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата\время в абстрактном времени календаря, к которому производится добавление.
quants [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    рабочее время в квантах.
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
Возвращает дату\время в абстрактном времени календаря. Либо в UTC, если был
задан zoneOffset. Дата округляется до 15 минут в большую сторону.
#### Реализации
[IBusinessCalendarService.AddWorkingQuantsToDateAsync(DateTime, Int64,
Nullable<TimeSpan>,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_AddWorkingQuantsToDateAsync.htm)  
##  __Исключения
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm)|
Ошибка при получении данных с сервера, если метод вызван на клиенте.  
---|---  
##  __См. также
#### Ссылки
[ClientBusinessCalendarService -
](T_Tessa_BusinessCalendar_ClientBusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
