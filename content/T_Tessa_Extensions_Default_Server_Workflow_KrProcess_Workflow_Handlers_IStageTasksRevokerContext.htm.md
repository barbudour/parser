# IStageTasksRevokerContext - интерфейс
Описывает контекст
[IStageTasksRevoker](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevoker.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStageTasksRevokerContext : IExtensionContext
VB __Копировать
     Public Interface IStageTasksRevokerContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IStageTasksRevokerContext : IExtensionContext
F# __Копировать
     type IStageTasksRevokerContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_CardID.htm)|
Идентификатор карточки.  
[Context](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_Context.htm)|
Контекст обработчика этапа.  
[OptionID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_OptionID.htm)|
Опционально указывается вариант завершения. Если не указан, то все задания
отзываются с вариантом завершения
[Cancel](F_Tessa_Extensions_Default_Shared_DefaultCompletionOptions_Cancel.htm)  
[RemoveFromActive](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_RemoveFromActive.htm)|
Удалить задание из активных.  
[TaskID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_TaskID.htm)|
Идентификатор задания для отзыва, если отзывается только одно задание.  
[TaskIDs](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_TaskIDs.htm)|
Список идентификаторов заданий для отзыва  
[TaskModificationAction](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext_TaskModificationAction.htm)|
Действие перед завершением задания.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
