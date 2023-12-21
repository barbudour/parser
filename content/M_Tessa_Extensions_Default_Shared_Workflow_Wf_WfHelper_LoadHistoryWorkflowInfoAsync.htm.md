# WfHelper.LoadHistoryWorkflowInfoAsync - метод
Загружает расширенную информацию по бизнес-процессам Workflow для записей в
истории заданий, которые относятся к бизнес-процессам. Возвращает признак
того, что хотя бы для одной записи была установлена расширенная информация.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> LoadHistoryWorkflowInfoAsync(
    	Guid cardID,
    	Dictionary<Guid, CardTaskHistoryItem> historyItemsByRowID,
    	DbManager db,
    	IQueryBuilderFactory builderFactory,
    	bool loadCalendarInfo = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function LoadHistoryWorkflowInfoAsync ( 
    	cardID As Guid,
    	historyItemsByRowID As Dictionary(Of Guid, CardTaskHistoryItem),
    	db As DbManager,
    	builderFactory As IQueryBuilderFactory,
    	Optional loadCalendarInfo As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    static Task<bool>^ LoadHistoryWorkflowInfoAsync(
    	Guid cardID, 
    	Dictionary<Guid, CardTaskHistoryItem^>^ historyItemsByRowID, 
    	DbManager^ db, 
    	IQueryBuilderFactory^ builderFactory, 
    	bool loadCalendarInfo = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member LoadHistoryWorkflowInfoAsync : 
            cardID : Guid * 
            historyItemsByRowID : Dictionary<Guid, CardTaskHistoryItem> * 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            ?loadCalendarInfo : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _loadCalendarInfo = defaultArg loadCalendarInfo false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, история которой расширяется информацией по Workflow.
historyItemsByRowID
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm)>
     Хэш-таблица, содержащая записи истории заданий по их идентификаторам. Не может быть равна null. 
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, предоставляющий доступ к базе данных. Не может быть равен null.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект, выполняющий построение SQL-запросов.
loadCalendarInfo
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Признак того, что должна быть загружена информация по квантам календаря.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если хотя бы для одной записи была установлена расширенная информация;
false в противном случае.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
