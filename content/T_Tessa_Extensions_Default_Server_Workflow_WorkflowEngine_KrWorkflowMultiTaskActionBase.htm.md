# KrWorkflowMultiTaskActionBase - класс
Базовый класс для обработчиков действий отправляющих несколько заданий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrWorkflowMultiTaskActionBase : KrWorkflowTaskActionBase
VB __Копировать
     Public MustInherit Class KrWorkflowMultiTaskActionBase
    	Inherits KrWorkflowTaskActionBase
C++ __Копировать
     public ref class KrWorkflowMultiTaskActionBase abstract : public KrWorkflowTaskActionBase
F# __Копировать
     [<AbstractClassAttribute>]
    type KrWorkflowMultiTaskActionBase = 
        class
            inherit KrWorkflowTaskActionBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm) __[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm) __[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm) __ KrWorkflowMultiTaskActionBase
Derived
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.KrApprovalAction](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrApprovalAction.htm)
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine.KrSigningAction](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrSigningAction.htm)
##  __Конструкторы
[KrWorkflowMultiTaskActionBase](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowMultiTaskActionBase__ctor.htm)|
Инициализирует новый экземпляр класса KrWorkflowMultiTaskActionBase  
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
[AddNewProcessingTaskID](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowMultiTaskActionBase_AddNewProcessingTaskID.htm)|
Добавляет указанный идентификатор задания в список обрабатываемых заданий
данным экземпляром действия.  
---|---  
[AddTaskHistoryAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_AddTaskHistoryAsync.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[AddTaskHistoryByTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_AddTaskHistoryByTaskAsync.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[AddTaskToNextContextTasks](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_AddTaskToNextContextTasks.htm)|
Устанавливает задание в список обрабатываемых заданий
[Tasks](P_Tessa_Workflow_IWorkflowEngineContext_Tasks.htm) для последующих
узлов и действий.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CheckActive](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowMultiTaskActionBase_CheckActive.htm)|
Метод для проверки факта, что действие активно и должно сохранить свое
состояние вместе с состоянием своего узла.  
(Переопределяет
[WorkflowActionBase.CheckActive(IWorkflowEngineContext)](M_Tessa_Workflow_Actions_WorkflowActionBase_CheckActive.htm))  
[Compile](M_Tessa_Workflow_Actions_WorkflowActionBase_Compile.htm)|  Метод для
компиляции данного действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[CompileEvents](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompileEvents.htm)|
Компилирует методы - обработчики событий.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CompleteSubtasksAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompleteSubtasksAsync.htm)|
Завершает дочерние задания указанных типов.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CompleteTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompleteTaskAsync.htm)|
Обрабатывает завершения задания.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CompleteTaskCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CompleteTaskCoreAsync.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CreateDialogsAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateDialogsAsync.htm)|
Инициализирует карточку диалога.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CreateDigestAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateDigestAsync.htm)|
Создаёт дайджест задания на основе дайджеста указанного в настройках действия,
комментария инициатора процесса согласования и дополнительного комментария.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CreateSubscription](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateSubscription.htm)|
Создаёт подписку на сигнал signalType для текущего действия.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[CreateTasksContext](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_CreateTasksContext.htm)|
Создаёт контекст работы с заданиями. Контекст нужен для сохранения измененных
действием заданий и записью их в
[Tasks](P_Tessa_Workflow_IWorkflowEngineContext_Tasks.htm).  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[DelegateTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DelegateTaskAsync.htm)|
Делегирует задание другому пользователю.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[DelegateTaskCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DelegateTaskCoreAsync.htm)|
Делегирует задание другому пользователю.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[DeleteTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DeleteTaskAsync.htm)|
Удаляет задание и его историю.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[DeleteTaskCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_DeleteTaskCoreAsync.htm)|
Удаляет указанное задание.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
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
[GetProcessingTaskIDList](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowMultiTaskActionBase_GetProcessingTaskIDList.htm)|
Возвращает список идентификаторов заданий обрабатываемых данным экземпляром
действия.  
[GetResultAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_GetResultAsync.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[GetSqlPerformers](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_GetSqlPerformers.htm)|
Возвращает коллекцию содержащую список SQL исполнителей.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetWithPlaceholdersAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_GetWithPlaceholdersAsync.htm)|
Возвращает текст с учетом плейсхолдеров.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PerformEvent](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_PerformEvent.htm)|
Обрабатывает событие.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[PrepareForExecute](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_PrepareForExecute.htm)|
Метод производит манипуляции с actionState после его создания.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[PrepareForSaveTemplate](M_Tessa_Workflow_Actions_WorkflowActionBase_PrepareForSaveTemplate.htm)|
Метод подготовки действия для сохранения.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[ProcessAsync](M_Tessa_Workflow_Actions_WorkflowActionBase_ProcessAsync.htm)|
Метод, вызываемый при запуске действия.  
(Унаследован от
[WorkflowActionBase](T_Tessa_Workflow_Actions_WorkflowActionBase.htm))  
[ProcessDialogAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_ProcessDialogAsync.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[RequestCommentTaskCompleteAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_RequestCommentTaskCompleteAsync.htm)|
Обрабатывает завершение заданий типа
[KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm).  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[SendCompleteActionNotificationAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendCompleteActionNotificationAsync.htm)|
Асинхронно отправляет уведомление о завершении действия.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[SendCompleteTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask,
WorkflowTaskNotificationInfo)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendCompleteTaskNotificationAsync.htm)|
Асинхронно отправляет уведомление о завершении задания.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[SendCompleteTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask, WorkflowTaskNotificationInfoBase, String,
WorkflowActionMethodDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendCompleteTaskNotificationAsync_1.htm)|
Асинхронно отправляет уведомление о завершении задания.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[SendRequestCommentTaskAsync(IWorkflowEngineContext, IRoleRepository,
CardTask)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendRequestCommentTaskAsync_1.htm)|
Асинхронно создаёт задание запроса комментария
([KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm)).
При создании задания используются данные родительского задания, в том числе
значения из секции
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrCommentators_Name.htm).  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[SendRequestCommentTaskAsync(IWorkflowEngineContext, Guid, Guid, String,
Nullable<DateTime>, Nullable<Int32>, Guid, String,
String)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendRequestCommentTaskAsync.htm)|
Асинхронно создаёт задание запроса комментария
([KrRequestCommentTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrRequestCommentTypeID.htm)).  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[SendStartTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask, String,
WorkflowActionMethodDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendStartTaskNotificationAsync_1.htm)|
Отправляет уведомления о запуске задания. Параметры считываются из секции с
именем sectionName.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[SendStartTaskNotificationAsync(IWorkflowEngineContext,
IWorkflowEngineCompiled, CardTask, Nullable<Guid>, Boolean, Boolean,
WorkflowActionMethodDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_SendStartTaskNotificationAsync.htm)|
Отправляет уведомления о запуске задания.  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
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
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
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
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
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
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[cardRepository](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_cardRepository.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[cardsScope](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_cardsScope.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[configurationInfoProvider](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_configurationInfoProvider.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[ctcBuilderFactory](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_ctcBuilderFactory.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[notificationManager](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_notificationManager.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[ProcessingTaskIDListParamKey](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowMultiTaskActionBase_ProcessingTaskIDListParamKey.htm)|
Имя ключа, по которому в параметрах действия содержится список идентификаторов
обрабатываемых заданий данным экземпляром действия. Тип значения:
[List<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1),
где T - [Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[requestExtender](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase_requestExtender.htm)|  
(Унаследован от
[KrWorkflowActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowActionBase.htm))  
[serverPermissionsProvider](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_serverPermissionsProvider.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
[signatureProvider](F_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase_signatureProvider.htm)|  
(Унаследован от
[KrWorkflowTaskActionBase](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_KrWorkflowTaskActionBase.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine.htm)
