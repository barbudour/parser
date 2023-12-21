# WorkflowManager - свойства
##  __Свойства
[CardGetStrategy](P_Tessa_Cards_Workflow_WorkflowManager_CardGetStrategy.htm)|
Стратегия, выполняющая низкоуровневую загрузку секций карточки, или null, если
такая загрузка не поддерживается. Обычно требуется для создания групп в
истории заданий совместно с объектом TaskHistoryManager.  
---|---  
[CardMetadata](P_Tessa_Cards_Workflow_WorkflowManager_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
[CardType](P_Tessa_Cards_Workflow_WorkflowManager_CardType.htm)| Тип карточки,
в рамках которого выполняется бизнес-процесс.  
[CountersSectionName](P_Tessa_Cards_Workflow_WorkflowManager_CountersSectionName.htm)|
Имя секции со счётчиками бизнес-процесса.  
[DbScope](P_Tessa_Cards_Workflow_WorkflowManager_DbScope.htm)|  Объект,
посредством которого выполняется взаимодействие с базой данных в пределах
транзакции на сохранение карточки.  
[Info](P_Tessa_Cards_Workflow_WorkflowManager_Info.htm)| Дополнительная
информация, связанная с контекстом бизнес-процесса.  
[NextRequest](P_Tessa_Cards_Workflow_WorkflowManager_NextRequest.htm)|  Запрос
на дополнительное сохранение карточки, в процессе которого могут высылаться
задания бизнес-процесса. После изменения запроса обязательно следует вызвать
метод [IWorkflowContext.NotifyNextRequestPending], чтобы определить
необходимость дополнительного сохранения карточки.  
[NextRequestPending](P_Tessa_Cards_Workflow_WorkflowManager_NextRequestPending.htm)|
Признак того, что хотя бы раз был вызван метод
[IWorkflowContext.NotifyNextRequestPending] для того, чтобы определить
необходимость дополнительного сохранения карточки посредством запроса
[IWorkflowContext.NextRequest].  
[ProcessesAwaitingRemoval](P_Tessa_Cards_Workflow_WorkflowManager_ProcessesAwaitingRemoval.htm)|
Подпроцессы, ожидающие удаления после выполнения всех действий на текущем
этапе (т.е. обработки всех заданий и всех сигналов из Request), но перед
запуском вложенного сохранения NextRequest. Подпроцессы указаны в порядке
удаления. Если один и тот же подпроцесс указан несколько раз, то он будет
удалён только один раз.  
[ProcessesSectionName](P_Tessa_Cards_Workflow_WorkflowManager_ProcessesSectionName.htm)|
Имя секции с активными подпроцессами бизнес-процесса.  
[QueueProcessor](P_Tessa_Cards_Workflow_WorkflowManager_QueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди
[Tessa.Cards.Workflow.WorkflowQueue].  
[Request](P_Tessa_Cards_Workflow_WorkflowManager_Request.htm)| Запрос на
сохранение карточки, в процессе которого производится управление бизнес-
процессом.  
[Session](P_Tessa_Cards_Workflow_WorkflowManager_Session.htm)| Сессия
пользователя, который совершил действие, вызвавшее изменение в бизнес-
процессе.  
[StoreDateTime](P_Tessa_Cards_Workflow_WorkflowManager_StoreDateTime.htm)|
Текущие дата и время сохранения для использования в транзакции.  
[TaskHistoryManager](P_Tessa_Cards_Workflow_WorkflowManager_TaskHistoryManager.htm)|
Объект, управляющий созданием групп в истории заданий.  
[TasksSectionName](P_Tessa_Cards_Workflow_WorkflowManager_TasksSectionName.htm)|
Имя секции с активными заданиями бизнес-процесса.  
[ValidationResult](P_Tessa_Cards_Workflow_WorkflowManager_ValidationResult.htm)|
Объект, посредством которого добавляются сообщения валидации, связанные с
управлением бизнес-процессом.  
[WorkflowCardID](P_Tessa_Cards_Workflow_WorkflowManager_WorkflowCardID.htm)|
Идентификатор карточки, в которой содержатся секции бизнес-процесса.  
##  __См. также
#### Ссылки
[WorkflowManager - ](T_Tessa_Cards_Workflow_WorkflowManager.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
