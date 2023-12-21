# WfWorkflowWorker - класс
Класс, реализующий логику бизнес-процессов Workflow.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.Wf](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class WfWorkflowWorker : WorkflowTaskWorker<WfWorkflowManager>
VB __Копировать
     Public Class WfWorkflowWorker
    	Inherits WorkflowTaskWorker(Of WfWorkflowManager)
C++ __Копировать
     public ref class WfWorkflowWorker : public WorkflowTaskWorker<WfWorkflowManager^>
F# __Копировать
     type WfWorkflowWorker = 
        class
            inherit WorkflowTaskWorker<WfWorkflowManager>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkflowWorker](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm)<[WfWorkflowManager](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager.htm)> __[WorkflowTaskWorker](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm)<[WfWorkflowManager](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager.htm)> __ WfWorkflowWorker
##  __Конструкторы
[WfWorkflowWorker](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CardRepositoryToCreateTasks](P_Tessa_Cards_Workflow_WorkflowTaskWorker_1_CardRepositoryToCreateTasks.htm)|
Репозиторий карточек, используемый для создания карточек заданий.  
(Унаследован от
[WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm))  
---|---  
[Manager](P_Tessa_Cards_Workflow_WorkflowWorker_1_Manager.htm)| Объект,
предоставляющий возможности для управления бизнес-процессом.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
##  __Методы
[AddNewTaskAsync](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_AddNewTaskAsync.htm)|
Создаёт и добавляет задание в запрос на дополнительное сохранение карточки.  
(Унаследован от
[WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm))  
---|---  
[AddNotificationsOnCreatedTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_AddNotificationsOnCreatedTasksAsync.htm)|
Добавляем уведомления в очередь о созданных заданиях.  
[AddTaskToProcessInfo(IWorkflowProcessInfo,
IEnumerable<Guid>)](M_Tessa_Cards_Workflow_WorkflowWorker_1_AddTaskToProcessInfo.htm)|
Добавляет идентификаторы заданий к списку заданий в подпроцессе.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[AddTaskToProcessInfo(IWorkflowProcessInfo,
Guid)](M_Tessa_Cards_Workflow_WorkflowWorker_1_AddTaskToProcessInfo_1.htm)|
Добавляет идентификатор задания к списку заданий в подпроцессе.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[CanCheckChildResolutionDateAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_CanCheckChildResolutionDateAsync.htm)|
Возвращает признак того, что требуется выполнить проверку на дату
запланированного завершения дочерней резолюции, чтобы она не превышала дату
завершения родительской резолюции более, чем на один бизнес-день.  
[ClearWasteOnNextStoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_ClearWasteOnNextStoreAsync.htm)|
Очищает поля с параметрами вариантов завершения у задачи при завершении без
удаления. Используется при создании дочерних задач, чтобы очистить комментарий
и прочие поля.  
[CompleteResolutionProjectOnNextStoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_CompleteResolutionProjectOnNextStoreAsync.htm)|
Указывает на необходимость завершить задание постановки задачи с указанными
параметрами и значениями в секциях.  
[CompleteTaskAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_CompleteTaskAsync.htm)|
Выполняет действие при завершении заданного задания. Не удаляет запись с
информацией по заданию, т.к. задание может завершаться без удаления записи.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[CompleteTaskCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_CompleteTaskCoreAsync.htm)|
Выполняет действия при завершении задания.  
(Переопределяет
[WorkflowWorker<TManager>.CompleteTaskCoreAsync(IWorkflowTaskInfo,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_CompleteTaskCoreAsync.htm))  
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
[GetTaskCount](M_Tessa_Cards_Workflow_WorkflowWorker_1_GetTaskCount.htm)|
Возвращает количество заданий, о которых известно в подпроцессе.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[GetTaskHistoryGroupsAsync](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_GetTaskHistoryGroupsAsync.htm)|
Загружает секцию карточки с идентификатором Manager.Request.Card.ID с группами
в истории, которые требуются для создания новых групп в истории. Возвращённое
значение не равно null даже в случае ошибок. Вызов метода не приводит к
изменению карточек в запросах Manager.Request и Manager.NextRequest.  
(Унаследован от
[WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasTasks](M_Tessa_Cards_Workflow_WorkflowWorker_1_HasTasks.htm)|  Возвращает
признак того, что в подпроцессе присутствует хотя бы одно известное задание.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ModifyAsAuthorOnNextStoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_ModifyAsAuthorOnNextStoreAsync.htm)|
Изменяет дату выполнения и комментарий задания в соответствии с заполненными
пользователем данными при следующем сохранении.  
[ProcessSignalAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ProcessSignalAsync.htm)|
Выполняет действие по обработке сигнала. Возвращает признак того, что сигнал
был ожидаем и обработан (необязательно успешно). Необработанный сигнал по
умолчанию не приводит к ошибке сохранения карточки и не приводит к откату
транзакции, но не помечается как обработанный в очереди. По умолчанию все
сигналы считаются необработанными. Необработанное исключение, возникшее в
обработчике, также отмечает сигнал как необработанный. Если для ожидаемого
сигнала требуется прервать транзакцию, то добавьте ошибку в
Manager.ValidationResult, но верните в методе true. Если параметры подпроцесса
отмечены как изменённые, то по завершении метода они сохраняются независимо от
возвращённого значения.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ProcessSignalCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_ProcessSignalCoreAsync.htm)|
Выполняет действие по обработке сигнала. Возвращает признак того, что сигнал
был ожидаем и обработан (необязательно успешно). Необработанный сигнал по
умолчанию не приводит к ошибке сохранения карточки и не приводит к откату
транзакции, но не помечается как обработанный в очереди. По умолчанию все
сигналы считаются необработанными. Необработанное исключение, возникшее в
обработчике, также отмечает сигнал как необработанный. Если для ожидаемого
сигнала требуется прервать транзакцию, то добавьте ошибку в
Manager.ValidationResult, но верните в методе true.  
(Переопределяет
[WorkflowWorker<TManager>.ProcessSignalCoreAsync(IWorkflowSignalInfo,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_ProcessSignalCoreAsync.htm))  
[ReinstateTaskAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ReinstateTaskAsync.htm)|
Выполняет действие при возврате на роль заданного задания. Не удаляет запись с
информацией по заданию.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ReinstateTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ReinstateTaskCoreAsync.htm)|
Выполняет действие при возврате задания на роль.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RemoveTaskFromProcessInfo(IWorkflowProcessInfo,
IEnumerable<Guid>)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RemoveTaskFromProcessInfo.htm)|
Удаляет идентификаторы заданий из списка заданий в подпроцессе. Возвращает
количество идентификаторов, которые присутствовали в списке заданий и были
удалены.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RemoveTaskFromProcessInfo(IWorkflowProcessInfo,
Guid)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RemoveTaskFromProcessInfo_1.htm)|
Удаляет идентификатор задания из списка заданий в подпроцессе. Возвращает
признак того, что идентификатор там был, после чего был удалён.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RenderStepAsync(Int32, IWorkflowProcessInfo,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RenderStepAsync.htm)|
Выполняет переход к состоянию с заданным номером.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RenderStepAsync(String, IWorkflowTaskInfo,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_RenderStepAsync.htm)|
Выполняет переход, номер которого содержится в параметрах задания taskInfo по
ключу transitionKey. Если номер перехода не найден или задан отрицательным
числом, то действий не выполняется и возвращается false.  
[RenderStepCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_RenderStepCoreAsync.htm)|
Выполняет переход.  
(Переопределяет [WorkflowWorker<TManager>.RenderStepCoreAsync(Int32,
IWorkflowProcessInfo,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RenderStepCoreAsync.htm))  
[ReplaceTaskHistorySubstringAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_ReplaceTaskHistorySubstringAsync.htm)|
Изменяем подстроку oldSubstring на строку newSubstring в результате записи в
истории завершённых заданий для задания taskRowID. Например, можно изменить
одно название роли на другое. Возвращает признак того, что запись была
изменена.  
[ResolveTaskHistoryGroupAsync](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_ResolveTaskHistoryGroupAsync.htm)|
Возвращает группу в истории заданий, вычисленную для заданных параметров. При
необходимости группа будет создана.  
(Унаследован от
[WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm))  
[RevokeChildResolutionsAsync(Guid,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_RevokeChildResolutionsAsync.htm)|
В следующий запрос на сохранение
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm)
добавляет отзыв всех дочерних резолюций для резолюции с заданным
идентификатором. При этом рекурсивно будут отозваны все дочерние резолюции,
включая дочерние для дочерних. Возвращает признак того, что все резолюции,
нуждающиеся в отзыве, будут отозваны, причём при их загрузке не возникло
ошибок.  
[RevokeChildResolutionsAsync(CardTask, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_RevokeChildResolutionsAsync_1.htm)|
В следующий запрос на сохранение
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm)
добавляет отзыв всех дочерних резолюций для заданной резолюции
parentResolution. При этом рекурсивно будут отозваны все дочерние резолюции,
включая дочерние для дочерних. Возвращает признак того, что все резолюции,
нуждающиеся в отзыве, будут отозваны, причём при их загрузке не возникло
ошибок. Метод выполняется только в том случае, если в коллекции
ChildrenResolutions есть хотя бы одно дочернее задание.  
[SendResolutionAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_SendResolutionAsync.htm)|
Отправляет задание резолюции с заданными параметрами.  
[SendResolutionControlAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_SendResolutionControlAsync.htm)|
Отправляет задание на контроль исполнения резолюции с заданными параметрами.  
[SendResolutionControlIfNecessaryForLastChildAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_SendResolutionControlIfNecessaryForLastChildAsync.htm)|
Отправляет задание на контроль исполнения резолюции с заданными параметрами
для родительского задания при завершении последней дочерней резолюции или
задании в цепочке отправки или контроля исполнения, где родительским заданием
для цепочки является дочерняя резолюция.  
[SendResolutionProjectAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_SendResolutionProjectAsync.htm)|
Оправляет задание проекта резолюции с заданными параметрами для текущего
пользователя.  
[SendResolutionToPerformersAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_SendResolutionToPerformersAsync.htm)|
Отправляет резолюцию исполнителям. Может выполнить как стандартную отправку на
заданную роль, так и массовую отправку, в процессе которой на каждую из ролей
исполнителей отправляется дочерняя резолюция, после чего отправляемая
резолюция завершается без отзыва дочерних.  
[SendTaskAsync(Guid, IWorkflowProcessInfo, String, Dictionary<String, Object>,
Nullable<Guid>, Func<CardTask, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_SendTaskAsync.htm)|
Создаёт и отправляет задание заданного типа с указанными параметрами от имени
текущего пользователя.  
(Унаследован от
[WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm))  
[SendTaskAsync(Guid, IWorkflowProcessInfo, String, Guid, String,
Dictionary<String, Object>, Nullable<Guid>, Func<CardTask, CancellationToken,
ValueTask>,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_SendTaskAsync_1.htm)|
Создаёт и отправляет задание заданного типа с указанными параметрами.  
(Унаследован от
[WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm))  
[StartProcessAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartProcessAsync.htm)|
Выполняет действие при старте подпроцесса с уникальным именем типа и
параметрами. Создаёт запись с информацией по подпроцессу.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StartProcessCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_StartProcessCoreAsync.htm)|
Выполняет действия при запуске подпроцесса.  
(Переопределяет
[WorkflowWorker<TManager>.StartProcessCoreAsync(IWorkflowProcessInfo,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartProcessCoreAsync.htm))  
[StartSubProcessWithCompletionAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartSubProcessWithCompletionAsync.htm)|
Запускает подпроцесс, который выполняет указанный переход при завершении.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StopProcessAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopProcessAsync.htm)|
Выполняет действие при завершении заданного подпроцесса. Удаляет запись с
информацией по подпроцессу.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StopProcessCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_StopProcessCoreAsync.htm)|
Выполняет действия при завершении подпроцесса.  
(Переопределяет
[WorkflowWorker<TManager>.StopProcessCoreAsync(IWorkflowProcessInfo,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopProcessCoreAsync.htm))  
[StopSubProcessWithCompletionAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopSubProcessWithCompletionAsync.htm)|
Завершает подпроцесс, выполняя переход, указанный при запуске подпроцесса
методом [StartSubProcessWithCompletionAsync(String, Int32,
IWorkflowProcessInfo, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartSubProcessWithCompletionAsync.htm).  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetHistoryItemParentRowIDAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_TryGetHistoryItemParentRowIDAsync.htm)|
Возвращает идентификатор родительской записи в истории заданий для заданного
задания taskRowID или null, если родительская запись отсутствует или по
заданному заданию не была создана запись в истории.  
[TryGetOrCreatePerformerRoleAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_TryGetOrCreatePerformerRoleAsync.htm)|
Возвращает роль исполнителя, на которую должно быть назначено задание, или
создаёт и возвращает временную роль, если указано несколько исполнителей.
Возвращает false, если не удалось получить или создать роль исполнителя; в
этом случае информация по произошедшей ошибке содержится в контекте бизнес-
процесса
[ValidationResult](P_Tessa_Cards_Workflow_IWorkflowContext_ValidationResult.htm).  
[TryGetPerformersAndCheckNotEmpty](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_TryGetPerformersAndCheckNotEmpty.htm)|
Возвращает массив строк с ролями исполнителей, используемыми при отправке
резолюции, или null, если получить список невозможно или список пуст.
Возвращаемое значение не может быть пустым массивом. Если значение пустое, то
добавляется сообщение об ошибке.  
[TryGetTasksFromProcessInfo](M_Tessa_Cards_Workflow_WorkflowWorker_1_TryGetTasksFromProcessInfo.htm)|
Возвращает массив идентификаторов заданий, о которых известно в подпроцессе,
или null, если таких заданий не существует.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[UpdateModifiedByAuthorDate](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_UpdateModifiedByAuthorDate.htm)|
Указывает для заданного результата завершения задания информацию о том, что
автор изменил задание после отправки.  
## __Поля
[RemoveTaskAndStopIfLastTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_RemoveTaskAndStopIfLastTransition.htm)|
Переход в любом подпроцессе, удаляющий текущее задание из списка в подпроцессе
и завершающий подпроцесс только в том случае, если текущее задание было
последним.  
---|---  
[StartProcessTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_StartProcessTransition.htm)|
Первый переход в любом подпроцессе.  
[StopProcessTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_StopProcessTransition.htm)|
Переход в любом подпроцессе, завершающий подпроцесс.  
[WfModifyAsAuthorTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_WfModifyAsAuthorTransition.htm)|
Переход в подпроцессе резолюций, изменяющий дату выполнения резолюции.  
[WfResolutionCompleteTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_WfResolutionCompleteTransition.htm)|
Переход в подпроцессе резолюций, завершающий резолюцию.  
[WfResolutionCreateChildTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_WfResolutionCreateChildTransition.htm)|
Переход в подпроцессе резолюций, создающий дочернюю резолюцию.  
[WfResolutionRevokeOrCancelTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_WfResolutionRevokeOrCancelTransition.htm)|
Переход в подпроцессе резолюций, отзывающий или отменяющий резолюцию.  
[WfResolutionSendToPerformerTransition](F_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_WfResolutionSendToPerformerTransition.htm)|
Переход в подпроцессе резолюций, отправляющий резолюцию исполнителю.  
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
[Tessa.Extensions.Default.Server.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)
