# WorkflowManager - методы
##  __Методы
[AddProcessAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddProcessAsync.htm)|
Добавляет информацию по подпроцессу.  
---|---  
[AddProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddProcessCoreAsync.htm)|
Добавляет информацию по заданному подпроцессу.  
[AddProcessToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddProcessToCacheAsync.htm)|
Добавляет информацию по подпроцессу в кэш. Если информация уже была добавлена,
то она будет замещена.  
[AddTaskAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddTaskAsync.htm)|
Добавляет информацию по заданию в список активных заданий. Метод следует
использовать при создании заданий, относящихся к бизнес-процессу.  
[AddTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddTaskCoreAsync.htm)|
Добавляет информацию по заданному заданию в список активных заданий.  
[AddTaskToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddTaskToCacheAsync.htm)|
Добавляет информацию по заданию в кэш. Если информация уже была добавлена, то
она будет замещена.  
[AddUnknownProcessToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddUnknownProcessToCacheAsync.htm)|
Добавляет в кэш информацию о том, что подпроцесс с заданным идентификатором
отсутствует.  
[AddUnknownTaskToCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_AddUnknownTaskToCacheAsync.htm)|
Добавляет в кэш информацию о том, что информация по заданному заданию
отсутствует.  
[CreateProcessInfoCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_CreateProcessInfoCoreAsync.htm)|
Метод, создающий информацию по подпроцессу для заданных параметров.  
[CreateTaskInfoCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_CreateTaskInfoCoreAsync.htm)|
Метод, создающий информацию по заданию в подпроцессе для заданных параметров.  
[DecrementCounterAsync](M_Tessa_Cards_Workflow_WorkflowManager_DecrementCounterAsync.htm)|
Уменьшает текущее значение счётчика на заданное значение decrementValue. Если
текущее значение становится не больше нуля, то счётчик удаляется. Возвращает
состояние счётчика после выполнения метода.  
[DecrementCounterCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_DecrementCounterCoreAsync.htm)|
Уменьшает текущее значение счётчика на заданное значение decrementValue. Если
текущее значение становится не больше нуля, то счётчик удаляется. Возвращает
состояние счётчика после выполнения метода.  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetWorkflowCardIDAsync](M_Tessa_Cards_Workflow_WorkflowManager_GetWorkflowCardIDAsync.htm)|
Асинхронно возвращает идентификатор карточки, в которой содержатся секции
бизнес-процесса.  
[InitCounterAsync](M_Tessa_Cards_Workflow_WorkflowManager_InitCounterAsync.htm)|
Инициализирует счётчик с заданным номером, уникальным для подпроцесса, и с
указанием начального значения. Счётчик используется для ожидания нескольких
параллельных заданий в бизнес-процессе.  
[InitCounterCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_InitCounterCoreAsync.htm)|
Инициализирует счётчик с заданным номером, уникальным для подпроцесса, и с
указанием начального значения. Счётчик используется для ожидания нескольких
параллельных заданий в бизнес-процессе.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyNextRequestPending](M_Tessa_Cards_Workflow_WorkflowManager_NotifyNextRequestPending.htm)|
Уведомляет о необходимости выполнить повторное сохранение карточки. Если метод
был вызван хотя бы раз, то свойство [IWorkflowContext.NextRequestPending]
вернёт значение true.  
[RemoveAwaitingProcessesAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveAwaitingProcessesAsync.htm)|
Удаляет все подпроцессы ProcessesAwaitingRemoval, ожидающие удаления после
выполнения всех действий на текущем этапе (т.е. обработки всех заданий и всех
сигналов из Request), но перед запуском вложенного сохранения NextRequest.
Подпроцессы удаляются в порядке, указанном в коллекции. Если один и тот же
подпроцесс указан несколько раз, то он будет удалён только один раз. После
выполнения метода коллекция очищается. Возвращается количество удалённых
подпроцессов или 0, если подпроцессы не будут удалены.  
[RemoveCounterAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveCounterAsync.htm)|
Удаляет счётчик с заданным номером, уникальным для подпроцесса.  
[RemoveCounterCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveCounterCoreAsync.htm)|
Удаляет счётчик с заданным номером, уникальным для подпроцесса.  
[RemoveProcessAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveProcessAsync.htm)|
Удаляет информацию по подпроцессу. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
[RemoveProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveProcessCoreAsync.htm)|
Удаляет информацию по подпроцессу. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
[RemoveProcessFromCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveProcessFromCacheAsync.htm)|
Удаляет из кэша информацию по подпроцессу с заданным идентификатором.  
[RemoveTaskAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveTaskAsync.htm)|
Удаляет заданное задание из списка активных заданий и возвращает информацию по
заданию или null, если задание неизвестно. Рекомендуется использовать при
завершении или отзыве задания.  
[RemoveTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveTaskCoreAsync.htm)|
Удаляет информацию по заданию из списка активных заданий.  
[RemoveTaskFromCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_RemoveTaskFromCacheAsync.htm)|
Удаляет из кэша информацию по заданному заданию.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetProcessAsync(Guid,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessAsync.htm)|
Возвращает информацию по подпроцессу с заданным идентификатором или null, если
подпроцесс не был найден.  
[TryGetProcessAsync(String,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessAsync_1.htm)|
Возвращает информацию по первому найденному подпроцессу с заданным именем типа
или null, если ни один подпроцесс подходящего типа не был найден.  
[TryGetProcessCoreAsync(Guid,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessCoreAsync.htm)|
Возвращает информацию по подпроцессу с заданным идентификатором или null, если
подпроцесс не был найден.  
[TryGetProcessCoreAsync(String,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessCoreAsync_1.htm)|
Возвращает информацию по первому найденному подпроцессу с заданным именем типа
или null, если ни один подпроцесс подходящего типа не был найден.  
[TryGetProcessFromCacheAsync(Guid,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessFromCacheAsync.htm)|
Возвращает информацию по подпроцессу в кэше или null, если информация
отсутствует в кэше.  
[TryGetProcessFromCacheAsync(String,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowManager_TryGetProcessFromCacheAsync_1.htm)|
Возвращает информацию по первому подпроцессу в кэше, имя типа которого равно
заданной строке typeName, или null, если подходящий подпроцесс отсутствует в
кэше.  
[TryGetTaskAsync](M_Tessa_Cards_Workflow_WorkflowManager_TryGetTaskAsync.htm)|
Возвращает информацию по заданию из списка активных заданий или null, если
задание отсутствовало в списке. Рекомендуется использовать для заданий,
завершение которых было отменено в расширениях.  
[TryGetTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_TryGetTaskCoreAsync.htm)|
Возвращает информацию по заданию из списка активных заданий или null, если
задание отсутствовало в списке. Рекомендуется использовать для заданий,
завершение которых было отменено в расширениях.  
[TryGetTaskFromCacheAsync](M_Tessa_Cards_Workflow_WorkflowManager_TryGetTaskFromCacheAsync.htm)|
Возвращает информацию по заданию в кэше или null, если информация отсутствует
в кэше.  
[UpdateProcessParametersAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateProcessParametersAsync.htm)|
Обновляет параметры подпроцесса. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
[UpdateProcessParametersCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateProcessParametersCoreAsync.htm)|
Обновляет параметры подпроцесса. Сбрасывает флаг
[Tessa.Cards.Workflow.IWorkflowProcessInfo.PendingProcessParametersUpdate].  
[UpdateTaskParametersAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateTaskParametersAsync.htm)|
Обновляет параметры задания (но не подпроцесса).  
[UpdateTaskParametersCoreAsync](M_Tessa_Cards_Workflow_WorkflowManager_UpdateTaskParametersCoreAsync.htm)|
Обновляет параметры задания (но не подпроцесса).  
##  __Методы расширения
[AddTask](M_Tessa_Cards_Workflow_WorkflowExtensions_AddTask.htm)|  Добавляет
задание в состоянии [Inserted](T_Tessa_Cards_CardRowState.htm) к следующей
сохраняемой карточке
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm).  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[WorkflowManager - ](T_Tessa_Cards_Workflow_WorkflowManager.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
