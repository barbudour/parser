# IKrProcessRunnerContext - интерфейс
Контекст
[IKrProcessRunner](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunner.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessRunnerContext : IExtensionContext
VB __Копировать
     Public Interface IKrProcessRunnerContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrProcessRunnerContext : IExtensionContext
F# __Копировать
     type IKrProcessRunnerContext = 
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
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_CardContext.htm)|
Контекст расширения на карточке. Может иметь значение по умолчанию для типа.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_CardID.htm)|
Идентификатор карточки.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_CardType.htm)|
Тип карточки.  
[ContextualSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ContextualSatellite.htm)|
Текущий контекстуальный сателлит.  
[DefaultPreparingGroupStrategyFunc](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_DefaultPreparingGroupStrategyFunc.htm)|
Фабрика для получения стандартных стратегий подготовки группы для пересчета.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_DocTypeID.htm)|
Идентификатор типа документа.  
[ExecutionUnitCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ExecutionUnitCache.htm)|
Кэш единиц исполнения в рамках одного выполнения Runner-а.  
[IgnoreGroupScripts](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_IgnoreGroupScripts.htm)|
Игнорировать скрипты групп и частичный пересчет.  
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_InitiationCause.htm)|
Причина запуска процесса. Складывается на основе информации в контексте.  
[IsProcessHolderCreated](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_IsProcessHolderCreated.htm)|
Возвращает значение, показывающее, что текущий процесс создал холдер
сателлита.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_KrComponents.htm)|
Включенные компоненты типового решения для текущей карточки.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
[ParentProcessID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ParentProcessID.htm)|
Идентификатор родительского процесса, если есть.  
[ParentProcessTypeName](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ParentProcessTypeName.htm)|
Тип родительского процесса, если есть.  
[PreparingGroupStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_PreparingGroupStrategy.htm)|
Стратегия для формирования данных, необходимых для пересчета.  
[ProcessHolder](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ProcessHolder.htm)|
Возвращает объект содержащий информацию по текущему процессу.  
[ProcessHolderSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ProcessHolderSatellite.htm)|
Текущий сателлит процесса. Имеет значение по умолчанию для типа, если процесс
выполняется в памяти.  
[ProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ProcessInfo.htm)|
Информация по запущенному процессу. Если
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_InitiationCause.htm)
равно
[InMemoryLaunching](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerInitiationCause.htm),
то возвращает значение null.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_SecondaryProcess.htm)|
Конфигурация вторичного процесса. Может иметь значение по умолчанию для типа.  
[SignalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_SignalInfo.htm)|
Информация по сигналу поступившему в процесс. Если
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_InitiationCause.htm)
не равно
[Signal](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerInitiationCause.htm),
то возвращает значение null.  
[SkippedGroupsByCondition](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_SkippedGroupsByCondition.htm)|
Список групп, которые в процессе текущего выполнения были пропущены по условию
скрипта.  
[SkippedStagesByCondition](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_SkippedStagesByCondition.htm)|
Список этапов, которые в процессе текущего выполнения были пропущены по
условию скрипта.  
[TaskHistoryResolver](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_TaskHistoryResolver.htm)|
Объект для работы с группами истории заданий. Может принимать null, если
отсутствует возможность управления группами истории заданий.  
[TaskInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_TaskInfo.htm)|
Информация по заданию в процессе. Если
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_InitiationCause.htm)
не равно
[CompleteTask](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerInitiationCause.htm),
то возвращает значение null.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_ValidationResult.htm)|
Результат валидации.  
[WorkflowAPI](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_WorkflowAPI.htm)|
Мост до WorkflowAPI  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_WorkflowProcess.htm)|
Контекст выполнения процесса.  
## __Методы
[UpdateCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_UpdateCardAsync.htm)|
Обновляет карточки содержащие информацию о процессе по данным содержащимся в
текущем объекте.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
