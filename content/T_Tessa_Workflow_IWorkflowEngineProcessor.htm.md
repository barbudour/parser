# IWorkflowEngineProcessor - интерфейс
Обработчик процессов WorkflowEngine на сервере.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowEngineProcessor
VB __Копировать
     Public Interface IWorkflowEngineProcessor
C++ __Копировать
     public interface class IWorkflowEngineProcessor
F# __Копировать
     type IWorkflowEngineProcessor = interface end
##  __Методы
[ProcessSignalAsync](M_Tessa_Workflow_IWorkflowEngineProcessor_ProcessSignalAsync.htm)|
Метод для обработки сигнала в процессе WorkflowEngine.  
---|---  
[SendAsyncSignalAsync](M_Tessa_Workflow_IWorkflowEngineProcessor_SendAsyncSignalAsync.htm)|
Производит асинхронную отправку сигнала в процесс.  
## __Методы расширения
[SendAsyncSignalAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendAsyncSignalAsync.htm)|
Производит асинхронную отправку сигнала процесса на заданный экземпляр узла.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
---|---  
[SendSignalAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalAsync.htm)|
Производит отправку сигнала на процесс.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
[SendSignalToAllSubscribersAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalToAllSubscribersAsync.htm)|
Производит отправку сигнала на все узлы процесса, подписанные на переданый тип
сигнала.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
[SendSignalToAllSubscribersWithContextAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalToAllSubscribersWithContextAsync.htm)|
Производит отправку сигнала на все узлы процесса, подписаныне на переданынй
тип сигнала.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
[SendSignalWithContextAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendSignalWithContextAsync.htm)|
Производит отправку сигнала на процесс в рамках заданного контекста обработки.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
[StartNewProcessAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_StartNewProcessAsync.htm)|
Производит создание нового экземпляра процесса и отправляет в него сигнал.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
