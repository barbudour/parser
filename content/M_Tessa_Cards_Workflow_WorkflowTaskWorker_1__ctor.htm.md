# WorkflowTaskWorker<TManager> \- конструктор
Создаёт экземпляр класса с указанием значений его свойств.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected WorkflowTaskWorker(
    	TManager manager,
    	ICardRepository cardRepositoryToCreateTasks
    )
VB __Копировать
     Protected Sub New ( 
    	manager As TManager,
    	cardRepositoryToCreateTasks As ICardRepository
    )
C++ __Копировать
     protected:
    WorkflowTaskWorker(
    	TManager manager, 
    	ICardRepository^ cardRepositoryToCreateTasks
    )
F# __Копировать
     new : 
            manager : 'TManager * 
            cardRepositoryToCreateTasks : ICardRepository -> WorkflowTaskWorker
#### Параметры
manager [TManager](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm)
    Объект, предоставляющий возможности для управления бизнес-процессом.
cardRepositoryToCreateTasks
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий карточек, используемый для создания карточек заданий.
##  __См. также
#### Ссылки
[WorkflowTaskWorker<TManager> \-
](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
