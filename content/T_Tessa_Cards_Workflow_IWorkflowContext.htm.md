# IWorkflowContext - интерфейс
Контекст бизнес-процесса, содержащий информацию по сохраняемой карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowContext
VB __Копировать
     Public Interface IWorkflowContext
C++ __Копировать
     public interface class IWorkflowContext
F# __Копировать
     type IWorkflowContext = interface end
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
## __Методы
[NotifyNextRequestPending](M_Tessa_Cards_Workflow_IWorkflowContext_NotifyNextRequestPending.htm)|
Уведомляет о необходимости выполнить повторное сохранение карточки. Если метод
был вызван хотя бы раз, то свойство [IWorkflowContext.NextRequestPending]
вернёт значение true.  
---|---  
## __Методы расширения
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
