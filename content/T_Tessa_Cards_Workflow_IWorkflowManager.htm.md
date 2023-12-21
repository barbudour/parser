# IWorkflowManager - интерфейс
Объект, предоставляющий возможности для управления бизнес-процессом.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowManager : IWorkflowContext
VB __Копировать
     Public Interface IWorkflowManager
    	Inherits IWorkflowContext
C++ __Копировать
     public interface class IWorkflowManager : IWorkflowContext
F# __Копировать
     type IWorkflowManager = 
        interface
            interface IWorkflowContext
        end
Implements
    [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm)
##  __Свойства
[CardGetStrategy](P_Tessa_Cards_Workflow_IWorkflowContext_CardGetStrategy.htm)|
Стратегия, выполняющая низкоуровневую загрузку секций карточки, или null, если
такая загрузка не поддерживается. Обычно требуется для создания групп в
истории заданий совместно с объектом TaskHistoryManager.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
---|---  
[CardMetadata](P_Tessa_Cards_Workflow_IWorkflowContext_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[CardType](P_Tessa_Cards_Workflow_IWorkflowContext_CardType.htm)| Тип
карточки, в рамках которого выполняется бизнес-процесс.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[DbScope](P_Tessa_Cards_Workflow_IWorkflowContext_DbScope.htm)|  Объект,
посредством которого выполняется взаимодействие с базой данных в пределах
транзакции на сохранение карточки.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[Info](P_Tessa_Cards_Workflow_IWorkflowContext_Info.htm)| Дополнительная
информация, связанная с контекстом бизнес-процесса.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm)|
Запрос на дополнительное сохранение карточки, в процессе которого могут
высылаться задания бизнес-процесса. После изменения запроса обязательно
следует вызвать метод [IWorkflowContext.NotifyNextRequestPending], чтобы
определить необходимость дополнительного сохранения карточки.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[NextRequestPending](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequestPending.htm)|
Признак того, что хотя бы раз был вызван метод
[IWorkflowContext.NotifyNextRequestPending] для того, чтобы определить
необходимость дополнительного сохранения карточки посредством запроса
[IWorkflowContext.NextRequest].  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[ProcessesAwaitingRemoval](P_Tessa_Cards_Workflow_IWorkflowManager_ProcessesAwaitingRemoval.htm)|
Подпроцессы, ожидающие удаления после выполнения всех действий на текущем
этапе (т.е. обработки всех заданий и всех сигналов из Request), но перед
запуском вложенного сохранения NextRequest. Подпроцессы указаны в порядке
удаления. Если один и тот же подпроцесс указан несколько раз, то он будет
удалён только один раз.  
[QueueProcessor](P_Tessa_Cards_Workflow_IWorkflowManager_QueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди
[Tessa.Cards.Workflow.WorkflowQueue].  
[Request](P_Tessa_Cards_Workflow_IWorkflowContext_Request.htm)| Запрос на
сохранение карточки, в процессе которого производится управление бизнес-
процессом.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[Session](P_Tessa_Cards_Workflow_IWorkflowContext_Session.htm)| Сессия
пользователя, который совершил действие, вызвавшее изменение в бизнес-
процессе.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[StoreDateTime](P_Tessa_Cards_Workflow_IWorkflowContext_StoreDateTime.htm)|
Текущие дата и время сохранения для использования в транзакции.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[TaskHistoryManager](P_Tessa_Cards_Workflow_IWorkflowContext_TaskHistoryManager.htm)|
Объект, управляющий созданием групп в истории заданий.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[ValidationResult](P_Tessa_Cards_Workflow_IWorkflowContext_ValidationResult.htm)|
Объект, посредством которого добавляются сообщения валидации, связанные с
управлением бизнес-процессом.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
##  __Методы
[AddProcessAsync](M_Tessa_Cards_Workflow_IWorkflowManager_AddProcessAsync.htm)|
Добавляет информацию по подпроцессу.  
---|---  
[AddTaskAsync](M_Tessa_Cards_Workflow_IWorkflowManager_AddTaskAsync.htm)|
Добавляет информацию по заданию в список активных заданий. Метод следует
использовать при создании заданий, относящихся к бизнес-процессу.  
[DecrementCounterAsync](M_Tessa_Cards_Workflow_IWorkflowManager_DecrementCounterAsync.htm)|
Уменьшает текущее значение счётчика на заданное значение decrementValue. Если
текущее значение становится не больше нуля, то счётчик удаляется. Возвращает
состояние счётчика после выполнения метода.  
[InitCounterAsync](M_Tessa_Cards_Workflow_IWorkflowManager_InitCounterAsync.htm)|
Инициализирует счётчик с заданным номером, уникальным для подпроцесса, и с
указанием начального значения. Счётчик используется для ожидания нескольких
параллельных заданий в бизнес-процессе.  
[NotifyNextRequestPending](M_Tessa_Cards_Workflow_IWorkflowContext_NotifyNextRequestPending.htm)|
Уведомляет о необходимости выполнить повторное сохранение карточки. Если метод
был вызван хотя бы раз, то свойство [IWorkflowContext.NextRequestPending]
вернёт значение true.  
(Унаследован от
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm))  
[RemoveAwaitingProcessesAsync](M_Tessa_Cards_Workflow_IWorkflowManager_RemoveAwaitingProcessesAsync.htm)|
Удаляет все подпроцессы ProcessesAwaitingRemoval, ожидающие удаления после
выполнения всех действий на текущем этапе (т.е. обработки всех заданий и всех
сигналов из Request), но перед запуском вложенного сохранения NextRequest.
Подпроцессы удаляются в порядке, указанном в коллекции. Если один и тот же
подпроцесс указан несколько раз, то он будет удалён только один раз. После
выполнения метода коллекция очищается. Возвращается количество удалённых
подпроцессов или 0, если подпроцессы не будут удалены.  
[RemoveCounterAsync](M_Tessa_Cards_Workflow_IWorkflowManager_RemoveCounterAsync.htm)|
Удаляет счётчик с заданным номером, уникальным для подпроцесса.  
[RemoveProcessAsync](M_Tessa_Cards_Workflow_IWorkflowManager_RemoveProcessAsync.htm)|
Удаляет информацию по подпроцессу. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
[RemoveTaskAsync](M_Tessa_Cards_Workflow_IWorkflowManager_RemoveTaskAsync.htm)|
Удаляет заданное задание из списка активных заданий и возвращает информацию по
заданию или null, если задание неизвестно. Рекомендуется использовать при
завершении или отзыве задания.  
[TryGetProcessAsync(Guid,
CancellationToken)](M_Tessa_Cards_Workflow_IWorkflowManager_TryGetProcessAsync.htm)|
Возвращает информацию по подпроцессу с заданным идентификатором или null, если
подпроцесс не был найден.  
[TryGetProcessAsync(String,
CancellationToken)](M_Tessa_Cards_Workflow_IWorkflowManager_TryGetProcessAsync_1.htm)|
Возвращает информацию по первому найденному подпроцессу с заданным именем типа
или null, если ни один подпроцесс подходящего типа не был найден.  
[TryGetTaskAsync](M_Tessa_Cards_Workflow_IWorkflowManager_TryGetTaskAsync.htm)|
Возвращает информацию по заданию из списка активных заданий или null, если
задание отсутствовало в списке. Рекомендуется использовать для заданий,
завершение которых было отменено в расширениях.  
[UpdateProcessParametersAsync](M_Tessa_Cards_Workflow_IWorkflowManager_UpdateProcessParametersAsync.htm)|
Обновляет параметры подпроцесса. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
[UpdateTaskParametersAsync](M_Tessa_Cards_Workflow_IWorkflowManager_UpdateTaskParametersAsync.htm)|
Обновляет параметры задания (но не подпроцесса).  
##  __Методы расширения
[AddTask](M_Tessa_Cards_Workflow_WorkflowExtensions_AddTask.htm)|  Добавляет
задание в состоянии [Inserted](T_Tessa_Cards_CardRowState.htm) к следующей
сохраняемой карточке
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm).  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
