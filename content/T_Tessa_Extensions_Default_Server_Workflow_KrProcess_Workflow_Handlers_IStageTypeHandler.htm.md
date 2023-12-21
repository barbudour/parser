# IStageTypeHandler - интерфейс
Описывает обработчик этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStageTypeHandler
VB __Копировать
     Public Interface IStageTypeHandler
C++ __Копировать
     public interface class IStageTypeHandler
F# __Копировать
     type IStageTypeHandler = interface end
##  __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
[HandleResurrectionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_HandleResurrectionAsync.htm)|
Обработка восстановления процесса.  
[HandleSignalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_HandleSignalAsync.htm)|
Обработка сигнала.  
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
