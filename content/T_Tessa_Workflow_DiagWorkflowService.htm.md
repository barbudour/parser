# DiagWorkflowService - класс
Реализация [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm), которая
выполняет логирование времени выполнения методов
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DiagWorkflowService : IWorkflowService, 
    	IWorkflowInstanceService
VB __Копировать
     Public NotInheritable Class DiagWorkflowService
    	Implements IWorkflowService, IWorkflowInstanceService
C++ __Копировать
     public ref class DiagWorkflowService sealed : IWorkflowService, 
    	IWorkflowInstanceService
F# __Копировать
     [<SealedAttribute>]
    type DiagWorkflowService = 
        class
            interface IWorkflowService
            interface IWorkflowInstanceService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DiagWorkflowService
Implements
    [IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm), [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)
##  __Конструкторы
[DiagWorkflowService](M_Tessa_Workflow_DiagWorkflowService__ctor.htm)|
Инициализирует новый экземпляр класса DiagWorkflowService  
---|---  
##  __Методы
[CreateNodeStateAsync](M_Tessa_Workflow_DiagWorkflowService_CreateNodeStateAsync.htm)|
Метод для создания состояния узла по объеккту узла шаблона процесса  
---|---  
[CreateProcessStateAsync](M_Tessa_Workflow_DiagWorkflowService_CreateProcessStateAsync.htm)|
Метод для создания экземпляра процесса по его шаблону  
[DeleteCommandSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_DeleteCommandSubscriptionAsync.htm)|
Метод для удаления подписки команды  
[DeleteNodeStateAsync](M_Tessa_Workflow_DiagWorkflowService_DeleteNodeStateAsync.htm)|
Метод для удаления состояния узла. Вмсесте с состоянием узла удаляются все его
подписки  
[DeleteProcessStateAsync](M_Tessa_Workflow_DiagWorkflowService_DeleteProcessStateAsync.htm)|
Метод для удаления состояния процесса  
[DeleteSubprocessSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_DeleteSubprocessSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
[DeleteTaskSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_DeleteTaskSubscriptionAsync.htm)|
Метод для удаления подписки  
[DeleteTimerSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_DeleteTimerSubscriptionAsync.htm)|
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
[GetAllModifiedTimerSubscriptionsAsync](M_Tessa_Workflow_DiagWorkflowService_GetAllModifiedTimerSubscriptionsAsync.htm)|
Метод для получения всех подписок таймеров  
[GetAllNodeStatesAsync](M_Tessa_Workflow_DiagWorkflowService_GetAllNodeStatesAsync.htm)|
Метод для получения всех состояний узла по ID экземпляра процесса  
[GetCommandSubscriptionsAsync](M_Tessa_Workflow_DiagWorkflowService_GetCommandSubscriptionsAsync.htm)|
Метод для получения списка подписок команды  
[GetDefaultVersionIDAsync](M_Tessa_Workflow_DiagWorkflowService_GetDefaultVersionIDAsync.htm)|
Метод для получения ID версии процесса, помеченной как по умолчанию  
[GetErrorDataAsync](M_Tessa_Workflow_DiagWorkflowService_GetErrorDataAsync.htm)|
Метод для получения данных об ошибке по её ID  
[GetErrorMessageAsync](M_Tessa_Workflow_DiagWorkflowService_GetErrorMessageAsync.htm)|
Возвращает сообщение об ошибке, указанное в шаблоне процесса  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLockStatusAsync](M_Tessa_Workflow_DiagWorkflowService_GetLockStatusAsync.htm)|
Получает информацию о блокировке текущей версии Бизнес-процесса и о карточке
Бизнес-процесса в целом (карточка заблокирована, если есть хоть одна
заблокированная карточка)  
[GetModifiedAsync](M_Tessa_Workflow_DiagWorkflowService_GetModifiedAsync.htm)|
Метод для получения даты изменения версии шаблона процесса  
[GetNodeStateAsync](M_Tessa_Workflow_DiagWorkflowService_GetNodeStateAsync.htm)|
Метод для получения состояния узла по его ID  
[GetProcessCardIDAsync](M_Tessa_Workflow_DiagWorkflowService_GetProcessCardIDAsync.htm)|
Метод для получения ID карточки процесса по ID состояния процесса  
[GetProcessCardIDsAsync](M_Tessa_Workflow_DiagWorkflowService_GetProcessCardIDsAsync.htm)|
Метод для получения списка идентификаторов карточек процессов по ID основной
карточки.  
[GetProcessInstanceIDAsync](M_Tessa_Workflow_DiagWorkflowService_GetProcessInstanceIDAsync.htm)|
Метод для получения ID экземпляра процесса по ID экземпляра узла  
[GetProcessStateAsync](M_Tessa_Workflow_DiagWorkflowService_GetProcessStateAsync.htm)|
Метод для получения экземпляра процесса по его ID  
[GetProcessVersionTemplateAsync](M_Tessa_Workflow_DiagWorkflowService_GetProcessVersionTemplateAsync.htm)|
Метод для получения Storage версии процесса.  
[GetSubprocessSubscriptionsAsync](M_Tessa_Workflow_DiagWorkflowService_GetSubprocessSubscriptionsAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
[GetTaskSubscriptionsAsync](M_Tessa_Workflow_DiagWorkflowService_GetTaskSubscriptionsAsync.htm)|
Метод для получения списка подписок по заданию процесса  
[GetTimerSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_GetTimerSubscriptionAsync.htm)|
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
[ResumeProcessAsync](M_Tessa_Workflow_DiagWorkflowService_ResumeProcessAsync.htm)|
Метод для возобновления процесса по ошибке.  
[SetIsDefaultAsync](M_Tessa_Workflow_DiagWorkflowService_SetIsDefaultAsync.htm)|
Метод для установки процесса по умолчанию.  
[StoreCommandSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_StoreCommandSubscriptionAsync.htm)|
Метод для сохранения подписки команды  
[StoreNodeStateAsync](M_Tessa_Workflow_DiagWorkflowService_StoreNodeStateAsync.htm)|
Метод для сохранения состояния узла  
[StoreProcessAndNodesStatesAsync](M_Tessa_Workflow_DiagWorkflowService_StoreProcessAndNodesStatesAsync.htm)|
Метод для сохранения состояния процесса и состояний узлов  
[StoreProcessStateAsync](M_Tessa_Workflow_DiagWorkflowService_StoreProcessStateAsync.htm)|
Метод для сохранения состояния процесса  
[StoreSubprocessSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_StoreSubprocessSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
[StoreTaskSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_StoreTaskSubscriptionAsync.htm)|
Метод для сохранения подписки задания  
[StoreTimerSubscriptionAsync](M_Tessa_Workflow_DiagWorkflowService_StoreTimerSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryLockVersionAsync](M_Tessa_Workflow_DiagWorkflowService_TryLockVersionAsync.htm)|
Метод для установки блокировки на версию процесса  
[TryUnlockVersionAsync](M_Tessa_Workflow_DiagWorkflowService_TryUnlockVersionAsync.htm)|
Метод для снятия блокировки с версии процесса  
[ValidateObjectAsync](M_Tessa_Workflow_DiagWorkflowService_ValidateObjectAsync.htm)|
Метод для валидации переданного объекта  
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
