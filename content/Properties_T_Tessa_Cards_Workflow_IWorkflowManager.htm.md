# IWorkflowManager - свойства
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
##  __См. также
#### Ссылки
[IWorkflowManager - ](T_Tessa_Cards_Workflow_IWorkflowManager.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
