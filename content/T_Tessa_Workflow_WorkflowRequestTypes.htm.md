# WorkflowRequestTypes - класс
Типы запросов для [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm).
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WorkflowRequestTypes
VB __Копировать
     Public NotInheritable Class WorkflowRequestTypes
C++ __Копировать
     public ref class WorkflowRequestTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WorkflowRequestTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowRequestTypes
##  __Поля
[BusinessProcessChangeBlock](F_Tessa_Workflow_WorkflowRequestTypes_BusinessProcessChangeBlock.htm)|
Запрос на обновление блокировки версии бизнес-процесса  
---|---  
[BusinessProcessGetBlockStatus](F_Tessa_Workflow_WorkflowRequestTypes_BusinessProcessGetBlockStatus.htm)|
Запрос на получение состояния блокировки процесса  
[BusinessProcessGetVersion](F_Tessa_Workflow_WorkflowRequestTypes_BusinessProcessGetVersion.htm)|
Запрос на получение данных версии бизнес-процесса  
[BusinessProcessSetIsDefault](F_Tessa_Workflow_WorkflowRequestTypes_BusinessProcessSetIsDefault.htm)|
Запрос на установку значения по умолчанию  
[GetSourcesRequestType](F_Tessa_Workflow_WorkflowRequestTypes_GetSourcesRequestType.htm)|
Запрос на загрузку скриптов шаблона процесса  
[StartProcessButtonRequestType](F_Tessa_Workflow_WorkflowRequestTypes_StartProcessButtonRequestType.htm)|
Запрос на запуск глобального процесса  
[WorkflowEngineCompilerRequest](F_Tessa_Workflow_WorkflowRequestTypes_WorkflowEngineCompilerRequest.htm)|
Запрос на выполнение переданного метода
[IWorkflowEngineCompiler](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiler.htm)  
[WorkflowEngineProcessorRequest](F_Tessa_Workflow_WorkflowRequestTypes_WorkflowEngineProcessorRequest.htm)|
Запрос на выполнение методов из
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)  
[WorkflowGetGlobalTilesRequest](F_Tessa_Workflow_WorkflowRequestTypes_WorkflowGetGlobalTilesRequest.htm)|
Запрос на получение всех доступных тайлов WorkflowEngine  
[WorkflowServiceRequest](F_Tessa_Workflow_WorkflowRequestTypes_WorkflowServiceRequest.htm)|
Запрос на выполнение переданного метода
[IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)  
##  __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
