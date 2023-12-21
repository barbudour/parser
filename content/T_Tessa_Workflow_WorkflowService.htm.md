# WorkflowService - класс
Сервис для управления шаблонами, экземплярами и подписками Бизнес-процесса
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowService : IWorkflowService, 
    	IWorkflowInstanceService
VB __Копировать
     Public NotInheritable Class WorkflowService
    	Implements IWorkflowService, IWorkflowInstanceService
C++ __Копировать
     public ref class WorkflowService sealed : IWorkflowService, 
    	IWorkflowInstanceService
F# __Копировать
     [<SealedAttribute>]
    type WorkflowService = 
        class
            interface IWorkflowService
            interface IWorkflowInstanceService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowService
Implements
    [IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm), [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)
##  __Заметки
Если объект зарегистрирован без зависимости IWorkflowEngineCompiler, то это
внутри tadmin MigrateFiles или другой похожей команды, где нет компиляции.
## __Конструкторы
[WorkflowService](M_Tessa_Workflow_WorkflowService__ctor.htm)| Инициализирует
новый экземпляр класса WorkflowService  
---|---  
##  __Методы
[CreateNodeStateAsync](M_Tessa_Workflow_WorkflowService_CreateNodeStateAsync.htm)|
Метод для создания состояния узла по объеккту узла шаблона процесса  
---|---  
[CreateProcessStateAsync](M_Tessa_Workflow_WorkflowService_CreateProcessStateAsync.htm)|
Метод для создания экземпляра процесса по его шаблону  
[DeleteCommandSubscriptionAsync](M_Tessa_Workflow_WorkflowService_DeleteCommandSubscriptionAsync.htm)|
Метод для удаления подписки команды  
[DeleteNodeStateAsync](M_Tessa_Workflow_WorkflowService_DeleteNodeStateAsync.htm)|
Метод для удаления состояния узла. Вмсесте с состоянием узла удаляются все его
подписки  
[DeleteProcessStateAsync](M_Tessa_Workflow_WorkflowService_DeleteProcessStateAsync.htm)|
Метод для удаления состояния процесса  
[DeleteSubprocessSubscriptionAsync](M_Tessa_Workflow_WorkflowService_DeleteSubprocessSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
[DeleteTaskSubscriptionAsync](M_Tessa_Workflow_WorkflowService_DeleteTaskSubscriptionAsync.htm)|
Метод для удаления подписки  
[DeleteTimerSubscriptionAsync](M_Tessa_Workflow_WorkflowService_DeleteTimerSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
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
[GetAllModifiedTimerSubscriptionsAsync](M_Tessa_Workflow_WorkflowService_GetAllModifiedTimerSubscriptionsAsync.htm)|
Метод для получения всех обновленных после заданной даты подписок таймеров.
Если передан null, возвращает все подписки таймеров.  
[GetAllNodeStatesAsync](M_Tessa_Workflow_WorkflowService_GetAllNodeStatesAsync.htm)|
Метод для получения всех состояний узла по ID экземпляра процесса  
[GetCommandSubscriptionsAsync](M_Tessa_Workflow_WorkflowService_GetCommandSubscriptionsAsync.htm)|
Метод для получения списка подписок команды  
[GetDefaultVersionIDAsync](M_Tessa_Workflow_WorkflowService_GetDefaultVersionIDAsync.htm)|  
[GetErrorDataAsync](M_Tessa_Workflow_WorkflowService_GetErrorDataAsync.htm)|  
[GetErrorMessageAsync](M_Tessa_Workflow_WorkflowService_GetErrorMessageAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLockStatusAsync](M_Tessa_Workflow_WorkflowService_GetLockStatusAsync.htm)|  
[GetModifiedAsync](M_Tessa_Workflow_WorkflowService_GetModifiedAsync.htm)|  
[GetNodeStateAsync](M_Tessa_Workflow_WorkflowService_GetNodeStateAsync.htm)|
Метод для получения состояния узла по его ID  
[GetProcessCardIDAsync](M_Tessa_Workflow_WorkflowService_GetProcessCardIDAsync.htm)|
Метод для получения ID карточки процесса по ID состояния процесса  
[GetProcessCardIDsAsync](M_Tessa_Workflow_WorkflowService_GetProcessCardIDsAsync.htm)|  
[GetProcessInstanceIDAsync](M_Tessa_Workflow_WorkflowService_GetProcessInstanceIDAsync.htm)|  
[GetProcessStateAsync](M_Tessa_Workflow_WorkflowService_GetProcessStateAsync.htm)|
Метод для получения экземпляра процесса по его ID  
[GetProcessVersionTemplateAsync](M_Tessa_Workflow_WorkflowService_GetProcessVersionTemplateAsync.htm)|  
[GetSubprocessSubscriptionsAsync](M_Tessa_Workflow_WorkflowService_GetSubprocessSubscriptionsAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
[GetTaskSubscriptionsAsync](M_Tessa_Workflow_WorkflowService_GetTaskSubscriptionsAsync.htm)|
Метод для получения списка подписок по заданию процесса  
[GetTimerSubscriptionAsync](M_Tessa_Workflow_WorkflowService_GetTimerSubscriptionAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
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
[ResumeProcessAsync](M_Tessa_Workflow_WorkflowService_ResumeProcessAsync.htm)|  
[SetIsDefaultAsync](M_Tessa_Workflow_WorkflowService_SetIsDefaultAsync.htm)|  
[StoreCommandSubscriptionAsync](M_Tessa_Workflow_WorkflowService_StoreCommandSubscriptionAsync.htm)|
Метод для сохранения подписки команды  
[StoreNodeStateAsync](M_Tessa_Workflow_WorkflowService_StoreNodeStateAsync.htm)|
Метод для сохранения состояния узла  
[StoreProcessAndNodesStatesAsync](M_Tessa_Workflow_WorkflowService_StoreProcessAndNodesStatesAsync.htm)|
Метод для сохранения состояния процесса и состояний узлов  
[StoreProcessStateAsync](M_Tessa_Workflow_WorkflowService_StoreProcessStateAsync.htm)|
Метод для сохранения состояния процесса  
[StoreSubprocessSubscriptionAsync](M_Tessa_Workflow_WorkflowService_StoreSubprocessSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
[StoreTaskSubscriptionAsync](M_Tessa_Workflow_WorkflowService_StoreTaskSubscriptionAsync.htm)|
Метод для сохранения подписки задания  
[StoreTimerSubscriptionAsync](M_Tessa_Workflow_WorkflowService_StoreTimerSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryLockVersionAsync](M_Tessa_Workflow_WorkflowService_TryLockVersionAsync.htm)|  
[TryUnlockVersionAsync](M_Tessa_Workflow_WorkflowService_TryUnlockVersionAsync.htm)|  
[ValidateObjectAsync](M_Tessa_Workflow_WorkflowService_ValidateObjectAsync.htm)|  
## __Методы расширения
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
