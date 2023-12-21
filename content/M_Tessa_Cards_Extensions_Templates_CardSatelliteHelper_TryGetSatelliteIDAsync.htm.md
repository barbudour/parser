# CardSatelliteHelper.TryGetSatelliteIDAsync - метод
Возвращает идентификатор сателлита по идентификатору основной карточки или
null, если сателлит ещё не создан.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?> TryGetSatelliteIDAsync(
    	IDbScope dbScope,
    	Guid mainCardID,
    	string satelliteTableName,
    	string satelliteColumnName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetSatelliteIDAsync ( 
    	dbScope As IDbScope,
    	mainCardID As Guid,
    	satelliteTableName As String,
    	satelliteColumnName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    static Task<Nullable<Guid>>^ TryGetSatelliteIDAsync(
    	IDbScope^ dbScope, 
    	Guid mainCardID, 
    	String^ satelliteTableName, 
    	String^ satelliteColumnName, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetSatelliteIDAsync : 
            dbScope : IDbScope * 
            mainCardID : Guid * 
            satelliteTableName : string * 
            satelliteColumnName : string * 
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
satelliteTableName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя таблицы в карточке-сателлите, которая содержит ссылку на основную карточку. 
satelliteColumnName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя колонки в таблице satelliteTableName, которая содержит идентификатор основной карточки. Например, "MainCardID". 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор сателлита, полученный по идентификатору основной карточки, или
null, если сателлит ещё не создан.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
