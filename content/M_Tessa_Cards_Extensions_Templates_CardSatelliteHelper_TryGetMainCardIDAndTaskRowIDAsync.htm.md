# CardSatelliteHelper.TryGetMainCardIDAndTaskRowIDAsync - метод
Возвращает идентификатор основной карточки и идентификатор задания по
идентификатору карточки-сателлита задания или null, если сателлит не найден.
Возвращает признак того, что карточка запрошенная информация найдена. Вторым
значением возвращает идентификатор основной карточки или Guid.Empty, если
карточка-сателлит не найдена. Третьим значением возвращает идентификатор
задания или Guid.Empty, если карточка-сателлит не найдена.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<(bool result, Guid mainCardID, Guid taskRowID)> TryGetMainCardIDAndTaskRowIDAsync(
    	IDbScope dbScope,
    	Guid satelliteID,
    	string sectionName,
    	string mainCardIDFieldName,
    	string taskRowIDFieldName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetMainCardIDAndTaskRowIDAsync ( 
    	dbScope As IDbScope,
    	satelliteID As Guid,
    	sectionName As String,
    	mainCardIDFieldName As String,
    	taskRowIDFieldName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (result As Boolean, mainCardID As Guid, taskRowID As Guid))
C++ __Копировать
     public:
    static Task<ValueTuple<bool, Guid, Guid>>^ TryGetMainCardIDAndTaskRowIDAsync(
    	IDbScope^ dbScope, 
    	Guid satelliteID, 
    	String^ sectionName, 
    	String^ mainCardIDFieldName, 
    	String^ taskRowIDFieldName, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetMainCardIDAndTaskRowIDAsync : 
            dbScope : IDbScope * 
            satelliteID : Guid * 
            sectionName : string * 
            mainCardIDFieldName : string * 
            taskRowIDFieldName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, Guid, Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, предоставляющий доступ к базе данных.
satelliteID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки-сателлита.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя строковой секции в карточке-сателлите, в которой содержатся поля со ссылками на основную карточку и на задание. 
mainCardIDFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля в секции sectionName, в которой содержит идентификатор основной карточки. 
taskRowIDFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля в секции sectionName, в которой содержит идентификатор задания. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-3)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
true, если запрошенная информация найдена; false в противном случае.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
