# WorkflowInstanceCardService - класс
Реализация логгера и сервиса объектов экземпляра процесса, которая пишет в
карточку.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowInstanceCardService : IWorkflowInstanceService, 
    	IWorkflowEngineLogger, IAsyncDisposable
VB __Копировать
     Public NotInheritable Class WorkflowInstanceCardService
    	Implements IWorkflowInstanceService, IWorkflowEngineLogger, IAsyncDisposable
C++ __Копировать
     public ref class WorkflowInstanceCardService sealed : IWorkflowInstanceService, 
    	IWorkflowEngineLogger, IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type WorkflowInstanceCardService = 
        class
            interface IWorkflowInstanceService
            interface IWorkflowEngineLogger
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowInstanceCardService
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IWorkflowEngineLogger](T_Tessa_Workflow_IWorkflowEngineLogger.htm), [IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm)
##  __Конструкторы
[WorkflowInstanceCardService](M_Tessa_Workflow_WorkflowInstanceCardService__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowInstanceCardService  
---|---  
##  __Методы
[CreateNodeStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_CreateNodeStateAsync.htm)|
Метод для создания состояния узла по объеккту узла шаблона процесса  
---|---  
[CreateProcessStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_CreateProcessStateAsync.htm)|
Метод для создания экземпляра процесса по его шаблону  
[DeleteCommandSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_DeleteCommandSubscriptionAsync.htm)|
Метод для удаления подписки команды  
[DeleteNodeStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_DeleteNodeStateAsync.htm)|
Метод для удаления состояния узла. Вмсесте с состоянием узла удаляются все его
подписки  
[DeleteProcessStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_DeleteProcessStateAsync.htm)|
Метод для удаления состояния процесса  
[DeleteSubprocessSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_DeleteSubprocessSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
[DeleteTaskSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_DeleteTaskSubscriptionAsync.htm)|
Метод для удаления подписки  
[DeleteTimerSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_DeleteTimerSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
[DisposeAsync](M_Tessa_Workflow_WorkflowInstanceCardService_DisposeAsync.htm)|  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAllNodeStatesAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetAllNodeStatesAsync.htm)|
Метод для получения всех состояний узла по ID экземпляра процесса  
[GetCommandSubscriptionsAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetCommandSubscriptionsAsync.htm)|
Метод для получения списка подписок команды  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNodeStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetNodeStateAsync.htm)|
Метод для получения состояния узла по его ID  
[GetProcessInstanceIDAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetProcessInstanceIDAsync.htm)|
Метод для получения ID экземпляра процесса по ID экземпляра узла  
[GetProcessStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetProcessStateAsync.htm)|
Метод для получения экземпляра процесса по его ID  
[GetSubprocessSubscriptionsAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetSubprocessSubscriptionsAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
[GetTaskSubscriptionsAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetTaskSubscriptionsAsync.htm)|
Метод для получения списка подписок по заданию процесса  
[GetTimerSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_GetTimerSubscriptionAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetWorkflowCard](M_Tessa_Workflow_WorkflowInstanceCardService_GetWorkflowCard.htm)|
Метод возвращает карточку с данными экземпляра процесса.  
[LogAsync](M_Tessa_Workflow_WorkflowInstanceCardService_LogAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StoreCommandSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_StoreCommandSubscriptionAsync.htm)|
Метод для сохранения подписки команды  
[StoreNodeStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_StoreNodeStateAsync.htm)|
Метод для сохранения состояния узла  
[StoreProcessAndNodesStatesAsync](M_Tessa_Workflow_WorkflowInstanceCardService_StoreProcessAndNodesStatesAsync.htm)|
Метод для сохранения состояния процесса и состояний узлов  
[StoreProcessStateAsync](M_Tessa_Workflow_WorkflowInstanceCardService_StoreProcessStateAsync.htm)|
Метод для сохранения состояния процесса  
[StoreSubprocessSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_StoreSubprocessSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
[StoreTaskSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_StoreTaskSubscriptionAsync.htm)|
Метод для сохранения подписки задания  
[StoreTimerSubscriptionAsync](M_Tessa_Workflow_WorkflowInstanceCardService_StoreTimerSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
