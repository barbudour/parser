# StageTypeHandlerContext - класс
Контекст обработчика этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StageTypeHandlerContext : IStageTypeHandlerContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class StageTypeHandlerContext
    	Implements IStageTypeHandlerContext, IExtensionContext
C++ __Копировать
     public ref class StageTypeHandlerContext sealed : IStageTypeHandlerContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type StageTypeHandlerContext = 
        class
            interface IStageTypeHandlerContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StageTypeHandlerContext
Implements
    [IStageTypeHandlerContext](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandlerContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[StageTypeHandlerContext(IKrProcessRunnerContext, Stage, KrProcessRunnerMode,
Nullable<DirectionAfterInterrupt>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext__ctor_1.htm)|
Инициализирует новый экземпляр класса StageTypeHandlerContext  
---|---  
[StageTypeHandlerContext(Nullable<Guid>, CardType, Nullable<Guid>,
Nullable<KrComponents>, Card, Card, ICardExtensionContext,
IValidationResultBuilder, Stage, WorkflowProcess, ProcessHolder,
IWorkflowProcessInfo, IWorkflowAPIBridge, IKrTaskHistoryResolver,
KrProcessRunnerMode, KrProcessRunnerInitiationCause, IKrProcessButton,
IMainCardAccessStrategy, Nullable<DirectionAfterInterrupt>, String,
Nullable<Guid>,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext__ctor.htm)|
Инициализирует новый экземпляр класса StageTypeHandlerContext  
##  __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_CardExtensionContext.htm)|
Контекст расширения, в рамках которого выполняется Kr процесс.  
[ContextualSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_ContextualSatellite.htm)|
Текущий контекстуальный сателлит.  
[DirectionAfterInterrupt](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_DirectionAfterInterrupt.htm)|
Направление дальнейшего движения процесса после прерывания. Актуально только
для обработки прерывания.  
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_InitiationCause.htm)|
Причина, по которой был вызван раннер: запуск процесса, завершение задания,
обработка сигнала и др.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_KrComponents.htm)|
Включенные компоненты типового решения для текущей карточки.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[MainCardDocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_MainCardDocTypeID.htm)|
Тип документа основной карточки. null, если процесс запущен вне карточки.  
[MainCardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_MainCardID.htm)|
ID основной карточки. null, если процесс запущен вне карточки.  
[MainCardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_MainCardType.htm)|
Тип основной карточки или null, если процесс запущен вне карточки.  
[NotMessageHasNoActiveStages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_NotMessageHasNoActiveStages.htm)|
Возвращает значение, показывающее, что при отсутствии этапов, доступных для
выполнения, не должно отображаться сообщение.  
[ParentProcessID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_ParentProcessID.htm)|
Идентификатор родительского процесса, если есть.  
[ParentProcessTypeName](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_ParentProcessTypeName.htm)|
Тип родительского процесса, если есть.  
[ProcessHolder](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_ProcessHolder.htm)|
Холдер текущих процессов.  
[ProcessHolderSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_ProcessHolderSatellite.htm)|
Текущий сателлит процесса.  
[ProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_ProcessInfo.htm)|
Информация по процессу WorkfowAPI.  
[RunnerMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_RunnerMode.htm)|
Режим раннера, запустившего обработку этапа.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_SecondaryProcess.htm)|
Кнопка, по которой запущен процесс.  
[SignalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_SignalInfo.htm)|
Информация по сигналу WorkflowAPI.  
[Stage](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_Stage.htm)|
Текущий этап процесса.  
[TaskHistoryResolver](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_TaskHistoryResolver.htm)|
Объект для получения групп истории заданий или null, если в текущем контексте
работа с историей заданий не поддерживается.  
[TaskInfo](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_TaskInfo.htm)|
Информация по заданию WorkflowAPI  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_ValidationResult.htm)|
Результат валидации.  
[WorkflowAPI](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_WorkflowAPI.htm)|
Интерфейс для обращения к WorkflowAPI null, если процесс запущен вне
WorkflowAPI.  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerContext_WorkflowProcess.htm)|
Процесс.  
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
##  __Методы расширения
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
