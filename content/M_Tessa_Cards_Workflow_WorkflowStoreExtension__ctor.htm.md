# WorkflowStoreExtension - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected WorkflowStoreExtension(
    	ICardRepository cardRepositoryToCreateNextRequest,
    	ICardRepository cardRepositoryToStoreNextRequest,
    	ICardRepository cardRepositoryToCreateTasks,
    	ICardTaskHistoryManager taskHistoryManager = null,
    	ICardGetStrategy cardGetStrategy = null,
    	IWorkflowQueueProcessor workflowQueueProcessor = null
    )
VB __Копировать
     Protected Sub New ( 
    	cardRepositoryToCreateNextRequest As ICardRepository,
    	cardRepositoryToStoreNextRequest As ICardRepository,
    	cardRepositoryToCreateTasks As ICardRepository,
    	Optional taskHistoryManager As ICardTaskHistoryManager = Nothing,
    	Optional cardGetStrategy As ICardGetStrategy = Nothing,
    	Optional workflowQueueProcessor As IWorkflowQueueProcessor = Nothing
    )
C++ __Копировать
     protected:
    WorkflowStoreExtension(
    	ICardRepository^ cardRepositoryToCreateNextRequest, 
    	ICardRepository^ cardRepositoryToStoreNextRequest, 
    	ICardRepository^ cardRepositoryToCreateTasks, 
    	ICardTaskHistoryManager^ taskHistoryManager = nullptr, 
    	ICardGetStrategy^ cardGetStrategy = nullptr, 
    	IWorkflowQueueProcessor^ workflowQueueProcessor = nullptr
    )
F# __Копировать
     new : 
            cardRepositoryToCreateNextRequest : ICardRepository * 
            cardRepositoryToStoreNextRequest : ICardRepository * 
            cardRepositoryToCreateTasks : ICardRepository * 
            ?taskHistoryManager : ICardTaskHistoryManager * 
            ?cardGetStrategy : ICardGetStrategy * 
            ?workflowQueueProcessor : IWorkflowQueueProcessor 
    (* Defaults:
            let _taskHistoryManager = defaultArg taskHistoryManager null
            let _cardGetStrategy = defaultArg cardGetStrategy null
            let _workflowQueueProcessor = defaultArg workflowQueueProcessor null
    *)
    -> WorkflowStoreExtension
#### Параметры
cardRepositoryToCreateNextRequest
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
Репозиторий для создания карточки для дополнительного сохранения карточки с
новыми заданиями.
Рекомендуется использовать в этом случае создание карточки без расширений,
т.к. на карточке могут быть расширения, резервирующие номера из
последовательностей и выполняющие другую работу, специфичные именно для
создания новой карточки, а не для создания запроса на сохранение существующей
карточки.
cardRepositoryToStoreNextRequest
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий для дополнительного сохранения карточки с новыми заданиями. 
cardRepositoryToCreateTasks
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий карточек, используемый для создания карточек заданий. Свойство может быть равно null, если создание заданий не предполагается. 
taskHistoryManager
[ICardTaskHistoryManager](T_Tessa_Cards_ICardTaskHistoryManager.htm)
(Optional)
     Объект, управляющий созданием групп в истории заданий, или null, если используется объект, не выполняющий действий [CardFakeTaskHistoryManager](T_Tessa_Cards_CardFakeTaskHistoryManager.htm). 
cardGetStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
(Optional)
     Стратегия, выполняющая низкоуровневую загрузку секций карточки, или null, если такая загрузка не поддерживается. Обычно требуется для создания групп в истории заданий совместно с объектом taskHistoryManager. 
workflowQueueProcessor
[IWorkflowQueueProcessor](T_Tessa_Cards_Workflow_IWorkflowQueueProcessor.htm)
(Optional)
     Объект, выполняющий обработку действий в очереди [WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm), или null, если используется обработчик по умолчанию. 
## __См. также
#### Ссылки
[WorkflowStoreExtension - ](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
