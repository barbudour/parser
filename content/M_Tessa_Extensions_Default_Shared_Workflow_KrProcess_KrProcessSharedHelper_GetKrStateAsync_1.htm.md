# KrProcessSharedHelper.GetKrStateAsync(Card, IDbScope, CancellationToken) -
метод
Асинхронно возвращает состояние карточки из возможных источников:
Секция KrApprovalCommonInfoVirtual;
Сателлит из Info карточки;
БД (опционально).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<KrState?> GetKrStateAsync(
    	Card card,
    	IDbScope dbScope = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetKrStateAsync ( 
    	card As Card,
    	Optional dbScope As IDbScope = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of KrState?)
C++ __Копировать
     public:
    static ValueTask<Nullable<KrState>> GetKrStateAsync(
    	Card^ card, 
    	IDbScope^ dbScope = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetKrStateAsync : 
            card : Card * 
            ?dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Nullable<KrState>> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка для которой требуется получить состояние.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
    Объект для взаимодействия с базой данных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[KrState](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrState.htm)>>  
Состояние карточки.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[GetKrStateAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_GetKrStateAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
