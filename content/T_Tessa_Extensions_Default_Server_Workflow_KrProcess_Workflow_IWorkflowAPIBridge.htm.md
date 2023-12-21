# IWorkflowAPIBridge - интерфейс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowAPIBridge
VB __Копировать
     Public Interface IWorkflowAPIBridge
C++ __Копировать
     public interface class IWorkflowAPIBridge
F# __Копировать
     type IWorkflowAPIBridge = interface end
##  __Свойства
[NextRequest](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_NextRequest.htm)|
Возвращает запрос на следующее сохранение.  
---|---  
[NextRequestPending](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_NextRequestPending.htm)|
Возвращает флаг, показывающий, необходимо ли выполнить следующее сохранение.  
[ProcessesAwaitingRemoval](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_ProcessesAwaitingRemoval.htm)|
Возвращает список процессов, ожидающих завершения.  
## __Методы
[AddActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_AddActiveTaskAsync.htm)|
Добавляет задание с указанным идентификатором в список активных.  
---|---  
[DecrementCounterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_DecrementCounterAsync.htm)|
Уменьшает текущее значение счётчика на заданное значение decrementValue. Если
текущее значение становится не больше нуля, то счётчик удаляется.  
[GetActiveTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_GetActiveTasksAsync.htm)|
Возвращает список идентификаторов активных заданий.  
[InitCounterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_InitCounterAsync.htm)|
Инициализирует счётчик с заданным номером с указанием начального значения.  
[NotifyNextRequestPending](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_NotifyNextRequestPending.htm)|
Уведомляет WorkflowAPI о необходимости выполнения следующего сохранения.  
[RemoveActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_RemoveActiveTaskAsync.htm)|
Удяляет задание с указанным идентификатором из списка активных. В случае
неудачи будет выброшено исключение  
[RemoveCounterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_RemoveCounterAsync.htm)|
Удаляет счётчик с заданным номером, уникальным для подпроцесса.  
[SendTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_SendTaskAsync.htm)|
Отправляет задание.  
[TryRemoveActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge_TryRemoveActiveTaskAsync.htm)|
Удаляет задание с указанным идентификатором из списка активных.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
