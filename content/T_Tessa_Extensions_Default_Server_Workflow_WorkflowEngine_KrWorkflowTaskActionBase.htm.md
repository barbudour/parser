# KrWorkflowTaskActionBase - класс
Базовый класс для обработчиков действий маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrWorkflowTaskActionBase : KrWorkflowActionBase
VB __Копировать
     Public MustInherit Class KrWorkflowTaskActionBase
    	Inherits KrWorkflowActionBase
C++ __Копировать
     public ref class KrWorkflowTaskActionBase abstract : public KrWorkflowActionBase
F# __Копировать
     [<AbstractClassAttribute>]
    type KrWorkflowTaskActionBase = 
        class
            inherit KrWorkflowActionBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm) __[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm) __ KrWorkflowTaskActionBase
Derived
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.KrAmendingAction](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrAmendingAction.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.KrResolutionAction](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrResolutionAction.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.KrTaskRegistrationAction](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrTaskRegistrationAction.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.KrUniversalTaskAction](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrUniversalTaskAction.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.KrWorkflowMultiTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowMultiTaskActionBase.htm)
##  __Конструкторы
[KrWorkflowTaskActionBase](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase__ctor.htm)|
Инициализирует новый экземпляр класса KrWorkflowTaskActionBase  
---|---  
##  __Свойства
[Descriptor](P_Tessa_Workflow_Actions_WorkflowActionBase_Descriptor.htm)|
Дескриптор действия. По умолчанию используется дескриптор, переданный в
конструкторе действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
---|---  
[ID](P_Tessa_Workflow_Actions_WorkflowActionBase_ID.htm)|  ID типа карточки,
он же ID в реестре
[IWorkflowActionRegistry](T_Tessa_Workflow_Actions_IWorkflowActionRegistry.htm).  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[IsStandAlone](P_Tessa_Workflow_Actions_WorkflowActionBase_IsStandAlone.htm)|
Флаг, обозначающий, что данное действие может быть только единственным
действием в узле.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
##  __Методы
[AddTaskHistoryAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_AddTaskHistoryAsync.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
---|---  
[AddTaskHistoryByTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_AddTaskHistoryByTaskAsync.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[AddTaskToNextContextTasks](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_AddTaskToNextContextTasks.htm)|
Устанавливает задание в список обрабатываемых заданий
[Tasks](P_Tessa_Workflow_IWorkflowEngineContext_Tasks.htm) для последующих
узлов и действий.  
[CheckActive](M_Tessa_Workflow_Actions_WorkflowActionBase_CheckActive.htm)|
Метод для проверки факта, что действие активно и должно сохранить свое
состояние вместе с состояним своего узла.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[Compile](M_Tessa_Workflow_Actions_WorkflowActionBase_Compile.htm)|  Метод для
компиляции данного действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[CompileEvents](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompileEvents.htm)|
Компилирует методы - обработчики событий.  
[CompleteSubtasksAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompleteSubtasksAsync.htm)|
Завершает дочерние задания указанных типов.  
[CompleteTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompleteTaskAsync.htm)|
Обрабатывает завершения задания.  
[CompleteTaskCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompleteTaskCoreAsync.htm)|  
[CreateDialogsAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateDialogsAsync.htm)|
Инициализирует карточку диалога.  
[CreateDigestAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateDigestAsync.htm)|
Создаёт дайджест задания на основе дайджеста указанного в настройках действия,
комментария инициатора процесса согласования и дополнительного комментария.  
[CreateSubscription](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateSubscription.htm)|
Создаёт подписку на сигнал signalType для текущего действия.  
[CreateTasksContext](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateTasksContext.htm)|
Создаёт контекст работы с заданиями. Контекст нужен для сохранения измененных
действием заданий и записью их в
[Tasks](P_Tessa_Workflow_IWorkflowEngineContext_Tasks.htm).  
[DelegateTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DelegateTaskAsync.htm)|
Делегирует задание другому пользователю.  
[DelegateTaskCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DelegateTaskCoreAsync.htm)|
Делегирует задание другому пользователю.  
[DeleteTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DeleteTaskAsync.htm)|
Удаляет задание и его историю.  
[DeleteTaskCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DeleteTaskCoreAsync.htm)|
Удаляет указанное задание.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_ExecuteAsync.htm)|
Метод, вызываемый при непосредственно исполнения самого действия.  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetResultAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_GetResultAsync.htm)|  
[GetSqlPerformers](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_GetSqlPerformers.htm)|
Возвращает коллекцию содержащую список SQL исполнителей.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetWithPlaceholdersAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_GetWithPlaceholdersAsync.htm)|
Возвращает текст с учетом плейсхолдеров.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PerformEvent](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_PerformEvent.htm)|
Обрабатывает событие.  
[PrepareForExecute](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_PrepareForExecute.htm)|
Метод производит манипуляции с actionState после его создания.  
(Переопределяет
[WorkflowActionBase.PrepareForExecute(WorkflowActionStateStorage,
IWorkflowEngineContext)](M_Tessa_Workflow_Actions_WorkflowActionBase_PrepareForExecute.htm))  
[PrepareForSaveTemplate](M_Tessa_Workflow_Actions_WorkflowActionBase_PrepareForSaveTemplate.htm)|
Метод подготовки действия для сохранения.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[ProcessAsync](M_Tessa_Workflow_Actions_WorkflowActionBase_ProcessAsync.htm)|
Метод, вызываемый при запуске действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[ProcessDialogAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_ProcessDialogAsync.htm)|  
[RequestCommentTaskCompleteAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_RequestCommentTaskCompleteAsync.htm)|
Обрабатывает завершение заданий типа
[KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm).  
[SendCompleteActionNotificationAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendCompleteActionNotificationAsync.htm)|
Асинхронно отправляет уведомление о завершении действия.  
[SendCompleteTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask,
WorkflowTaskNotificationInfo)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendCompleteTaskNotificationAsync.htm)|
Асинхронно отправляет уведомление о завершении задания.  
[SendCompleteTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask, WorkflowTaskNotificationInfoBase, String,
WorkflowActionMethodDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendCompleteTaskNotificationAsync_1.htm)|
Асинхронно отправляет уведомление о завершении задания.  
[SendRequestCommentTaskAsync(IWorkflowEngineContext, IRoleRepository,
CardTask)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendRequestCommentTaskAsync_1.htm)|
Асинхронно создаёт задание запроса комментария
([KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm)).
При создании задания используются данные родительского задания, в том числе
значения из секции
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrCommentators_Name.htm).  
[SendRequestCommentTaskAsync(IWorkflowEngineContext, Guid, Guid, String,
Nullable<DateTime>, Nullable<Int32>, Guid, String,
String)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendRequestCommentTaskAsync.htm)|
Асинхронно создаёт задание запроса комментария
([KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm)).  
[SendStartTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask, String,
WorkflowActionMethodDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendStartTaskNotificationAsync_1.htm)|
Отправляет уведомления о запуске задания. Параметры считываются из секции с
именем sectionName.  
[SendStartTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask, Nullable<Guid>, Boolean, Boolean,
WorkflowActionMethodDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendStartTaskNotificationAsync.htm)|
Отправляет уведомления о запуске задания.  
[SetStateIDAsync(IWorkflowEngineContext, KrState,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_SetStateIDAsync_1.htm)|
Устанавливает состояние карточки.  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[SetStateIDAsync(IWorkflowEngineContext, Int32, String,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_SetStateIDAsync.htm)|
Устанавливает состояние карточки.  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[StorePreviousState](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_StorePreviousState.htm)|
Сохраняет идентификатор предыдущего состояния карточки в параметрах процесса.  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[SubscribeOnEvents](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SubscribeOnEvents.htm)|
Создаёт подписки на обрабатываемые события.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetPreviousState](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_TryGetPreviousState.htm)|
Возвращает идентификатор предыдущего состояния карточки из параметров
процесса.  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[UpdateTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_UpdateTaskAsync.htm)|
Обновляет активное задание.  
[Validate](M_Tessa_Workflow_Actions_WorkflowActionBase_Validate.htm)|  Метод
валидации действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
##  __Поля
[calendarService](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_calendarService.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
---|---  
[cardFileManager](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_cardFileManager.htm)|  
[cardRepository](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_cardRepository.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[cardsScope](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_cardsScope.htm)|  
[configurationInfoProvider](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_configurationInfoProvider.htm)|  
[ctcBuilderFactory](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_ctcBuilderFactory.htm)|  
[DialogsSectionName](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DialogsSectionName.htm)|  
[EventsSectionName](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_EventsSectionName.htm)|  
[notificationManager](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_notificationManager.htm)|  
[NotificationRolesSectionName](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_NotificationRolesSectionName.htm)|  
[requestExtender](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_requestExtender.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[serverPermissionsProvider](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_serverPermissionsProvider.htm)|  
[signatureProvider](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_signatureProvider.htm)|  
[TaskCompleteParams](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_TaskCompleteParams.htm)|  
[TaskParams](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_TaskParams.htm)|  
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
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)
