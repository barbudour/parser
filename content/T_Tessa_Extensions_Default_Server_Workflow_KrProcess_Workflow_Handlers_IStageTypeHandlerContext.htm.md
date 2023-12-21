# IStageTypeHandlerContext - интерфейс
Контекст обработчика этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStageTypeHandlerContext : IExtensionContext
VB __Копировать
     Public Interface IStageTypeHandlerContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IStageTypeHandlerContext : IExtensionContext
F# __Копировать
     type IStageTypeHandlerContext = 
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
[CardExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_CardExtensionContext.htm)|
Контекст расширения, в рамках которого выполняется Kr процесс.  
[ContextualSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_ContextualSatellite.htm)|
Текущий контекстуальный сателлит.  
[DirectionAfterInterrupt](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_DirectionAfterInterrupt.htm)|
Направление дальнейшего движения процесса после прерывания. Актуально только
для обработки прерывания.  
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_InitiationCause.htm)|
Причина, по которой был вызван раннер: запуск процесса, завершение задания,
обработка сигнала и др.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_KrComponents.htm)|
Включенные компоненты типового решения для текущей карточки.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[MainCardDocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_MainCardDocTypeID.htm)|
Тип документа основной карточки. null, если процесс запущен вне карточки.  
[MainCardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_MainCardID.htm)|
ID основной карточки. null, если процесс запущен вне карточки.  
[MainCardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_MainCardType.htm)|
Тип основной карточки или null, если процесс запущен вне карточки.  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
[ParentProcessID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_ParentProcessID.htm)|
Идентификатор родительского процесса, если есть.  
[ParentProcessTypeName](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_ParentProcessTypeName.htm)|
Тип родительского процесса, если есть.  
[ProcessHolder](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_ProcessHolder.htm)|
Холдер текущих процессов.  
[ProcessHolderSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_ProcessHolderSatellite.htm)|
Текущий сателлит процесса.  
[ProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_ProcessInfo.htm)|
Информация по процессу WorkfowAPI.  
[RunnerMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_RunnerMode.htm)|
Режим раннера, запустившего обработку этапа.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_SecondaryProcess.htm)|
Кнопка, по которой запущен процесс.  
[SignalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_SignalInfo.htm)|
Информация по сигналу WorkflowAPI.  
[Stage](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_Stage.htm)|
Текущий этап процесса.  
[TaskHistoryResolver](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_TaskHistoryResolver.htm)|
Объект для получения групп истории заданий или null, если в текущем контексте
работа с историей заданий не поддерживается.  
[TaskInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_TaskInfo.htm)|
Информация по заданию WorkflowAPI  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_ValidationResult.htm)|
Результат валидации.  
[WorkflowAPI](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_WorkflowAPI.htm)|
Интерфейс для обращения к WorkflowAPI null, если процесс запущен вне
WorkflowAPI.  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext_WorkflowProcess.htm)|
Процесс.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
