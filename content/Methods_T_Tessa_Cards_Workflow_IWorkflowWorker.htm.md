# IWorkflowWorker - методы
##  __Методы
[CompleteTaskAsync](M_Tessa_Cards_Workflow_IWorkflowWorker_CompleteTaskAsync.htm)|
Выполняет действие при завершении заданного задания. Не удаляет запись с
информацией по заданию, т.к. задание может завершаться без удаления записи.  
---|---  
[ProcessSignalAsync](M_Tessa_Cards_Workflow_IWorkflowWorker_ProcessSignalAsync.htm)|
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
[ReinstateTaskAsync](M_Tessa_Cards_Workflow_IWorkflowWorker_ReinstateTaskAsync.htm)|
Выполняет действие при возврате на роль заданного задания. Не удаляет запись с
информацией по заданию.  
[RenderStepAsync](M_Tessa_Cards_Workflow_IWorkflowWorker_RenderStepAsync.htm)|
Выполняет переход к состоянию с заданным номером.  
[StartProcessAsync](M_Tessa_Cards_Workflow_IWorkflowWorker_StartProcessAsync.htm)|
Выполняет действие при старте подпроцесса с уникальным именем типа и
параметрами. Создаёт запись с информацией по подпроцессу.  
[StopProcessAsync](M_Tessa_Cards_Workflow_IWorkflowWorker_StopProcessAsync.htm)|
Выполняет действие при завершении заданного подпроцесса. Удаляет запись с
информацией по подпроцессу.  
## __См. также
#### Ссылки
[IWorkflowWorker - ](T_Tessa_Cards_Workflow_IWorkflowWorker.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
