# CardSatelliteHelper.TryGetUniversalSatelliteIDAsync - метод
Возвращает идентификатор сателлита по идентификатору основной карточки,
идентификатору задания и типу сателлита или null, если сателлит ещё не создан.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?> TryGetUniversalSatelliteIDAsync(
    	IDbScope dbScope,
    	Guid mainCardID,
    	Guid? taskID,
    	Guid satelliteTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetUniversalSatelliteIDAsync ( 
    	dbScope As IDbScope,
    	mainCardID As Guid,
    	taskID As Guid?,
    	satelliteTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    static Task<Nullable<Guid>>^ TryGetUniversalSatelliteIDAsync(
    	IDbScope^ dbScope, 
    	Guid mainCardID, 
    	Nullable<Guid> taskID, 
    	Guid satelliteTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetUniversalSatelliteIDAsync : 
            dbScope : IDbScope * 
            mainCardID : Guid * 
            taskID : Nullable<Guid> * 
            satelliteTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий выполнение запросов к базе данных.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки.
taskID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор задания, если сателлит относится к заданию.
satelliteTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа сателлита.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор сателлита, полученный по переданным параметрам, или null, если
сателлит ещё не создан.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
