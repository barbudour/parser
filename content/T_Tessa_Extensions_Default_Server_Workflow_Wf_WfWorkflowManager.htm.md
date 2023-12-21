# WfWorkflowManager - класс
Объект, предоставляющий возможности для управления бизнес-процессами Workflow.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.Wf](N_Tessa_Extensions_Default_Server_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class WfWorkflowManager : WorkflowManager
VB __Копировать
     Public Class WfWorkflowManager
    	Inherits WorkflowManager
C++ __Копировать
     public ref class WfWorkflowManager : public WorkflowManager
F# __Копировать
     type WfWorkflowManager = 
        class
            inherit WorkflowManager
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm) __ WfWorkflowManager
##  __Конструкторы
[WfWorkflowManager](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager_CardCache.htm)|
Кэш карточек.  
---|---  
[CardGetStrategy](P_Tessa_Cards_Workflow_WorkflowManager_CardGetStrategy.htm)|
Стратегия, выполняющая низкоуровневую загрузку секций карточки, или null, если
такая загрузка не поддерживается. Обычно требуется для создания групп в
истории заданий совместно с объектом TaskHistoryManager.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[CardMetadata](P_Tessa_Cards_Workflow_WorkflowManager_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[CardType](P_Tessa_Cards_Workflow_WorkflowManager_CardType.htm)| Тип карточки,
в рамках которого выполняется бизнес-процесс.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[CountersSectionName](P_Tessa_Cards_Workflow_WorkflowManager_CountersSectionName.htm)|
Имя секции со счётчиками бизнес-процесса.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[DbScope](P_Tessa_Cards_Workflow_WorkflowManager_DbScope.htm)|  Объект,
посредством которого выполняется взаимодействие с базой данных в пределах
транзакции на сохранение карточки.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[Info](P_Tessa_Cards_Workflow_WorkflowManager_Info.htm)| Дополнительная
информация, связанная с контекстом бизнес-процесса.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[KrTypesCache](P_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager_KrTypesCache.htm)|
Кэш с карточками и дополнительными настройками.  
[NextRequest](P_Tessa_Cards_Workflow_WorkflowManager_NextRequest.htm)|  Запрос
на дополнительное сохранение карточки, в процессе которого могут высылаться
задания бизнес-процесса. После изменения запроса обязательно следует вызвать
метод [IWorkflowContext.NotifyNextRequestPending], чтобы определить
необходимость дополнительного сохранения карточки.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[NextRequestPending](P_Tessa_Cards_Workflow_WorkflowManager_NextRequestPending.htm)|
Признак того, что хотя бы раз был вызван метод
[IWorkflowContext.NotifyNextRequestPending] для того, чтобы определить
необходимость дополнительного сохранения карточки посредством запроса
[IWorkflowContext.NextRequest].  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[NotificationManager](P_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager_NotificationManager.htm)|
Объект, управляющий отправкой уведомлений.  
[ProcessesAwaitingRemoval](P_Tessa_Cards_Workflow_WorkflowManager_ProcessesAwaitingRemoval.htm)|
Подпроцессы, ожидающие удаления после выполнения всех действий на текущем
этапе (т.е. обработки всех заданий и всех сигналов из Request), но перед
запуском вложенного сохранения NextRequest. Подпроцессы указаны в порядке
удаления. Если один и тот же подпроцесс указан несколько раз, то он будет
удалён только один раз.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[ProcessesSectionName](P_Tessa_Cards_Workflow_WorkflowManager_ProcessesSectionName.htm)|
Имя секции с активными подпроцессами бизнес-процесса.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[QueueProcessor](P_Tessa_Cards_Workflow_WorkflowManager_QueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди
[Tessa.Cards.Workflow.WorkflowQueue].  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[Request](P_Tessa_Cards_Workflow_WorkflowManager_Request.htm)| Запрос на
сохранение карточки, в процессе которого производится управление бизнес-
процессом.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RoleRepository](P_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager_RoleRepository.htm)|
Репозиторий для управления ролями.  
[Session](P_Tessa_Cards_Workflow_WorkflowManager_Session.htm)| Сессия
пользователя, который совершил действие, вызвавшее изменение в бизнес-
процессе.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[StoreDateTime](P_Tessa_Cards_Workflow_WorkflowManager_StoreDateTime.htm)|
Текущие дата и время сохранения для использования в транзакции.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TaskHistoryManager](P_Tessa_Cards_Workflow_WorkflowManager_TaskHistoryManager.htm)|
Объект, управляющий созданием групп в истории заданий.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TasksSectionName](P_Tessa_Cards_Workflow_WorkflowManager_TasksSectionName.htm)|
Имя секции с активными заданиями бизнес-процесса.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[ValidationResult](P_Tessa_Cards_Workflow_WorkflowManager_ValidationResult.htm)|
Объект, посредством которого добавляются сообщения валидации, связанные с
управлением бизнес-процессом.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[WorkflowCardID](P_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager_WorkflowCardID.htm)|
Идентификатор карточки-сателлита Workflow, используемой для хранения
информации по бизнес-процессам, или идентификатор основной карточки, если
идентификатор карточки-сателлита не был установлен в текущем контексте.  
(Переопределяет
[WorkflowManager.WorkflowCardID](P_Tessa_Cards_Workflow_WorkflowManager_WorkflowCardID.htm))  
##  __Методы
[AddProcessAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddProcessAsync.htm)|
Добавляет информацию по подпроцессу.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
---|---  
[AddProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddProcessCoreAsync.htm)|
Добавляет информацию по заданному подпроцессу.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[AddProcessToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddProcessToCacheAsync.htm)|
Добавляет информацию по подпроцессу в кэш. Если информация уже была добавлена,
то она будет замещена.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[AddTaskAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddTaskAsync.htm)|
Добавляет информацию по заданию в список активных заданий. Метод следует
использовать при создании заданий, относящихся к бизнес-процессу.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[AddTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddTaskCoreAsync.htm)|
Добавляет информацию по заданному заданию в список активных заданий.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[AddTaskToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddTaskToCacheAsync.htm)|
Добавляет информацию по заданию в кэш. Если информация уже была добавлена, то
она будет замещена.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[AddUnknownProcessToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddUnknownProcessToCacheAsync.htm)|
Добавляет в кэш информацию о том, что подпроцесс с заданным идентификатором
отсутствует.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[AddUnknownTaskToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddUnknownTaskToCacheAsync.htm)|
Добавляет в кэш информацию о том, что информация по заданному заданию
отсутствует.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[CreateProcessInfoCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_CreateProcessInfoCoreAsync.htm)|
Метод, создающий информацию по подпроцессу для заданных параметров.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[CreateTaskInfoCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_CreateTaskInfoCoreAsync.htm)|
Метод, создающий информацию по заданию в подпроцессе для заданных параметров.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[DecrementCounterAsync](M_Tessa_Cards_Workflow_WorkflowManager_DecrementCounterAsync.htm)|
Уменьшает текущее значение счётчика на заданное значение decrementValue. Если
текущее значение становится не больше нуля, то счётчик удаляется. Возвращает
состояние счётчика после выполнения метода.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[DecrementCounterCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_DecrementCounterCoreAsync.htm)|
Уменьшает текущее значение счётчика на заданное значение decrementValue. Если
текущее значение становится не больше нуля, то счётчик удаляется. Возвращает
состояние счётчика после выполнения метода.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
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
[GetSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager_GetSettingsAsync.htm)|
Возвращает настройки решения для Wf.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetWorkflowCardIDAsync](M_Tessa_Cards_Workflow_WorkflowManager_GetWorkflowCardIDAsync.htm)|
Асинхронно возвращает идентификатор карточки, в которой содержатся секции
бизнес-процесса.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[InitCounterAsync](M_Tessa_Cards_Workflow_WorkflowManager_InitCounterAsync.htm)|
Инициализирует счётчик с заданным номером, уникальным для подпроцесса, и с
указанием начального значения. Счётчик используется для ожидания нескольких
параллельных заданий в бизнес-процессе.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[InitCounterCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_InitCounterCoreAsync.htm)|
Инициализирует счётчик с заданным номером, уникальным для подпроцесса, и с
указанием начального значения. Счётчик используется для ожидания нескольких
параллельных заданий в бизнес-процессе.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyNextRequestPending](M_Tessa_Cards_Workflow_WorkflowManager_NotifyNextRequestPending.htm)|
Уведомляет о необходимости выполнить повторное сохранение карточки. Если метод
был вызван хотя бы раз, то свойство [IWorkflowContext.NextRequestPending]
вернёт значение true.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveAwaitingProcessesAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveAwaitingProcessesAsync.htm)|
Удаляет все подпроцессы ProcessesAwaitingRemoval, ожидающие удаления после
выполнения всех действий на текущем этапе (т.е. обработки всех заданий и всех
сигналов из Request), но перед запуском вложенного сохранения NextRequest.
Подпроцессы удаляются в порядке, указанном в коллекции. Если один и тот же
подпроцесс указан несколько раз, то он будет удалён только один раз. После
выполнения метода коллекция очищается. Возвращается количество удалённых
подпроцессов или 0, если подпроцессы не будут удалены.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveCounterAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveCounterAsync.htm)|
Удаляет счётчик с заданным номером, уникальным для подпроцесса.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveCounterCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveCounterCoreAsync.htm)|
Удаляет счётчик с заданным номером, уникальным для подпроцесса.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveProcessAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveProcessAsync.htm)|
Удаляет информацию по подпроцессу. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveProcessCoreAsync.htm)|
Удаляет информацию по подпроцессу. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveProcessFromCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveProcessFromCacheAsync.htm)|
Удаляет из кэша информацию по подпроцессу с заданным идентификатором.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveTaskAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveTaskAsync.htm)|
Удаляет заданное задание из списка активных заданий и возвращает информацию по
заданию или null, если задание неизвестно. Рекомендуется использовать при
завершении или отзыве задания.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveTaskCoreAsync.htm)|
Удаляет информацию по заданию из списка активных заданий.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[RemoveTaskFromCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveTaskFromCacheAsync.htm)|
Удаляет из кэша информацию по заданному заданию.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetProcessAsync(Guid,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessAsync.htm)|
Возвращает информацию по подпроцессу с заданным идентификатором или null, если
подпроцесс не был найден.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetProcessAsync(String,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessAsync_1.htm)|
Возвращает информацию по первому найденному подпроцессу с заданным именем типа
или null, если ни один подпроцесс подходящего типа не был найден.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetProcessCoreAsync(Guid,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessCoreAsync.htm)|
Возвращает информацию по подпроцессу с заданным идентификатором или null, если
подпроцесс не был найден.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetProcessCoreAsync(String,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessCoreAsync_1.htm)|
Возвращает информацию по первому найденному подпроцессу с заданным именем типа
или null, если ни один подпроцесс подходящего типа не был найден.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetProcessFromCacheAsync(Guid,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessFromCacheAsync.htm)|
Возвращает информацию по подпроцессу в кэше или null, если информация
отсутствует в кэше.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetProcessFromCacheAsync(String,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessFromCacheAsync_1.htm)|
Возвращает информацию по первому подпроцессу в кэше, имя типа которого равно
заданной строке typeName, или null, если подходящий подпроцесс отсутствует в
кэше.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetTaskAsync](M_Tessa_Cards_Workflow_WorkflowManager_TryGetTaskAsync.htm)|
Возвращает информацию по заданию из списка активных заданий или null, если
задание отсутствовало в списке. Рекомендуется использовать для заданий,
завершение которых было отменено в расширениях.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_TryGetTaskCoreAsync.htm)|
Возвращает информацию по заданию из списка активных заданий или null, если
задание отсутствовало в списке. Рекомендуется использовать для заданий,
завершение которых было отменено в расширениях.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[TryGetTaskFromCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_TryGetTaskFromCacheAsync.htm)|
Возвращает информацию по заданию в кэше или null, если информация отсутствует
в кэше.  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[UpdateProcessParametersAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateProcessParametersAsync.htm)|
Обновляет параметры подпроцесса. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[UpdateProcessParametersCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateProcessParametersCoreAsync.htm)|
Обновляет параметры подпроцесса. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[UpdateTaskParametersAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateTaskParametersAsync.htm)|
Обновляет параметры задания (но не подпроцесса).  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
[UpdateTaskParametersCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateTaskParametersCoreAsync.htm)|
Обновляет параметры задания (но не подпроцесса).  
(Унаследован от [WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm))  
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
