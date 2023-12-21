# Tessa.Cards.Workflow - пространство имён
API для реализации Workflow.
##  __Классы
[DefaultWorkflowQueueProcessor](T_Tessa_Cards_Workflow_DefaultWorkflowQueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
---|---  
[WorkflowContext](T_Tessa_Cards_Workflow_WorkflowContext.htm)|  Контекст
бизнес-процесса, содержащий информацию по сохраняемой карточке.  
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Cards.Workflow.  
[WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm)|  Объект,
предоставляющий возможности для управления бизнес-процессом. В классах-
наследниках могут быть переопределены методы объекта и добавлены свойства,
содержащие важные для бизнес-процесса значения.  
[WorkflowProcessInfo](T_Tessa_Cards_Workflow_WorkflowProcessInfo.htm)|
Информация по подпроцессу.  
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm)|  Очередь обработки
сигналов.  
[WorkflowQueueEventType](T_Tessa_Cards_Workflow_WorkflowQueueEventType.htm)|
Тип события по обработке сигнала в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
[WorkflowQueueEventTypeRegistry](T_Tessa_Cards_Workflow_WorkflowQueueEventTypeRegistry.htm)|
Реестр типов событий
[WorkflowQueueEventType](T_Tessa_Cards_Workflow_WorkflowQueueEventType.htm) по
обработке сигнала в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm). Класс является
синглтоном.  
[WorkflowQueueEventTypes](T_Tessa_Cards_Workflow_WorkflowQueueEventTypes.htm)|
Стандартные типы событий по обработке сигнала в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
[WorkflowQueueItem](T_Tessa_Cards_Workflow_WorkflowQueueItem.htm)|  Действие с
номером в очереди [WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
[WorkflowQueueProcessor](T_Tessa_Cards_Workflow_WorkflowQueueProcessor.htm)|
Базовый класс для объекта, выполняющего обработку действий в очереди с
номерами.  
[WorkflowQueueSignal](T_Tessa_Cards_Workflow_WorkflowQueueSignal.htm)|
Объект, сохраняющий информацию по сигналу
[IWorkflowSignal](T_Tessa_Cards_Workflow_IWorkflowSignal.htm).  
[WorkflowScopeContext](T_Tessa_Cards_Workflow_WorkflowScopeContext.htm)|
Контекст бизнес-процессов на Workflow API. Позволяет в процессе сохранения
получить информацию по родительскому контексту сохранения
[StoreContext](P_Tessa_Cards_Workflow_WorkflowScopeContext_StoreContext.htm),
а также по контексту Workflow API.  
[WorkflowSignal](T_Tessa_Cards_Workflow_WorkflowSignal.htm)|  Сигнал в
Workflow API. Обеспечивает взаимодействие с подпроцессом в произвольный момент
времени.  
[WorkflowSignalInfo](T_Tessa_Cards_Workflow_WorkflowSignalInfo.htm)|
Информация по сигналу, поступившему в подпроцесс.  
[WorkflowSignalType](T_Tessa_Cards_Workflow_WorkflowSignalType.htm)|  Тип
сигнала [IWorkflowSignal](T_Tessa_Cards_Workflow_IWorkflowSignal.htm).  
[WorkflowSignalTypeRegistry](T_Tessa_Cards_Workflow_WorkflowSignalTypeRegistry.htm)|
Реестр типов сигналов
[WorkflowSignalType](T_Tessa_Cards_Workflow_WorkflowSignalType.htm). Класс
является синглтоном.  
[WorkflowSignalTypes](T_Tessa_Cards_Workflow_WorkflowSignalTypes.htm)|
Стандартные типы сигналов в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm)|
Расширение, выполняющее взаимодействие с бизнес-процессом при сохранении
карточки.  
[WorkflowTaskInfo](T_Tessa_Cards_Workflow_WorkflowTaskInfo.htm)|  Информация
по заданию, которая содержится в списке активных заданий.  
[WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm)|
Базовый класс для объекта, реализующего логику подпроцессов и переходов в
бизнес-процессе с возможностью создавать задания.  
[WorkflowValidateThat](T_Tessa_Cards_Workflow_WorkflowValidateThat.htm)|
Предикаты для валидации значений в объектах, связанных со стандартным API
Workflow.  
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm)|
Базовый класс для объекта, реализующего логику подпроцессов и переходов в
бизнес-процессе.  
## __Интерфейсы
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm)|  Контекст
бизнес-процесса, содержащий информацию по сохраняемой карточке.  
---|---  
[IWorkflowManager](T_Tessa_Cards_Workflow_IWorkflowManager.htm)|  Объект,
предоставляющий возможности для управления бизнес-процессом.  
[IWorkflowProcessInfo](T_Tessa_Cards_Workflow_IWorkflowProcessInfo.htm)|
Информация по подпроцессу.  
[IWorkflowQueueEventTypeRegistry](T_Tessa_Cards_Workflow_IWorkflowQueueEventTypeRegistry.htm)|
Реестр типов событий
[WorkflowQueueEventType](T_Tessa_Cards_Workflow_WorkflowQueueEventType.htm) по
вызову действия с номером в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
[IWorkflowQueueProcessor](T_Tessa_Cards_Workflow_IWorkflowQueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди
[WorkflowQueue](T_Tessa_Cards_Workflow_WorkflowQueue.htm).  
[IWorkflowScopeContext](T_Tessa_Cards_Workflow_IWorkflowScopeContext.htm)|
Контекст бизнес-процессов на Workflow API. Позволяет в процессе сохранения
получить информацию по родительскому контексту сохранения
[StoreContext](P_Tessa_Cards_Workflow_IWorkflowScopeContext_StoreContext.htm),
а также по контексту Workflow API.  
[IWorkflowSignal](T_Tessa_Cards_Workflow_IWorkflowSignal.htm)|  Сигнал в
Workflow API. Обеспечивает взаимодействие с подпроцессом в произвольный момент
времени.  
[IWorkflowSignalInfo](T_Tessa_Cards_Workflow_IWorkflowSignalInfo.htm)|
Информация по сигналу, поступившему в подпроцесс.  
[IWorkflowSignalTypeRegistry](T_Tessa_Cards_Workflow_IWorkflowSignalTypeRegistry.htm)|
Реестр типов сигналов
[WorkflowSignalType](T_Tessa_Cards_Workflow_WorkflowSignalType.htm).  
[IWorkflowTaskInfo](T_Tessa_Cards_Workflow_IWorkflowTaskInfo.htm)|  Информация
по заданию, которая содержится в списке активных заданий.  
[IWorkflowWorker](T_Tessa_Cards_Workflow_IWorkflowWorker.htm)|  Объект,
реализующий логику подпроцессов и переходов в бизнес-процессе.  
## __Перечисления
[WorkflowCounterState](T_Tessa_Cards_Workflow_WorkflowCounterState.htm)|
Состояние счётчика после его декремента.  
---|---
