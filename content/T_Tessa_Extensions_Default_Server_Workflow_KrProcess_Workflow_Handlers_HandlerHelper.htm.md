# HandlerHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class HandlerHelper
VB __Копировать
     Public NotInheritable Class HandlerHelper
C++ __Копировать
     public ref class HandlerHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type HandlerHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ HandlerHelper
##  __Методы
[AppendToCompletedTasks](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_AppendToCompletedTasks.htm)|
Добавляет информацию о завершённом задании в список завершённых заданий этапа.  
---|---  
[AppendToCompletedTasksWithPreparing](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_AppendToCompletedTasksWithPreparing.htm)|
Добавляет информацию о завершённом задании в список завершённых заданий этапа
предварительно выполнив подготовку в соответствии со значением свойства этапа
[WriteTaskFullInformation](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_WriteTaskFullInformation.htm).  
[ClearCompletedTasks](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_ClearCompletedTasks.htm)|
Удаляет список завершённых заданий этапа из указанного этапа.  
[GetStageAuthorAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_GetStageAuthorAsync.htm)|
Возвращает автора текущего этапа.  
[GetTaskHistoryGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_GetTaskHistoryGroupAsync.htm)|
Возвращает идентификатор текущей группы истории заданий.  
[GetTaskKind](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_GetTaskKind.htm)|  
[InitScriptContextAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_InitScriptContextAsync.htm)|
Инициализирует указанный объект информацией содержащейся в контексте
обработчика этапа.  
[RemoveTaskHistoryGroupOverride](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_RemoveTaskHistoryGroupOverride.htm)|
Удаляет из
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
информацию о ранее определённом идентификаторе текущей группы истории заданий.  
[SetTaskKind](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_SetTaskKind.htm)|  
[SetTaskResultAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_SetTaskResultAsync.htm)|  
[TryGetOverridenTaskHistoryGroup](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HandlerHelper_TryGetOverridenTaskHistoryGroup.htm)|
Возвращает идентификатор текущей группы истории заданий из
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
указанного этапа.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
