# BusinessCalendarService.RebuildCalendarAsync - метод
Интерфейс API бизнес календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task RebuildCalendarAsync(
    	Guid operationGuid,
    	DateTime dateTimeStart,
    	DateTime dateTimeEnd,
    	DateTime workTimeStart,
    	DateTime workTimeEnd,
    	DateTime lunchTimeStart,
    	DateTime lunchTimeEnd,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RebuildCalendarAsync ( 
    	operationGuid As Guid,
    	dateTimeStart As DateTime,
    	dateTimeEnd As DateTime,
    	workTimeStart As DateTime,
    	workTimeEnd As DateTime,
    	lunchTimeStart As DateTime,
    	lunchTimeEnd As DateTime,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ RebuildCalendarAsync(
    	Guid operationGuid, 
    	DateTime dateTimeStart, 
    	DateTime dateTimeEnd, 
    	DateTime workTimeStart, 
    	DateTime workTimeEnd, 
    	DateTime lunchTimeStart, 
    	DateTime lunchTimeEnd, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract RebuildCalendarAsync : 
            operationGuid : Guid * 
            dateTimeStart : DateTime * 
            dateTimeEnd : DateTime * 
            workTimeStart : DateTime * 
            workTimeEnd : DateTime * 
            lunchTimeStart : DateTime * 
            lunchTimeEnd : DateTime * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override RebuildCalendarAsync : 
            operationGuid : Guid * 
            dateTimeStart : DateTime * 
            dateTimeEnd : DateTime * 
            workTimeStart : DateTime * 
            workTimeEnd : DateTime * 
            lunchTimeStart : DateTime * 
            lunchTimeEnd : DateTime * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
operationGuid [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
dateTimeStart
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
dateTimeEnd [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
workTimeStart
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
workTimeEnd [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
lunchTimeStart
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
lunchTimeEnd
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[IBusinessCalendarService.RebuildCalendarAsync(Guid, DateTime, DateTime,
DateTime, DateTime, DateTime, DateTime,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_RebuildCalendarAsync.htm)  
##  __См. также
#### Ссылки
[BusinessCalendarService -
](T_Tessa_BusinessCalendar_BusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
