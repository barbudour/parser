# IWorkflowInstanceService - интерфейс
Сервис для управления экземплярами и подписками Бизнес-процесса
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowInstanceService
VB __Копировать
     Public Interface IWorkflowInstanceService
C++ __Копировать
     public interface class IWorkflowInstanceService
F# __Копировать
     type IWorkflowInstanceService = interface end
##  __Методы
[CreateNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_CreateNodeStateAsync.htm)|
Метод для создания состояния узла по объеккту узла шаблона процесса  
---|---  
[CreateProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_CreateProcessStateAsync.htm)|
Метод для создания экземпляра процесса по его шаблону  
[DeleteCommandSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteCommandSubscriptionAsync.htm)|
Метод для удаления подписки команды  
[DeleteNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteNodeStateAsync.htm)|
Метод для удаления состояния узла. Вмсесте с состоянием узла удаляются все его
подписки  
[DeleteProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteProcessStateAsync.htm)|
Метод для удаления состояния процесса  
[DeleteSubprocessSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteSubprocessSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
[DeleteTaskSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteTaskSubscriptionAsync.htm)|
Метод для удаления подписки  
[DeleteTimerSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_DeleteTimerSubscriptionAsync.htm)|
Метод для удаления подписки подпроцесса  
[GetAllNodeStatesAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetAllNodeStatesAsync.htm)|
Метод для получения всех состояний узла по ID экземпляра процесса  
[GetCommandSubscriptionsAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetCommandSubscriptionsAsync.htm)|
Метод для получения списка подписок команды  
[GetNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetNodeStateAsync.htm)|
Метод для получения состояния узла по его ID  
[GetProcessInstanceIDAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetProcessInstanceIDAsync.htm)|
Метод для получения ID экземпляра процесса по ID экземпляра узла  
[GetProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetProcessStateAsync.htm)|
Метод для получения экземпляра процесса по его ID  
[GetSubprocessSubscriptionsAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetSubprocessSubscriptionsAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
[GetTaskSubscriptionsAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetTaskSubscriptionsAsync.htm)|
Метод для получения списка подписок по заданию процесса  
[GetTimerSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_GetTimerSubscriptionAsync.htm)|
Метод для получения списка подписок по ID подпроцесса  
[StoreCommandSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreCommandSubscriptionAsync.htm)|
Метод для сохранения подписки команды  
[StoreNodeStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreNodeStateAsync.htm)|
Метод для сохранения состояния узла  
[StoreProcessAndNodesStatesAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreProcessAndNodesStatesAsync.htm)|
Метод для сохранения состояния процесса и состояний узлов  
[StoreProcessStateAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreProcessStateAsync.htm)|
Метод для сохранения состояния процесса  
[StoreSubprocessSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreSubprocessSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
[StoreTaskSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreTaskSubscriptionAsync.htm)|
Метод для сохранения подписки задания  
[StoreTimerSubscriptionAsync](M_Tessa_Workflow_IWorkflowInstanceService_StoreTimerSubscriptionAsync.htm)|
Метод для сохранения подписки подпроцесса  
## __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
