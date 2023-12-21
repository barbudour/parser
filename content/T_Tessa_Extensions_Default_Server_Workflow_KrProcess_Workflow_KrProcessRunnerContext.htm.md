# KrProcessRunnerContext - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrProcessRunnerContext : IKrProcessRunnerContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class KrProcessRunnerContext
    	Implements IKrProcessRunnerContext, IExtensionContext
C++ __Копировать
     public ref class KrProcessRunnerContext sealed : IKrProcessRunnerContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type KrProcessRunnerContext = 
        class
            interface IKrProcessRunnerContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessRunnerContext
Implements
    [IKrProcessRunnerContext](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrProcessRunnerContext](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext__ctor.htm)|
Инициализирует новый экземпляр класса KrProcessRunnerContext  
---|---  
##  __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_CardContext.htm)|
Контекст расширения на карточке. Может иметь значение по умолчанию для типа.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_CardID.htm)|
Идентификатор карточки.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_CardType.htm)|
Тип карточки.  
[ContextualSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ContextualSatellite.htm)|
Текущий контекстуальный сателлит.  
[DefaultPreparingGroupStrategyFunc](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_DefaultPreparingGroupStrategyFunc.htm)|
Фабрика для получения стандартных стратегий подготовки группы для пересчета.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_DocTypeID.htm)|
Идентификатор типа документа.  
[ExecutionUnitCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ExecutionUnitCache.htm)|
Кэш единиц исполнения в рамках одного выполнения Runner-а.  
[IgnoreGroupScripts](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_IgnoreGroupScripts.htm)|
Игнорировать скрипты групп и частичный пересчет.  
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_InitiationCause.htm)|
Причина запуска процесса. Складывается на основе информации в контексте.  
[IsProcessHolderCreated](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_IsProcessHolderCreated.htm)|
Возвращает значение, показывающее, что текущий процесс создал холдер
сателлита.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_KrComponents.htm)|
Включенные компоненты типового решения для текущей карточки.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
[ParentProcessID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ParentProcessID.htm)|
Идентификатор родительского процесса, если есть.  
[ParentProcessTypeName](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ParentProcessTypeName.htm)|
Тип родительского процесса, если есть.  
[PreparingGroupStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_PreparingGroupStrategy.htm)|
Стратегия для формирования данных, необходимых для пересчета.  
[ProcessHolder](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ProcessHolder.htm)|
Возвращает объект содержащий информацию по текущему процессу.  
[ProcessHolderSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ProcessHolderSatellite.htm)|
Текущий сателлит процесса. Имеет значение по умолчанию для типа, если процесс
выполняется в памяти.  
[ProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ProcessInfo.htm)|
Информация по запущенному процессу. Если
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_InitiationCause.htm)
равно
[InMemoryLaunching](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerInitiationCause.htm),
то возвращает значение null.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_SecondaryProcess.htm)|
Конфигурация вторичного процесса. Может иметь значение по умолчанию для типа.  
[SignalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_SignalInfo.htm)|
Информация по сигналу поступившему в процесс. Если
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_InitiationCause.htm)
не равно
[Signal](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerInitiationCause.htm),
то возвращает значение null.  
[SkippedGroupsByCondition](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_SkippedGroupsByCondition.htm)|
Список групп, которые в процессе текущего выполнения были пропущены по условию
скрипта.  
[SkippedStagesByCondition](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_SkippedStagesByCondition.htm)|
Список этапов, которые в процессе текущего выполнения были пропущены по
условию скрипта.  
[TaskHistoryResolver](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_TaskHistoryResolver.htm)|
Объект для работы с группами истории заданий. Может принимать null, если
отсутствует возможность управления группами истории заданий.  
[TaskInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_TaskInfo.htm)|
Информация по заданию в процессе. Если
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunnerContext_InitiationCause.htm)
не равно
[CompleteTask](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerInitiationCause.htm),
то возвращает значение null.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_ValidationResult.htm)|
Результат валидации.  
[WorkflowAPI](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_WorkflowAPI.htm)|
Мост до WorkflowAPI  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_WorkflowProcess.htm)|
Контекст выполнения процесса.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerContext_UpdateCardAsync.htm)|
Обновляет карточки содержащие информацию о процессе по данным содержащимся в
текущем объекте.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
