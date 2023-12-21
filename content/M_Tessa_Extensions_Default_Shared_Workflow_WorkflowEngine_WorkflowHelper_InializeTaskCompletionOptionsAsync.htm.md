# WorkflowHelper.InializeTaskCompletionOptionsAsync - метод
Инициализирует указанный список строк, содержащий параметры обработки
вариантов завершения заданий указанных типов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask InializeTaskCompletionOptionsAsync(
    	ICardMetadata cardMetadata,
    	ListStorage<CardRow> rows,
    	CardRow templateRow,
    	IEnumerable<Guid> taskTypeIDs,
    	IValidationResultBuilder validationResult,
    	Object validationResultObject = null,
    	bool isSetTaskTypeInfo = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function InializeTaskCompletionOptionsAsync ( 
    	cardMetadata As ICardMetadata,
    	rows As ListStorage(Of CardRow),
    	templateRow As CardRow,
    	taskTypeIDs As IEnumerable(Of Guid),
    	validationResult As IValidationResultBuilder,
    	Optional validationResultObject As Object = Nothing,
    	Optional isSetTaskTypeInfo As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    static ValueTask InializeTaskCompletionOptionsAsync(
    	ICardMetadata^ cardMetadata, 
    	ListStorage<CardRow^>^ rows, 
    	CardRow^ templateRow, 
    	IEnumerable<Guid>^ taskTypeIDs, 
    	IValidationResultBuilder^ validationResult, 
    	Object^ validationResultObject = nullptr, 
    	bool isSetTaskTypeInfo = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member InializeTaskCompletionOptionsAsync : 
            cardMetadata : ICardMetadata * 
            rows : ListStorage<CardRow> * 
            templateRow : CardRow * 
            taskTypeIDs : IEnumerable<Guid> * 
            validationResult : IValidationResultBuilder * 
            ?validationResultObject : Object * 
            ?isSetTaskTypeInfo : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _validationResultObject = defaultArg validationResultObject null
            let _isSetTaskTypeInfo = defaultArg isSetTaskTypeInfo false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация, необходимая для использования типов карточек совместно с пакетом карточек.
rows
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>
    Инициализируемый список строк.
templateRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка, используемая в качестве шаблона. Значение не изменяется.
taskTypeIDs
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Перечисление идентификаторов типов заданий.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат выполнения.
validationResultObject
[Object](https://learn.microsoft.com/dotnet/api/system.object) (Optional)
    Ссылка на объект, определяющая фактический тип объекта, имя которого используется в сообщении валидации.
isSetTaskTypeInfo
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Значение true, если необходимо задать информацию о типе задания, иначе - false.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __Заметки
Секция не изменяется, если содержит значения.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
