# WfWorkflowStoreExtension - класс
Расширение, выполняющее взаимодействие с бизнес-процессом Workflow при
сохранении карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.Wf](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class WfWorkflowStoreExtension : WorkflowStoreExtension
VB __Копировать
     Public Class WfWorkflowStoreExtension
    	Inherits WorkflowStoreExtension
C++ __Копировать
     public ref class WfWorkflowStoreExtension : public WorkflowStoreExtension
F# __Копировать
     type WfWorkflowStoreExtension = 
        class
            inherit WorkflowStoreExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm) __[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm) __ WfWorkflowStoreExtension
##  __Конструкторы
[WfWorkflowStoreExtension](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension__ctor.htm)|
Инициализирует новый экземпляр класса WfWorkflowStoreExtension  
---|---  
##  __Свойства
[CardGetStrategy](P_Tessa_Cards_Workflow_WorkflowStoreExtension_CardGetStrategy.htm)|
Стратегия, выполняющая низкоуровневую загрузку секций карточки, или null, если
такая загрузка не поддерживается. Обычно требуется для создания групп в
истории заданий совместно с объектом
[TaskHistoryManager](P_Tessa_Cards_Workflow_WorkflowStoreExtension_TaskHistoryManager.htm).  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
---|---  
[CardRepositoryToCreateNextRequest](P_Tessa_Cards_Workflow_WorkflowStoreExtension_CardRepositoryToCreateNextRequest.htm)|
Репозиторий для создания карточки для дополнительного сохранения карточки с
новыми заданиями.  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
[CardRepositoryToCreateTasks](P_Tessa_Cards_Workflow_WorkflowStoreExtension_CardRepositoryToCreateTasks.htm)|
Репозиторий карточек, используемый для создания карточек заданий.  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
[CardRepositoryToStoreNextRequest](P_Tessa_Cards_Workflow_WorkflowStoreExtension_CardRepositoryToStoreNextRequest.htm)|
Репозиторий для дополнительного сохранения карточки с новыми заданиями.  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
[TaskHistoryManager](P_Tessa_Cards_Workflow_WorkflowStoreExtension_TaskHistoryManager.htm)|
Объект, управляющий созданием групп в истории заданий.  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
[WorkflowQueueProcessor](P_Tessa_Cards_Workflow_WorkflowStoreExtension_WorkflowQueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после сохранения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[BeforeCommitTransaction](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_BeforeCommitTransaction.htm)|  
(Переопределяет
[WorkflowStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_BeforeCommitTransaction.htm))  
[BeforeRequest](M_Tessa_Cards_Workflow_WorkflowStoreExtension_BeforeRequest.htm)|
Действие, выполняемое перед сохранением карточки стандартными средствами.
Может установить ответ на запрос для того, чтобы сохранение карточки
стандартными средствами не выполнялось.  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
[CanHandleQueueItemAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CanHandleQueueItemAsync.htm)|  
(Переопределяет
[WorkflowStoreExtension.CanHandleQueueItemAsync(WorkflowQueueItem,
ICardStoreExtensionContext)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CanHandleQueueItemAsync.htm))  
[CanStartProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CanStartProcessAsync.htm)|  
(Переопределяет [WorkflowStoreExtension.CanStartProcessAsync(Nullable<Guid>,
String,
ICardStoreExtensionContext)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CanStartProcessAsync.htm))  
[CanStartResolutionProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CanStartResolutionProcessAsync.htm)|
Возвращает признак того, что бизнес-процесс резолюций может быть запущен.  
[CardIsAllowedAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CardIsAllowedAsync.htm)|  
(Переопределяет [WorkflowStoreExtension.CardIsAllowedAsync(Card,
ICardStoreExtensionContext)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CardIsAllowedAsync.htm))  
[CompleteResolutionAndGetResult](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CompleteResolutionAndGetResult.htm)|
Завершает задание резолюции Workflow и возвращает результат задания или null,
если результат задания не удалось получить.  
[CreateContextAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CreateContextAsync.htm)|  
(Переопределяет
[WorkflowStoreExtension.CreateContextAsync(ICardStoreExtensionContext,
CardStoreRequest)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CreateContextAsync.htm))  
[CreateManagerAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CreateManagerAsync.htm)|  
(Переопределяет [WorkflowStoreExtension.CreateManagerAsync(IWorkflowContext,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CreateManagerAsync.htm))  
[CreateWorkerAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_CreateWorkerAsync.htm)|  
(Переопределяет [WorkflowStoreExtension.CreateWorkerAsync(IWorkflowManager,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CreateWorkerAsync.htm))  
[DeferTaskHistoryRemovalUntilTransaction](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_DeferTaskHistoryRemovalUntilTransaction.htm)|
Добавляет заданный идентификатор в список идентификаторов заданий, записи по
истории которых будут удалены в транзакции на сохранение карточки, если у
таких записей отсутствуют дочерние записи.  
[EnsureSatelliteExistsAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_EnsureSatelliteExistsAsync.htm)|
Проверяет, что в заданном контексте
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm) задан
идентификатор карточки-сателлита Workflow. Если он там отсутствует, то
создаётся и сохраняется сателлит, а затем его идентификатор устанавливается в
контексте. Возвращает признак того, что метод выполнен успешно, и в контексте
действительно присутствует карточка-сателлит.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[HandleUnknownTaskAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_HandleUnknownTaskAsync.htm)|
Выполняет обработку задания, для которого не удалось найти информацию в
бизнес-процессе. Возвращает признак того, что выполнение можно продолжить.
Добавляет ошибку в результат валидации и возвращает false, если выполнение
следует прервать.  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ModifyCompletedTasksBeforeRequestAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_ModifyCompletedTasksBeforeRequestAsync.htm)|  
(Переопределяет
[WorkflowStoreExtension.ModifyCompletedTasksBeforeRequestAsync(List<CardTask>,
ICardStoreExtensionContext)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_ModifyCompletedTasksBeforeRequestAsync.htm))  
[StartProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_StartProcessAsync.htm)|  
(Переопределяет [WorkflowStoreExtension.StartProcessAsync(Nullable<Guid>,
String, IWorkflowWorker,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_StartProcessAsync.htm))  
[TaskIsAllowedAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension_TaskIsAllowedAsync.htm)|  
(Переопределяет [WorkflowStoreExtension.TaskIsAllowedAsync(CardTask,
ICardStoreExtensionContext)](M_Tessa_Cards_Workflow_WorkflowStoreExtension_TaskIsAllowedAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnknownTaskIsAllowedAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_UnknownTaskIsAllowedAsync.htm)|
Возвращает признак того, что задание, для которого не удалось найти информацию
в бизнес-процессе, не должно останавливать сохранение карточки с ошибкой. Чаще
всего такая ситуация возникает для заданий, которое уже было завершено в
параллельном сохранении (например, заместителем исполнителя в роли задания).
Рекомендуется оставить значение по умолчанию false для всех заданий, кроме
исключительных случаев.  
(Унаследован от
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)
