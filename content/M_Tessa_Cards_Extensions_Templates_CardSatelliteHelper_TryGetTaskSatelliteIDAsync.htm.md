# CardSatelliteHelper.TryGetTaskSatelliteIDAsync - метод
Возвращает идентификатор карточки-сателлита для задания с заданным
идентификатором, или null, если для задания отсутствует сателлит.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?> TryGetTaskSatelliteIDAsync(
    	IDbScope dbScope,
    	Guid taskRowID,
    	string sectionName,
    	string taskRowIDFieldName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetTaskSatelliteIDAsync ( 
    	dbScope As IDbScope,
    	taskRowID As Guid,
    	sectionName As String,
    	taskRowIDFieldName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    static Task<Nullable<Guid>>^ TryGetTaskSatelliteIDAsync(
    	IDbScope^ dbScope, 
    	Guid taskRowID, 
    	String^ sectionName, 
    	String^ taskRowIDFieldName, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetTaskSatelliteIDAsync : 
            dbScope : IDbScope * 
            taskRowID : Guid * 
            sectionName : string * 
            taskRowIDFieldName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, предоставляющий доступ к базе данных.
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя секции карточки-сателлита задания, в которой содержится поле с идентификатором задания. 
taskRowIDFieldName
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя поля в секции sectionName, в котором содержится идентификатор задания taskRowID. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор карточки-сателлита для задания с заданным идентификатором, или
null, если для задания отсутствует сателлит.
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
