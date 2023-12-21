# ClientWorkflowService - класс
Сервис для управления шаблонами, экземплярами и подписками Бизнес-процесса
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientWorkflowService : IWorkflowService, 
    	IWorkflowInstanceService
VB __Копировать
     Public NotInheritable Class ClientWorkflowService
    	Implements IWorkflowService, IWorkflowInstanceService
C++ __Копировать
     public ref class ClientWorkflowService sealed : IWorkflowService, 
    	IWorkflowInstanceService
F# __Копировать
     [<SealedAttribute>]
    type ClientWorkflowService = 
        class
            interface IWorkflowService
            interface IWorkflowInstanceService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientWorkflowService
Implements
    [IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm), [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)
##  __Конструкторы
[ClientWorkflowService](M_Tessa_Workflow_ClientWorkflowService__ctor.htm)|
Инициализирует новый экземпляр класса ClientWorkflowService  
---|---  
##  __Методы
[CreateNodeStateAsync](M_Tessa_Workflow_ClientWorkflowService_CreateNodeStateAsync.htm)|  
---|---  
[CreateProcessStateAsync](M_Tessa_Workflow_ClientWorkflowService_CreateProcessStateAsync.htm)|  
[DeleteCommandSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_DeleteCommandSubscriptionAsync.htm)|  
[DeleteNodeStateAsync](M_Tessa_Workflow_ClientWorkflowService_DeleteNodeStateAsync.htm)|  
[DeleteProcessStateAsync](M_Tessa_Workflow_ClientWorkflowService_DeleteProcessStateAsync.htm)|  
[DeleteSubprocessSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_DeleteSubprocessSubscriptionAsync.htm)|  
[DeleteTaskSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_DeleteTaskSubscriptionAsync.htm)|  
[DeleteTimerSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_DeleteTimerSubscriptionAsync.htm)|  
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
[GetAllModifiedTimerSubscriptionsAsync](M_Tessa_Workflow_ClientWorkflowService_GetAllModifiedTimerSubscriptionsAsync.htm)|  
[GetAllNodeStatesAsync](M_Tessa_Workflow_ClientWorkflowService_GetAllNodeStatesAsync.htm)|  
[GetCommandSubscriptionsAsync](M_Tessa_Workflow_ClientWorkflowService_GetCommandSubscriptionsAsync.htm)|  
[GetDefaultVersionIDAsync](M_Tessa_Workflow_ClientWorkflowService_GetDefaultVersionIDAsync.htm)|  
[GetErrorDataAsync](M_Tessa_Workflow_ClientWorkflowService_GetErrorDataAsync.htm)|  
[GetErrorMessageAsync](M_Tessa_Workflow_ClientWorkflowService_GetErrorMessageAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLockStatusAsync](M_Tessa_Workflow_ClientWorkflowService_GetLockStatusAsync.htm)|  
[GetModifiedAsync](M_Tessa_Workflow_ClientWorkflowService_GetModifiedAsync.htm)|  
[GetNodeStateAsync](M_Tessa_Workflow_ClientWorkflowService_GetNodeStateAsync.htm)|  
[GetProcessCardIDAsync](M_Tessa_Workflow_ClientWorkflowService_GetProcessCardIDAsync.htm)|  
[GetProcessCardIDsAsync](M_Tessa_Workflow_ClientWorkflowService_GetProcessCardIDsAsync.htm)|  
[GetProcessInstanceIDAsync](M_Tessa_Workflow_ClientWorkflowService_GetProcessInstanceIDAsync.htm)|  
[GetProcessStateAsync](M_Tessa_Workflow_ClientWorkflowService_GetProcessStateAsync.htm)|  
[GetProcessVersionTemplateAsync](M_Tessa_Workflow_ClientWorkflowService_GetProcessVersionTemplateAsync.htm)|  
[GetSubprocessSubscriptionsAsync](M_Tessa_Workflow_ClientWorkflowService_GetSubprocessSubscriptionsAsync.htm)|  
[GetTaskSubscriptionsAsync](M_Tessa_Workflow_ClientWorkflowService_GetTaskSubscriptionsAsync.htm)|  
[GetTimerSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_GetTimerSubscriptionAsync.htm)|  
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
[ResumeProcessAsync](M_Tessa_Workflow_ClientWorkflowService_ResumeProcessAsync.htm)|  
[SetIsDefaultAsync](M_Tessa_Workflow_ClientWorkflowService_SetIsDefaultAsync.htm)|  
[StoreCommandSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_StoreCommandSubscriptionAsync.htm)|  
[StoreNodeStateAsync](M_Tessa_Workflow_ClientWorkflowService_StoreNodeStateAsync.htm)|  
[StoreProcessAndNodesStatesAsync](M_Tessa_Workflow_ClientWorkflowService_StoreProcessAndNodesStatesAsync.htm)|  
[StoreProcessStateAsync](M_Tessa_Workflow_ClientWorkflowService_StoreProcessStateAsync.htm)|  
[StoreSubprocessSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_StoreSubprocessSubscriptionAsync.htm)|  
[StoreTaskSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_StoreTaskSubscriptionAsync.htm)|  
[StoreTimerSubscriptionAsync](M_Tessa_Workflow_ClientWorkflowService_StoreTimerSubscriptionAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryLockVersionAsync](M_Tessa_Workflow_ClientWorkflowService_TryLockVersionAsync.htm)|  
[TryUnlockVersionAsync](M_Tessa_Workflow_ClientWorkflowService_TryUnlockVersionAsync.htm)|  
[ValidateObjectAsync](M_Tessa_Workflow_ClientWorkflowService_ValidateObjectAsync.htm)|  
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
