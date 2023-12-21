# WorkflowEngineContextExtension - класс
Предоставляет методы расширения для
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WorkflowEngineContextExtension
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class WorkflowEngineContextExtension
C++ __Копировать
    [ExtensionAttribute]
    public ref class WorkflowEngineContextExtension abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type WorkflowEngineContextExtension = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineContextExtension
##  __Методы
[AddActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_AddActiveTaskAsync.htm)|
Добавляет указанный идентификатор задания в список активных заданий.  
---|---  
[AddToHistoryAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_AddToHistoryAsync.htm)|
Добавляет в историю процесса запись о задании.  
[GetActiveTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_GetActiveTasksAsync.htm)|
Возвращает доступную только для чтения коллекцию идентификаторов активных
заданий.  
[GetAuthorIDAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_GetAuthorIDAsync.htm)|
Возвращает идентификатор роли автора задания.  
[GetKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_GetKrSatelliteAsync.htm)|
Возвращает карточку основного сателлита
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm).  
[SendEditInterjectTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_SendEditInterjectTaskAsync.htm)|
Асинхронно отправляет задание доработки автором
([KrEditInterjectTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrEditInterjectTypeID.htm)).
Параметры задания берутся из секции
[SectionName](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_KrWeEditInterjectOptionsVirtual_SectionName.htm).  
[TryRemoveActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_TryRemoveActiveTaskAsync.htm)|
Удаляет указанный идентификатор задания из списка активных заданий.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)
