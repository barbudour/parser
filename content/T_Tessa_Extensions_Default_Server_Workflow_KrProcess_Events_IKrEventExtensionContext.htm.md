# IKrEventExtensionContext - интерфейс
Контекст
[IKrEventManager](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Events](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrEventExtensionContext : IExtensionContext
VB __Копировать
     Public Interface IKrEventExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrEventExtensionContext : IExtensionContext
F# __Копировать
     type IKrEventExtensionContext = 
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
[CardExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_CardExtensionContext.htm)|
Контекст расширения, в рамках которого выполняется Kr процесс.  
[ContextualSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_ContextualSatellite.htm)|
Текущий контекстуальный сателлит.  
[EventType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_EventType.htm)|
Тип события.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_Info.htm)|
Дополнительная неперсистентная информация о событии.  
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_InitiationCause.htm)|
Причина, по которой был вызван раннер: запуск процесса, завершение задания,
обработка сигнала и др.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[MainCardDocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_MainCardDocTypeID.htm)|
Тип документа основной карточки или значение null, если процесс запущен вне
карточки.  
[MainCardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_MainCardID.htm)|
Идентификатор основной карточки или значение null, если процесс запущен вне
карточки.  
[MainCardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_MainCardType.htm)|
Тип основной карточки или значение null, если процесс запущен вне карточки.  
[ProcessHolder](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_ProcessHolder.htm)|
Холдер текущего процесса.  
[ProcessHolderSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_ProcessHolderSatellite.htm)|
Текущий сателлит процесса.  
[ProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_ProcessInfo.htm)|
Информация по процессу WorkflowAPI.  
[RunnerMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_RunnerMode.htm)|
Режим раннера, запустившего обработку этапа.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_SecondaryProcess.htm)|
Вторичный процесс.  
[SignalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_SignalInfo.htm)|
Информация по сигналу WorkflowAPI.  
[Stage](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_Stage.htm)|
Текущий этап процесса.  
[TaskInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_TaskInfo.htm)|
Информация по заданию WorkflowAPI.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_ValidationResult.htm)|
Результат валидации.  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_IKrEventExtensionContext_WorkflowProcess.htm)|
Процесс.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Events - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events.htm)
