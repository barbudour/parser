# WorkflowTaskWorker<TManager> \- методы
##  __Методы
[AddNewTaskAsync](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_AddNewTaskAsync.htm)|
Создаёт и добавляет задание в запрос на дополнительное сохранение карточки.  
---|---  
[AddTaskToProcessInfo(IWorkflowProcessInfo,
IEnumerable<Guid>)](M_Tessa_Cards_Workflow_WorkflowWorker_1_AddTaskToProcessInfo.htm)|
Добавляет идентификаторы заданий к списку заданий в подпроцессе.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[AddTaskToProcessInfo(IWorkflowProcessInfo,
Guid)](M_Tessa_Cards_Workflow_WorkflowWorker_1_AddTaskToProcessInfo_1.htm)|
Добавляет идентификатор задания к списку заданий в подпроцессе.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[CompleteTaskAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_CompleteTaskAsync.htm)|
Выполняет действие при завершении заданного задания. Не удаляет запись с
информацией по заданию, т.к. задание может завершаться без удаления записи.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[CompleteTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_CompleteTaskCoreAsync.htm)|
Выполняет действие при завершении заданного задания.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
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
[GetTaskCount](M_Tessa_Cards_Workflow_WorkflowWorker_1_GetTaskCount.htm)|
Возвращает количество заданий, о которых известно в подпроцессе.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[GetTaskHistoryGroupsAsync](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_GetTaskHistoryGroupsAsync.htm)|
Загружает секцию карточки с идентификатором Manager.Request.Card.ID с группами
в истории, которые требуются для создания новых групп в истории. Возвращённое
значение не равно null даже в случае ошибок. Вызов метода не приводит к
изменению карточек в запросах Manager.Request и Manager.NextRequest.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasTasks](M_Tessa_Cards_Workflow_WorkflowWorker_1_HasTasks.htm)|  Возвращает
признак того, что в подпроцессе присутствует хотя бы одно известное задание.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ProcessSignalAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ProcessSignalAsync.htm)|
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
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ProcessSignalCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ProcessSignalCoreAsync.htm)|
Выполняет действие по обработке сигнала. Возвращает признак того, что сигнал
был ожидаем и обработан (необязательно успешно). Необработанный сигнал по
умолчанию не приводит к ошибке сохранения карточки и не приводит к откату
транзакции, но не помечается как обработанный в очереди. По умолчанию все
сигналы считаются необработанными. Необработанное исключение, возникшее в
обработчике, также отмечает сигнал как необработанный. Если для ожидаемого
сигнала требуется прервать транзакцию, то добавьте ошибку в
Manager.ValidationResult, но верните в методе true.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ReinstateTaskAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ReinstateTaskAsync.htm)|
Выполняет действие при возврате на роль заданного задания. Не удаляет запись с
информацией по заданию.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ReinstateTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ReinstateTaskCoreAsync.htm)|
Выполняет действие при возврате задания на роль.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RemoveTaskFromProcessInfo(IWorkflowProcessInfo,
IEnumerable<Guid>)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RemoveTaskFromProcessInfo.htm)|
Удаляет идентификаторы заданий из списка заданий в подпроцессе. Возвращает
количество идентификаторов, которые присутствовали в списке заданий и были
удалены.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RemoveTaskFromProcessInfo(IWorkflowProcessInfo,
Guid)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RemoveTaskFromProcessInfo_1.htm)|
Удаляет идентификатор задания из списка заданий в подпроцессе. Возвращает
признак того, что идентификатор там был, после чего был удалён.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RenderStepAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_RenderStepAsync.htm)|
Выполняет переход к состоянию с заданным номером.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[RenderStepCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_RenderStepCoreAsync.htm)|
Выполняет переход к состоянию с заданным номером.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ResolveTaskHistoryGroupAsync](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_ResolveTaskHistoryGroupAsync.htm)|
Возвращает группу в истории заданий, вычисленную для заданных параметров. При
необходимости группа будет создана.  
[SendTaskAsync(Guid, IWorkflowProcessInfo, String, Dictionary<String, Object>,
Nullable<Guid>, Func<CardTask, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_SendTaskAsync.htm)|
Создаёт и отправляет задание заданного типа с указанными параметрами от имени
текущего пользователя.  
[SendTaskAsync(Guid, IWorkflowProcessInfo, String, Guid, String,
Dictionary<String, Object>, Nullable<Guid>, Func<CardTask, CancellationToken,
ValueTask>,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowTaskWorker_1_SendTaskAsync_1.htm)|
Создаёт и отправляет задание заданного типа с указанными параметрами.  
[StartProcessAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartProcessAsync.htm)|
Выполняет действие при старте подпроцесса с уникальным именем типа и
параметрами. Создаёт запись с информацией по подпроцессу.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StartProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartProcessCoreAsync.htm)|
Выполняет действие при старте подпроцесса с уникальным именем типа и
параметрами.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StartSubProcessWithCompletionAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartSubProcessWithCompletionAsync.htm)|
Запускает подпроцесс, который выполняет указанный переход при завершении.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StopProcessAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopProcessAsync.htm)|
Выполняет действие при завершении заданного подпроцесса. Удаляет запись с
информацией по подпроцессу.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StopProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopProcessCoreAsync.htm)|
Выполняет действие при завершении заданного подпроцесса.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[StopSubProcessWithCompletionAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopSubProcessWithCompletionAsync.htm)|
Завершает подпроцесс, выполняя переход, указанный при запуске подпроцесса
методом [StartSubProcessWithCompletionAsync(String, Int32,
IWorkflowProcessInfo, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartSubProcessWithCompletionAsync.htm).  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetTasksFromProcessInfo](M_Tessa_Cards_Workflow_WorkflowWorker_1_TryGetTasksFromProcessInfo.htm)|
Возвращает массив идентификаторов заданий, о которых известно в подпроцессе,
или null, если таких заданий не существует.  
(Унаследован от
[WorkflowWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowWorker_1.htm))  
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
[WorkflowTaskWorker<TManager> \-
](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
