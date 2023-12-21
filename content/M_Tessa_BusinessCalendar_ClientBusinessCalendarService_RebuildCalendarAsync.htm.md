# ClientBusinessCalendarService.RebuildCalendarAsync - метод
Выполняет перестроение календаря на основании указанных настроек, в т.ч.
списка исключений.
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
    Guid операции.
dateTimeStart
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Первая дата в абстрактном времени календаря.
dateTimeEnd [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Вторая дата в абстрактном времени календаря (должна быть больше первой).
workTimeStart
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Начало рабочего дня.
workTimeEnd [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Конец рабочего дня.
lunchTimeStart
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Начало обеда.
lunchTimeEnd
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Конец обеда.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IBusinessCalendarService.RebuildCalendarAsync(Guid, DateTime, DateTime,
DateTime, DateTime, DateTime, DateTime,
CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_RebuildCalendarAsync.htm)  
##  __Исключения
[ValidationException](T_Tessa_Platform_Validation_ValidationException.htm)|
Ошибка при получении данных с сервера, если метод вызван на клиенте.  
---|---  
##  __См. также
#### Ссылки
[ClientBusinessCalendarService -
](T_Tessa_BusinessCalendar_ClientBusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
