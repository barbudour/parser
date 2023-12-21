# CardSatelliteHelper.TryGetMainCardIDFromSatelliteIDAsync - метод
Возвращает идентификатор основной карточки по идентификатору карточки-
сателлита или null, если сателлит не найден.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?> TryGetMainCardIDFromSatelliteIDAsync(
    	IDbScope dbScope,
    	Guid satelliteID,
    	string sectionName,
    	string mainCardIDFieldName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetMainCardIDFromSatelliteIDAsync ( 
    	dbScope As IDbScope,
    	satelliteID As Guid,
    	sectionName As String,
    	mainCardIDFieldName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    static Task<Nullable<Guid>>^ TryGetMainCardIDFromSatelliteIDAsync(
    	IDbScope^ dbScope, 
    	Guid satelliteID, 
    	String^ sectionName, 
    	String^ mainCardIDFieldName, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetMainCardIDFromSatelliteIDAsync : 
            dbScope : IDbScope * 
            satelliteID : Guid * 
            sectionName : string * 
            mainCardIDFieldName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, предоставляющий доступ к базе данных.
satelliteID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки-сателлита.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя строковой секции в карточке-сателлите, в которой содержится поле со ссылкой на основную карточку. 
mainCardIDFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля в секции sectionName, в которой содержит идентификатор основной карточки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор основной карточки по идентификатору карточки-сателлита или null,
если сателлит не найден.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
