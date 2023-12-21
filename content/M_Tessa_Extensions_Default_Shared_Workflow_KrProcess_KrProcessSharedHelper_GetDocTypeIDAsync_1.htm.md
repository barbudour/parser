# KrProcessSharedHelper.GetDocTypeIDAsync(Card, IDbScope, CancellationToken) -
метод
Асинхронно возвращает идентификатор типа документа для карточки с указанным
идентификатором. Метод кэширует тип документа в Card.Info, если он не был
найден в объекте карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<Guid?> GetDocTypeIDAsync(
    	Card card,
    	IDbScope dbScope,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetDocTypeIDAsync ( 
    	card As Card,
    	dbScope As IDbScope,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Guid?)
C++ __Копировать
     public:
    static ValueTask<Nullable<Guid>> GetDocTypeIDAsync(
    	Card^ card, 
    	IDbScope^ dbScope, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetDocTypeIDAsync : 
            card : Card * 
            dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Nullable<Guid>> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется получить идентификатор типа документа.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект для взаимодействия с базой данных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор типа документа или значение null, если его не удалось получить
для указанной карточки.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[GetDocTypeIDAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetDocTypeIDAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
