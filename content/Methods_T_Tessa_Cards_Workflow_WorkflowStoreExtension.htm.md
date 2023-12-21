# WorkflowStoreExtension - методы
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после сохранения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[BeforeCommitTransaction](M_Tessa_Cards_Workflow_WorkflowStoreExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
(Переопределяет
[CardStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeCommitTransaction.htm))  
[BeforeRequest](M_Tessa_Cards_Workflow_WorkflowStoreExtension_BeforeRequest.htm)|
Действие, выполняемое перед сохранением карточки стандартными средствами.
Может установить ответ на запрос для того, чтобы сохранение карточки
стандартными средствами не выполнялось.  
(Переопределяет
[CardStoreExtension.BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeRequest.htm))  
[CanHandleQueueItemAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CanHandleQueueItemAsync.htm)|
Возвращает признак того, что элемент очереди может быть обработан текущим
объектом. Чаще всего такая функция проверяет, что тип подпроцесса
item.Signal.ProcessTypeName соответствует текущему выполняемому расширению
процесса Workflow API.  
[CanStartProcessAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CanStartProcessAsync.htm)|
Возвращает признак того, что бизнес-процесс с заданным именем может быть
запущен посредством вызова метода [StartProcess]. При запуске бизнес-процесса
обычно отправляются задания и инициализируются счётчики.  
[CardIsAllowedAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CardIsAllowedAsync.htm)|
Возвращает признак того, что бизнес-процесс разрешён для заданной карточки.  
[CreateContextAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CreateContextAsync.htm)|
Создаёт контекст бизнес-процесса, используя контекст сохраняемой карточки.  
[CreateManagerAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CreateManagerAsync.htm)|
Создаёт объект, предоставляющий возможности по управлению бизнес-процессом.  
[CreateWorkerAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_CreateWorkerAsync.htm)|
Создаёт объект, реализующий логику подпроцессов и переходов в бизнес-процессе.  
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
[HandleUnknownTaskAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_HandleUnknownTaskAsync.htm)|
Выполняет обработку задания, для которого не удалось найти информацию в
бизнес-процессе. Возвращает признак того, что выполнение можно продолжить.
Добавляет ошибку в результат валидации и возвращает false, если выполнение
следует прервать.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ModifyCompletedTasksBeforeRequestAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_ModifyCompletedTasksBeforeRequestAsync.htm)|
Изменяет завершаемые задания перед их сохранением, если этого требует логика
бизнес-процесса Workflow.  
[StartProcessAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_StartProcessAsync.htm)|
Запускает бизнес-процесс с заданным именем на выполнение.  
[TaskIsAllowedAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_TaskIsAllowedAsync.htm)|
Возвращает признак того, что задание входит в бизнес-процесс. Рекомендуется
определять этот признак по типу задания.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnknownTaskIsAllowedAsync](M_Tessa_Cards_Workflow_WorkflowStoreExtension_UnknownTaskIsAllowedAsync.htm)|
Возвращает признак того, что задание, для которого не удалось найти информацию
в бизнес-процессе, не должно останавливать сохранение карточки с ошибкой. Чаще
всего такая ситуация возникает для заданий, которое уже было завершено в
параллельном сохранении (например, заместителем исполнителя в роли задания).
Рекомендуется оставить значение по умолчанию false для всех заданий, кроме
исключительных случаев.  
## __Методы расширения
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
[WorkflowStoreExtension - ](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
