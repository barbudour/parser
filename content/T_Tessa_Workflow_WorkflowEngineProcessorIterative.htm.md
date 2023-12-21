# WorkflowEngineProcessorIterative - класс
Обработчик процессов WorkflowEngine на сервере.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowEngineProcessorIterative : IWorkflowEngineProcessor
VB __Копировать
     Public NotInheritable Class WorkflowEngineProcessorIterative
    	Implements IWorkflowEngineProcessor
C++ __Копировать
     public ref class WorkflowEngineProcessorIterative sealed : IWorkflowEngineProcessor
F# __Копировать
     [<SealedAttribute>]
    type WorkflowEngineProcessorIterative = 
        class
            interface IWorkflowEngineProcessor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineProcessorIterative
Implements
    [IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)
##  __Конструкторы
[WorkflowEngineProcessorIterative](M_Tessa_Workflow_WorkflowEngineProcessorIterative__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineProcessorIterative  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ProcessSignalAsync](M_Tessa_Workflow_WorkflowEngineProcessorIterative_ProcessSignalAsync.htm)|
Метод для обработки сигнала в процессе WorkflowEngine.  
[SendAsyncSignalAsync](M_Tessa_Workflow_WorkflowEngineProcessorIterative_SendAsyncSignalAsync.htm)|
Производит асинхронную отправку сигнала в процесс.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SendAsyncSignalAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_SendAsyncSignalAsync.htm)|
Производит асинхронную отправку сигнала процесса на заданный экземпляр узла.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[StartNewProcessAsync](M_Tessa_Workflow_WorkflowEngineProcessorExtensions_StartNewProcessAsync.htm)|
Производит создание нового экземпляра процесса и отправляет в него сигнал.  
(Определяется
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
