# WorkflowHelper.InializeActionCompletionOptions - метод
Инициализирует указанный список строк, содержащий параметры обработки
вариантов завершения действий, заданными вариантами завершения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void InializeActionCompletionOptions(
    	IReadOnlyDictionary<Guid, ActionCompletionOption> completionOptions,
    	ListStorage<CardRow> rows,
    	CardRow templateRow,
    	IList<Guid> optionIDs
    )
VB __Копировать
     Public Shared Sub InializeActionCompletionOptions ( 
    	completionOptions As IReadOnlyDictionary(Of Guid, ActionCompletionOption),
    	rows As ListStorage(Of CardRow),
    	templateRow As CardRow,
    	optionIDs As IList(Of Guid)
    )
C++ __Копировать
     public:
    static void InializeActionCompletionOptions(
    	IReadOnlyDictionary<Guid, ActionCompletionOption^>^ completionOptions, 
    	ListStorage<CardRow^>^ rows, 
    	CardRow^ templateRow, 
    	IList<Guid>^ optionIDs
    )
F# __Копировать
     static member InializeActionCompletionOptions : 
            completionOptions : IReadOnlyDictionary<Guid, ActionCompletionOption> * 
            rows : ListStorage<CardRow> * 
            templateRow : CardRow * 
            optionIDs : IList<Guid> -> unit 
#### Параметры
completionOptions
[IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[ActionCompletionOption](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_ActionCompletionOption.htm)>
    Коллекция содержащая информацию о вариантах завершения.
rows
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>
    Инициализируемый список строк.
templateRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка, используемая в качестве шаблона. Значение не изменяется.
optionIDs
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Перечисление идентификаторов вариантов завершения.
##  __Заметки
Секция не изменяется, если содержит значения.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
