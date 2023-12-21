# KrProcessSharedHelper.GetDocTypeIDAsync(Guid, IDbScope, CancellationToken) -
метод
Асинхронно возвращает идентификатор типа документа для карточки с указанным
идентификатором.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<Guid?> GetDocTypeIDAsync(
    	Guid cardID,
    	IDbScope dbScope,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetDocTypeIDAsync ( 
    	cardID As Guid,
    	dbScope As IDbScope,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
     public:
    static Task<Nullable<Guid>>^ GetDocTypeIDAsync(
    	Guid cardID, 
    	IDbScope^ dbScope, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetDocTypeIDAsync : 
            cardID : Guid * 
            dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки для которой требуется получить идентификатор типа документа.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект для взаимодействия с базой данных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор типа документа или значение null, если не удалось получить
идентификатор типа документа для указанной карточки.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[GetDocTypeIDAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetDocTypeIDAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
