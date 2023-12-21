# WorkflowEngineProcessorExtensions - класс
##  __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WorkflowEngineProcessorExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class WorkflowEngineProcessorExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class WorkflowEngineProcessorExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type WorkflowEngineProcessorExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineProcessorExtensions
##  __Методы
[SendAsyncSignalAsync(IWorkflowEngineProcessor, IWorkflowEngineSignal, Guid,
Guid, Boolean, String,
CancellationToken)](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendAsyncSignalAsync.htm)|
Производит асинхронную отправку сигнала процесса на заданный экземпляр узла.  
---|---  
[SendAsyncSignalAsync(IWorkflowEngineProcessorClient, IWorkflowEngineSignal,
Guid, Guid, Boolean, String,
CancellationToken)](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendAsyncSignalAsync_1.htm)|
Производит асинхронную отправку сигнала процесса на заданный экземпляр узла.  
[SendSignalAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalAsync.htm)|
Производит отправку сигнала на процесс.  
[SendSignalToAllSubscribersAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalToAllSubscribersAsync.htm)|
Производит отправку сигнала на все узлы процесса, подписанные на переданый тип
сигнала.  
[SendSignalToAllSubscribersWithContextAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalToAllSubscribersWithContextAsync.htm)|
Производит отправку сигнала на все узлы процесса, подписаныне на переданынй
тип сигнала.  
[SendSignalWithContextAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalWithContextAsync.htm)|
Производит отправку сигнала на процесс в рамках заданного контекста обработки.  
[StartNewProcessAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_StartNewProcessAsync.htm)|
Производит создание нового экземпляра процесса и отправляет в него сигнал.  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
