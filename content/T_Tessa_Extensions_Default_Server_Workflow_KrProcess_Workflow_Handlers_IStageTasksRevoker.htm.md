# IStageTasksRevoker - интерфейс
Описывает объект выполняющий отзыв заданий этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStageTasksRevoker
VB __Копировать
     Public Interface IStageTasksRevoker
C++ __Копировать
     public interface class IStageTasksRevoker
F# __Копировать
     type IStageTasksRevoker = interface end
##  __Методы
[RevokeAllStageTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevoker_RevokeAllStageTasksAsync.htm)|
Отзывает все задания этапа.  
---|---  
[RevokeTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevoker_RevokeTaskAsync.htm)|
Отзывает задание идентификатор которого указан в свойстве
[TaskID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_TaskID.htm).  
[RevokeTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevoker_RevokeTasksAsync.htm)|
Отзывает все задания идентификаторы которых указаны в свойстве
[TaskIDs](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_TaskIDs.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
