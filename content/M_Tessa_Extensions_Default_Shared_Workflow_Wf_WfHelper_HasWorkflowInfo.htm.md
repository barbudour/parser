# WfHelper.HasWorkflowInfo - метод
Возвращает признак того, что заданная запись истории заданий содержит
информацию из расширенной истории заданий Workflow.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasWorkflowInfo(
    	CardTaskHistoryItem historyItem
    )
VB __Копировать
     Public Shared Function HasWorkflowInfo ( 
    	historyItem As CardTaskHistoryItem
    ) As Boolean
C++ __Копировать
     public:
    static bool HasWorkflowInfo(
    	CardTaskHistoryItem^ historyItem
    )
F# __Копировать
     static member HasWorkflowInfo : 
            historyItem : CardTaskHistoryItem -> bool 
#### Параметры
historyItem [CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm)
    Запись истории заданий.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если запись истории заданий содержит информацию из расширенной истории
заданий Workflow; false в противном случае.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
