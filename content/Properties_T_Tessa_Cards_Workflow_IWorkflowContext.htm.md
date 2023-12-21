# IWorkflowContext - свойства
##  __Свойства
[CardGetStrategy](P_Tessa_Cards_Workflow_IWorkflowContext_CardGetStrategy.htm)|
Стратегия, выполняющая низкоуровневую загрузку секций карточки, или null, если
такая загрузка не поддерживается. Обычно требуется для создания групп в
истории заданий совместно с объектом TaskHistoryManager.  
---|---  
[CardMetadata](P_Tessa_Cards_Workflow_IWorkflowContext_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
[CardType](P_Tessa_Cards_Workflow_IWorkflowContext_CardType.htm)| Тип
карточки, в рамках которого выполняется бизнес-процесс.  
[DbScope](P_Tessa_Cards_Workflow_IWorkflowContext_DbScope.htm)|  Объект,
посредством которого выполняется взаимодействие с базой данных в пределах
транзакции на сохранение карточки.  
[Info](P_Tessa_Cards_Workflow_IWorkflowContext_Info.htm)| Дополнительная
информация, связанная с контекстом бизнес-процесса.  
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm)|
Запрос на дополнительное сохранение карточки, в процессе которого могут
высылаться задания бизнес-процесса. После изменения запроса обязательно
следует вызвать метод [IWorkflowContext.NotifyNextRequestPending], чтобы
определить необходимость дополнительного сохранения карточки.  
[NextRequestPending](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequestPending.htm)|
Признак того, что хотя бы раз был вызван метод
[IWorkflowContext.NotifyNextRequestPending] для того, чтобы определить
необходимость дополнительного сохранения карточки посредством запроса
[IWorkflowContext.NextRequest].  
[Request](P_Tessa_Cards_Workflow_IWorkflowContext_Request.htm)| Запрос на
сохранение карточки, в процессе которого производится управление бизнес-
процессом.  
[Session](P_Tessa_Cards_Workflow_IWorkflowContext_Session.htm)| Сессия
пользователя, который совершил действие, вызвавшее изменение в бизнес-
процессе.  
[StoreDateTime](P_Tessa_Cards_Workflow_IWorkflowContext_StoreDateTime.htm)|
Текущие дата и время сохранения для использования в транзакции.  
[TaskHistoryManager](P_Tessa_Cards_Workflow_IWorkflowContext_TaskHistoryManager.htm)|
Объект, управляющий созданием групп в истории заданий.  
[ValidationResult](P_Tessa_Cards_Workflow_IWorkflowContext_ValidationResult.htm)|
Объект, посредством которого добавляются сообщения валидации, связанные с
управлением бизнес-процессом.  
## __См. также
#### Ссылки
[IWorkflowContext - ](T_Tessa_Cards_Workflow_IWorkflowContext.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
