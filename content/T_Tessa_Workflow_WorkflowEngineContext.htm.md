# WorkflowEngineContext - класс
Контекст обработки процесса в WorkflowEngine.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowEngineContext : IWorkflowEngineContext, 
    	IExtensionContext, IAsyncDisposable
VB __Копировать
     Public NotInheritable Class WorkflowEngineContext
    	Implements IWorkflowEngineContext, IExtensionContext, IAsyncDisposable
C++ __Копировать
     public ref class WorkflowEngineContext sealed : IWorkflowEngineContext, 
    	IExtensionContext, IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type WorkflowEngineContext = 
        class
            interface IWorkflowEngineContext
            interface IExtensionContext
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineContext
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm)
##  __Конструкторы
[WorkflowEngineContext](M_Tessa_Workflow_WorkflowEngineContext__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineContext  
---|---  
##  __Свойства
[ActionInstance](P_Tessa_Workflow_WorkflowEngineContext_ActionInstance.htm)|
Текущий экземпляр действия.  
---|---  
[ActionTemplate](P_Tessa_Workflow_WorkflowEngineContext_ActionTemplate.htm)|
Шаблон действия.  
[AsyncRequests](P_Tessa_Workflow_WorkflowEngineContext_AsyncRequests.htm)|
Список асинхронных запросов, отправляемых при завершении обработки процесса.  
[Cancel](P_Tessa_Workflow_WorkflowEngineContext_Cancel.htm)|  Определяет,
требуется ли остановка обработки.  
[CancellationToken](P_Tessa_Workflow_WorkflowEngineContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[CardMetadata](P_Tessa_Workflow_WorkflowEngineContext_CardMetadata.htm)|
Метаданные карточек.  
[CardsScope](P_Tessa_Workflow_WorkflowEngineContext_CardsScope.htm)|  Скоуп
для загрузки карточек. Все загруженные или добавленные через него карточки, в
которых есть изменения, будут сохранены по окончанию обработки процесса
автоматически.  
[CommandSubscriptions](P_Tessa_Workflow_WorkflowEngineContext_CommandSubscriptions.htm)|
Список подписок команд. Заполняется в действиях.  
[Container](P_Tessa_Workflow_WorkflowEngineContext_Container.htm)|  Контейнер
зависимостей.  
[DbScope](P_Tessa_Workflow_WorkflowEngineContext_DbScope.htm)|  Объект,
обеспечивающий взаимодействие с базой данных.  
[EndSignals](P_Tessa_Workflow_WorkflowEngineContext_EndSignals.htm)|  Список
сигналов, отправляемых в родительский процесс при завершении обработки.  
[FileContainer](P_Tessa_Workflow_WorkflowEngineContext_FileContainer.htm)|
Контейнер файлов для обрабатываемой карточки. Устарел. Используйте вместо
этого
[GetFileContainerAsync(CancellationToken)](M_Tessa_Workflow_IWorkflowEngineContext_GetFileContainerAsync.htm)  
Устарело.  
[Info](P_Tessa_Workflow_WorkflowEngineContext_Info.htm)|  Дополнительная
информация.  
[InNonPersistentMode](P_Tessa_Workflow_WorkflowEngineContext_InNonPersistentMode.htm)|
Определяет, что выполнение процесса производится в неперсистентном режиме (в
памяти без сохранения в БД).  
[IsAsync](P_Tessa_Workflow_WorkflowEngineContext_IsAsync.htm)|  Определяет,
производится ли асинхронная обработка процесса.  
[IsMain](P_Tessa_Workflow_WorkflowEngineContext_IsMain.htm)|  Определяет,
является ли данный контекст основным.  
[IsMainCardLoaded](P_Tessa_Workflow_WorkflowEngineContext_IsMainCardLoaded.htm)|
Флаг, определяющий, загружена ли основная карточка.  
[KeepAlive](P_Tessa_Workflow_WorkflowEngineContext_KeepAlive.htm)|
Определяет, нужно ли сохранить состояние узла после его выполнения.  
[Links](P_Tessa_Workflow_WorkflowEngineContext_Links.htm)|  Список переходов
после выполнения ноды. Может быть изменен в процессе выполнения действий.  
[Logger](P_Tessa_Workflow_WorkflowEngineContext_Logger.htm)|  Объект для
логирования сообщений.  
[MainCard](P_Tessa_Workflow_WorkflowEngineContext_MainCard.htm)|  Карточка,
обрабатываемая процессом. Устарел. Используйте вместо этого
[GetMainCardAsync(CancellationToken)](M_Tessa_Workflow_IWorkflowEngineContext_GetMainCardAsync.htm)  
Устарело.  
[NodeInstance](P_Tessa_Workflow_WorkflowEngineContext_NodeInstance.htm)|
Текущий экземпляр узла.  
[NodeTemplate](P_Tessa_Workflow_WorkflowEngineContext_NodeTemplate.htm)|
Шаблон узла.  
[Parameters](P_Tessa_Workflow_WorkflowEngineContext_Parameters.htm)|  Список
параметров текущего обрабатываемого скрипта.  
[PreviousNode](P_Tessa_Workflow_WorkflowEngineContext_PreviousNode.htm)|
Предыдущий экземпляр узла.  
[ProcessInstance](P_Tessa_Workflow_WorkflowEngineContext_ProcessInstance.htm)|
Текущий экземпляр процесса.  
[ProcessTemplate](P_Tessa_Workflow_WorkflowEngineContext_ProcessTemplate.htm)|
Шаблон процесса.  
[ResponseInfo](P_Tessa_Workflow_WorkflowEngineContext_ResponseInfo.htm)|
Дополнительная информация, отправляемая в ответе на клиент.  
[SendParentProcessExitSignals](P_Tessa_Workflow_WorkflowEngineContext_SendParentProcessExitSignals.htm)|
Определяет, нужна ли отправка сигналов завершения подпроцесса в родительский
процесс.  
[Session](P_Tessa_Workflow_WorkflowEngineContext_Session.htm)|  Текущая
сессия.  
[Signal](P_Tessa_Workflow_WorkflowEngineContext_Signal.htm)|  Текущий сигнал.  
[StopPending](P_Tessa_Workflow_WorkflowEngineContext_StopPending.htm)|
Определяет, ожидает ли процесс остановки по окончанию обработки.  
[StoreCard](P_Tessa_Workflow_WorkflowEngineContext_StoreCard.htm)|
Сохраняемая карточка, обрабатываемая процессом.  
[StoreDateTime](P_Tessa_Workflow_WorkflowEngineContext_StoreDateTime.htm)|
Дата/время сохранения карточки.  
[SubprocessSubscriptions](P_Tessa_Workflow_WorkflowEngineContext_SubprocessSubscriptions.htm)|
Список подписок подпроцессов. Заполняется в действиях.  
[Task](P_Tessa_Workflow_WorkflowEngineContext_Task.htm)|  Первое задание из
списка обрабатываемых заданий
[Tasks](P_Tessa_Workflow_IWorkflowEngineContext_Tasks.htm) или null, если
список пуст.  
[Tasks](P_Tessa_Workflow_WorkflowEngineContext_Tasks.htm)|  Список
обрабатываемых заданий. Может быть пустым, но не может быть равным null.  
[TaskSubscriptions](P_Tessa_Workflow_WorkflowEngineContext_TaskSubscriptions.htm)|
Список подписок заданий. Заполняется в действиях.  
[TimerSubscriptions](P_Tessa_Workflow_WorkflowEngineContext_TimerSubscriptions.htm)|
Список подписок таймеров. Заполняется в действиях.  
[ValidationResult](P_Tessa_Workflow_WorkflowEngineContext_ValidationResult.htm)|
Билдер результата валидации.  
[WorkflowCardID](P_Tessa_Workflow_WorkflowEngineContext_WorkflowCardID.htm)|
Идентификатор карточки текущего процесса.  
[WorkflowService](P_Tessa_Workflow_WorkflowEngineContext_WorkflowService.htm)|
Сервис для управления экземплярами и подписками бизнес-процесса.  
## __Методы
[AddDisposableObject(IAsyncDisposable)](M_Tessa_Workflow_WorkflowEngineContext_AddDisposableObject.htm)|
Метод для добавления объекта, для которого будет вызван метод
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) при завершении обработки.  
---|---  
[AddDisposableObject(IDisposable)](M_Tessa_Workflow_WorkflowEngineContext_AddDisposableObject_1.htm)|
Метод для добавления объекта, для которого будет вызван метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) при завершении обработки.  
[AddLink](M_Tessa_Workflow_WorkflowEngineContext_AddLink.htm)|  Метод для
добавления перехода для обработки по его алиасу.  
[AddToExistingNodes](M_Tessa_Workflow_WorkflowEngineContext_AddToExistingNodes.htm)|
Метод для добавления экземпляра узла к списку существующих узлов процесса.  
[CheckNodeDeleted](M_Tessa_Workflow_WorkflowEngineContext_CheckNodeDeleted.htm)|
Метод для проверки наличия экземпляра узла среди удаленных.  
[CountAction](M_Tessa_Workflow_WorkflowEngineContext_CountAction.htm)|  Метод
для подсчета числа обработанных в рамках данного контекста действий.  
[CountDepth](M_Tessa_Workflow_WorkflowEngineContext_CountDepth.htm)|  Метод
для подсчета числа обработанных в рамках данной ветви исполнения узлов.  
[CountNode](M_Tessa_Workflow_WorkflowEngineContext_CountNode.htm)|  Метод для
подсчета числа обработанных в рамках данного контекста узлов.  
[CreateNextContext](M_Tessa_Workflow_WorkflowEngineContext_CreateNextContext.htm)|
Метод для создания дочернего контекста обработки процесса из текущего
контекста для нового процесса.  
[DisposeAsync](M_Tessa_Workflow_WorkflowEngineContext_DisposeAsync.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources asynchronously.  
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
[GetAllModifiedNodes](M_Tessa_Workflow_WorkflowEngineContext_GetAllModifiedNodes.htm)|
Возвращает список измененных узлов.  
[GetAllNewNodes](M_Tessa_Workflow_WorkflowEngineContext_GetAllNewNodes.htm)|
Возвращает список новых узлов.  
[GetAllRowsAsync(String[])](M_Tessa_Workflow_WorkflowEngineContext_GetAllRowsAsync_1.htm)|
Метод для получения списка с учетом вложенных в список привязок. Использует
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
из самого контекста.  
[GetAllRowsAsync(IDictionary<String, Object>,
String[])](M_Tessa_Workflow_WorkflowEngineContext_GetAllRowsAsync.htm)|  Метод
для получения списка строк с учетом вложенных в список привязок. Использует
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
из самого контекста.  
[GetAsync<T>(String[])](M_Tessa_Workflow_WorkflowEngineContext_GetAsync__1_1.htm)|
Метод для получения значения с учетом возможной привязки параметра. Использует
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
из самого контекста.  
[GetAsync<T>(IDictionary<String, Object>,
String[])](M_Tessa_Workflow_WorkflowEngineContext_GetAsync__1.htm)|  Метод для
получения значения с учетом возможной привязки параметра из указанного объекта
с данными. Использует
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
из самого контекста.  
[GetAsync<T>(String[], Int32,
String[])](M_Tessa_Workflow_WorkflowEngineContext_GetAsync__1_2.htm)|  Метод
для получения значения из элемента списка с учетом возможной привязки
параметра. Использует
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
из самого контекста.  
[GetCardAsync](M_Tessa_Workflow_WorkflowEngineContext_GetCardAsync.htm)|
Загружает карточку, имеющую указанный идентификатор. Если карточка не найдена
в скоупе карточек, то она загружается из БД.  
[GetContextState](M_Tessa_Workflow_WorkflowEngineContext_GetContextState.htm)|
Возвращает состояние контекста. В него входит информация о текущем стеке
выполнения и текущий сигнал.  
[GetDeletedNodes](M_Tessa_Workflow_WorkflowEngineContext_GetDeletedNodes.htm)|
Возвращает список удаленных узлов.  
[GetDeletedProcesses](M_Tessa_Workflow_WorkflowEngineContext_GetDeletedProcesses.htm)|
Возвращает список идентификаторов удаленных процессов.  
[GetExistingNodesAsync](M_Tessa_Workflow_WorkflowEngineContext_GetExistingNodesAsync.htm)|
Возвращает список загруженных экземпляров узлов по идентификатору шаблона
узла.  
[GetFileContainerAsync](M_Tessa_Workflow_WorkflowEngineContext_GetFileContainerAsync.htm)|
Метод для получения файлового контейнера основной карточки.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMainCardAsync](M_Tessa_Workflow_WorkflowEngineContext_GetMainCardAsync.htm)|
Метод для получения основной карточки. Метод загружает карточку с сервера,
если она еще не была загружена.  
[GetMainCardSatelliteAsync](M_Tessa_Workflow_WorkflowEngineContext_GetMainCardSatelliteAsync.htm)|
Возвращает карточку сателлита.  
[GetModifiedProcesses](M_Tessa_Workflow_WorkflowEngineContext_GetModifiedProcesses.htm)|
Возвращает список измененных процессов.  
[GetNewProcesses](M_Tessa_Workflow_WorkflowEngineContext_GetNewProcesses.htm)|
Возвращает список новых процессов.  
[GetRowAsync(String[],
Int32)](M_Tessa_Workflow_WorkflowEngineContext_GetRowAsync_1.htm)|  Метод для
получения списка строк с учетом вложенных в строку привязок. Использует
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
из самого контекста.  
[GetRowAsync(IDictionary<String, Object>, String[],
Int32)](M_Tessa_Workflow_WorkflowEngineContext_GetRowAsync.htm)|  Метод для
получения списка строк с учетом вложенных в строку привязок. Использует
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
из самого контекста.  
[GetTaskAsync](M_Tessa_Workflow_WorkflowEngineContext_GetTaskAsync.htm)|
Метод для получения объекта задания карточки по его идентификатору. Возвращает
задание из сохраняемой карточки, если оно там есть, иначе из основной
карточки.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[KeepNode](M_Tessa_Workflow_WorkflowEngineContext_KeepNode.htm)|  Метод для
установки факта, что состояние текущего обрабатываемого экземпляра узла должно
быть сохранено.  
[LogDebugAsync](M_Tessa_Workflow_WorkflowEngineContext_LogDebugAsync.htm)|
Метод для записи сообщения с уровнем Debug в лог процесса.  
[LogErrorAsync](M_Tessa_Workflow_WorkflowEngineContext_LogErrorAsync.htm)|
Метод для записи сообщения с уровнем Error в лог процесса.  
[LogInfoAsync](M_Tessa_Workflow_WorkflowEngineContext_LogInfoAsync.htm)|
Метод для записи сообщения с уровнем Info в лог процесса.  
[MarkNodeDeleted](M_Tessa_Workflow_WorkflowEngineContext_MarkNodeDeleted.htm)|
Метод для помечания текущего экземпляра узла как удалённого.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ModifyStoreRequest(Action<CardStoreRequest>)](M_Tessa_Workflow_WorkflowEngineContext_ModifyStoreRequest.htm)|
Метод для отложенной модификации запроса на сохранение основной карточки.  
[ModifyStoreRequest(CardStoreRequest)](M_Tessa_Workflow_WorkflowEngineContext_ModifyStoreRequest_1.htm)|
Метод для модификации запроса на сохранения с помощью отложенных методов,
добавленных
[ModifyStoreRequest(Action<CardStoreRequest>)](M_Tessa_Workflow_IWorkflowEngineContext_ModifyStoreRequest.htm).  
[SendTaskAsync](M_Tessa_Workflow_WorkflowEngineContext_SendTaskAsync.htm)|
Метод для отправки задания для основной карточки в рамках выполнения процесса.  
[SetAction](M_Tessa_Workflow_WorkflowEngineContext_SetAction.htm)|  Метод для
установки текущего обрабатываемого действия.  
[SetLink](M_Tessa_Workflow_WorkflowEngineContext_SetLink.htm)|  Метод для
установки текущей связи.  
[SetMainCard](M_Tessa_Workflow_WorkflowEngineContext_SetMainCard.htm)|  Метод
для установки новой карточки как основной.  
[SetNode](M_Tessa_Workflow_WorkflowEngineContext_SetNode.htm)|  Метод для
установки текущего экземпляра узла.  
[SetProcess](M_Tessa_Workflow_WorkflowEngineContext_SetProcess.htm)|  Метод
для установки обрабатываемого процесса в контекст.  
[SetSignal](M_Tessa_Workflow_WorkflowEngineContext_SetSignal.htm)|  Метод для
установки текущего сигнала.  
[StopProcess](M_Tessa_Workflow_WorkflowEngineContext_StopProcess.htm)|  Метод
для остановки процесса.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TrySetNotPersistentMode](M_Tessa_Workflow_WorkflowEngineContext_TrySetNotPersistentMode.htm)|
Метод для осуществление попытки перехода выполнения процесса в неперсистентный
режим, или выхода из него.  
## __Методы расширения
[AddActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_AddActiveTaskAsync.htm)|
Добавляет указанный идентификатор задания в список активных заданий.  
(Определяется
[WorkflowEngineContextExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension.htm))  
---|---  
[AddToHistoryAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_AddToHistoryAsync.htm)|
Добавляет в историю процесса запись о задании.  
(Определяется
[WorkflowEngineContextExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension.htm))  
[CreatePlaceholderInfo](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_CreatePlaceholderInfo.htm)|
Метод для создания объекта с дополнительний информацией для контекста
плейсхолдеров из контекста обработки бизнес-процессов.  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
[CreatePlaceholderInfoWithoutTask](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_CreatePlaceholderInfoWithoutTask.htm)|
Метод для создания объекта с дополнительний информацией для контекста
плейсхолдеров из контекста обработки бизнес-процессов без передачи информации
о задании.  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetActiveTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_GetActiveTasksAsync.htm)|
Возвращает доступную только для чтения коллекцию идентификаторов активных
заданий.  
(Определяется
[WorkflowEngineContextExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension.htm))  
[GetAuthorIDAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_GetAuthorIDAsync.htm)|
Возвращает идентификатор роли автора задания.  
(Определяется
[WorkflowEngineContextExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension.htm))  
[GetKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_GetKrSatelliteAsync.htm)|
Возвращает карточку основного сателлита
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm).  
(Определяется
[WorkflowEngineContextExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SendEditInterjectTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_SendEditInterjectTaskAsync.htm)|
Асинхронно отправляет задание доработки автором
([KrEditInterjectTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrEditInterjectTypeID.htm)).
Параметры задания берутся из секции
[SectionName](F_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowConstants_KrWeEditInterjectOptionsVirtual_SectionName.htm).  
(Определяется
[WorkflowEngineContextExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[TryRemoveActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension_TryRemoveActiveTaskAsync.htm)|
Удаляет указанный идентификатор задания из списка активных заданий.  
(Определяется
[WorkflowEngineContextExtension](T_Tessa_Extensions_Default_Server_Workflow_WorkflowEngine_WorkflowEngineContextExtension.htm))  
##  __См. также
#### Ссылки
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
