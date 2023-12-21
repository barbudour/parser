# WorkflowHelper.GetValidatePerformerNotSpecifiedMessage - метод
Формирует сообщение валидации о том, что нет ни одного исполнителя.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetValidatePerformerNotSpecifiedMessage(
    	WorkflowActionStorage action,
    	WorkflowNodeStorage node,
    	string template = "$KrActions_PerformerNotSpecified"
    )
VB __Копировать
     Public Shared Function GetValidatePerformerNotSpecifiedMessage ( 
    	action As WorkflowActionStorage,
    	node As WorkflowNodeStorage,
    	Optional template As String = "$KrActions_PerformerNotSpecified"
    ) As String
C++ __Копировать
     public:
    static String^ GetValidatePerformerNotSpecifiedMessage(
    	WorkflowActionStorage^ action, 
    	WorkflowNodeStorage^ node, 
    	String^ template = L"$KrActions_PerformerNotSpecified"
    )
F# __Копировать
     static member GetValidatePerformerNotSpecifiedMessage : 
            action : WorkflowActionStorage * 
            node : WorkflowNodeStorage * 
            ?template : string 
    (* Defaults:
            let _template = defaultArg template "$KrActions_PerformerNotSpecified"
    *)
    -> string 
#### Параметры
action
[WorkflowActionStorage](T_Tessa_Workflow_Storage_WorkflowActionStorage.htm)
    Действие.
node [WorkflowNodeStorage](T_Tessa_Workflow_Storage_WorkflowNodeStorage.htm)
    Узел.
template [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Шаблон.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Сформированное сообщение.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
