# CardSatelliteHelper.TryGetSatelliteIDListAsync - метод
Возвращает список идентификаторов карточек-сателлитов для заданной основной
карточки или null, если список пустой.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<List<Guid>> TryGetSatelliteIDListAsync(
    	IDbScope dbScope,
    	Guid mainCardID,
    	string sectionName,
    	string mainCardIDFieldName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetSatelliteIDListAsync ( 
    	dbScope As IDbScope,
    	mainCardID As Guid,
    	sectionName As String,
    	mainCardIDFieldName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of Guid))
C++ __Копировать
     public:
    static Task<List<Guid>^>^ TryGetSatelliteIDListAsync(
    	IDbScope^ dbScope, 
    	Guid mainCardID, 
    	String^ sectionName, 
    	String^ mainCardIDFieldName, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetSatelliteIDListAsync : 
            dbScope : IDbScope * 
            mainCardID : Guid * 
            sectionName : string * 
            mainCardIDFieldName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, предоставляющий доступ к базе данных.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки.
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
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Список идентификаторов карточек-сателлитов для заданной основной карточки или
null, если список пустой.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
