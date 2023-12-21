# IWorkflowService - интерфейс
Сервис для управления шаблонами, экземплярами и подписками Бизнес-процесса
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowService : IWorkflowInstanceService
VB __Копировать
     Public Interface IWorkflowService
    	Inherits IWorkflowInstanceService
C++ __Копировать
     public interface class IWorkflowService : IWorkflowInstanceService
F# __Копировать
     type IWorkflowService = 
        interface
            interface IWorkflowInstanceService
        end
Implements
    [IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm)
##  __Методы
[CreateNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_CreateNodeStateAsync.htm)|
Метод для создания состояния узла по объеккту узла шаблона процесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
---|---  
[CreateProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_CreateProcessStateAsync.htm)|
Метод для создания экземпляра процесса по его шаблону  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[DeleteCommandSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteCommandSubscriptionAsync.htm)|
Метод для удаления подписки команды  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[DeleteNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteNodeStateAsync.htm)|
Метод для удаления состояния узла. Вмсесте с состоянием узла удаляются все его
подписки  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[DeleteProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteProcessStateAsync.htm)|
Метод для удаления состояния процесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[DeleteSubprocessSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteSubprocessSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[DeleteTaskSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteTaskSubscriptionAsync.htm)|
Метод для удаления подписки  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[DeleteTimerSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteTimerSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetAllModifiedTimerSubscriptionsAsync](M_Tessa_Workflow_IWorkflowService_GetAllModifiedTimerSubscriptionsAsync.htm)|
Метод для получения всех подписок таймеров  
[GetAllNodeStatesAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetAllNodeStatesAsync.htm)|
Метод для получения всех состояний узла по ID экземпляра процесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetCommandSubscriptionsAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetCommandSubscriptionsAsync.htm)|
Метод для получения списка подписок команды  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetDefaultVersionIDAsync](M_Tessa_Workflow_IWorkflowService_GetDefaultVersionIDAsync.htm)|
Метод для получения ID версии процесса, помеченной как по умолчанию  
[GetErrorDataAsync](M_Tessa_Workflow_IWorkflowService_GetErrorDataAsync.htm)|
Метод для получения данных об ошибке по её ID  
[GetErrorMessageAsync](M_Tessa_Workflow_IWorkflowService_GetErrorMessageAsync.htm)|
Возвращает сообщение об ошибке, указанное в шаблоне процесса  
[GetLockStatusAsync](M_Tessa_Workflow_IWorkflowService_GetLockStatusAsync.htm)|
Получает информацию о блокировке текущей версии Бизнес-процесса и о карточке
Бизнес-процесса в целом (карточка заблокирована, если есть хоть одна
заблокированная карточка)  
[GetModifiedAsync](M_Tessa_Workflow_IWorkflowService_GetModifiedAsync.htm)|
Метод для получения даты изменения версии шаблона процесса  
[GetNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetNodeStateAsync.htm)|
Метод для получения состояния узла по его ID  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetProcessCardIDAsync](M_Tessa_Workflow_IWorkflowService_GetProcessCardIDAsync.htm)|
Метод для получения ID карточки процесса по ID состояния процесса  
[GetProcessCardIDsAsync](M_Tessa_Workflow_IWorkflowService_GetProcessCardIDsAsync.htm)|
Метод для получения списка идентификаторов карточек процессов по ID основной
карточки.  
[GetProcessInstanceIDAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetProcessInstanceIDAsync.htm)|
Метод для получения ID экземпляра процесса по ID экземпляра узла  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetProcessStateAsync.htm)|
Метод для получения экземпляра процесса по его ID  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetProcessVersionTemplateAsync](M_Tessa_Workflow_IWorkflowService_GetProcessVersionTemplateAsync.htm)|
Метод для получения Storage версии процесса.  
[GetSubprocessSubscriptionsAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetSubprocessSubscriptionsAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetTaskSubscriptionsAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetTaskSubscriptionsAsync.htm)|
Метод для получения списка подписок по заданию процесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[GetTimerSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetTimerSubscriptionAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[ResumeProcessAsync](M_Tessa_Workflow_IWorkflowService_ResumeProcessAsync.htm)|
Метод для возобновления процесса по ошибке.  
[SetIsDefaultAsync](M_Tessa_Workflow_IWorkflowService_SetIsDefaultAsync.htm)|
Метод для установки процесса по умолчанию.  
[StoreCommandSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreCommandSubscriptionAsync.htm)|
Метод для сохранения подписки команды  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[StoreNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreNodeStateAsync.htm)|
Метод для сохранения состояния узла  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[StoreProcessAndNodesStatesAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreProcessAndNodesStatesAsync.htm)|
Метод для сохранения состояния процесса и состояний узлов  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[StoreProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreProcessStateAsync.htm)|
Метод для сохранения состояния процесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[StoreSubprocessSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreSubprocessSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[StoreTaskSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreTaskSubscriptionAsync.htm)|
Метод для сохранения подписки задания  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[StoreTimerSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreTimerSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
(Унаследован от
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm))  
[TryLockVersionAsync](M_Tessa_Workflow_IWorkflowService_TryLockVersionAsync.htm)|
Метод для установки блокировки на версию процесса  
[TryUnlockVersionAsync](M_Tessa_Workflow_IWorkflowService_TryUnlockVersionAsync.htm)|
Метод для снятия блокировки с версии процесса  
[ValidateObjectAsync](M_Tessa_Workflow_IWorkflowService_ValidateObjectAsync.htm)|
Метод для валидации переданного объекта  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
