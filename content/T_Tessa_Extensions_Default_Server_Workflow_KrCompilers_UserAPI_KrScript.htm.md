# KrScript - класс
Абстрактный класс предоставляющий свойства и методы доступные в скриптах
маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrScript : IKrScript, 
    	ISealable, IKrProcessItemScript, IKrProcessExecutionScript, IKrProcessVisibilityScript, IContextChangeableScript, 
    	IExtensionContext
VB __Копировать
     Public MustInherit Class KrScript
    	Implements IKrScript, ISealable, IKrProcessItemScript, IKrProcessExecutionScript, 
    	IKrProcessVisibilityScript, IContextChangeableScript, IExtensionContext
C++ __Копировать
     public ref class KrScript abstract : IKrScript, 
    	ISealable, IKrProcessItemScript, IKrProcessExecutionScript, IKrProcessVisibilityScript, IContextChangeableScript, 
    	IExtensionContext
F# __Копировать
     [<AbstractClassAttribute>]
    type KrScript = 
        class
            interface IKrScript
            interface ISealable
            interface IKrProcessItemScript
            interface IKrProcessExecutionScript
            interface IKrProcessVisibilityScript
            interface IContextChangeableScript
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrScript
Implements
    [IContextChangeableScript](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IContextChangeableScript.htm), [IKrProcessExecutionScript](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessExecutionScript.htm), [IKrProcessItemScript](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript.htm), [IKrProcessVisibilityScript](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessVisibilityScript.htm), [IKrScript](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrScript.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[KrScript](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript__ctor.htm)|
Инициализирует новый экземпляр класса KrScript  
---|---  
##  __Свойства
[Action](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Action.htm)|
Возвращает информацию о конфигурации текущего действия.  
---|---  
[Button](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Button.htm)|
Возвращает кнопку, по нажатию на которую был запущен текущий процесс.  
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CanChangeOrder.htm)|
Возвращает или задаёт значение, показывающее, можно ли менять порядок этапов
шаблона.  
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardCache.htm)|
Потокобезопасный кэш с карточками и дополнительными настройками.  
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardContext.htm)|
Возвращает или задаёт контекст расширения, в рамках которого выполняется этап.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardID.htm)|
Возвращает или задаёт идентификатор текущей карточки документа.  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardMetadata.htm)|
Содержит метаинформацию, необходимую для использования типов карточек
совместно с пакетом карточек.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardType.htm)|
Возвращает или задаёт тип текущей карточки.  
[CardTypeCaption](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardTypeCaption.htm)|
Возвращает отображаемое название типа текущей карточки документа.  
[CardTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardTypeID.htm)|
Возвращает идентификатор типа текущей карточки документа.  
[CardTypeName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardTypeName.htm)|
Возвращает название типа текущей карточки документа.  
[Confirmed](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Confirmed.htm)|
Признак того, что выполняемый элемент подтвержден условием построения.  
[CurrentStages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CurrentStages.htm)|
Возвращает подмножество этапов, относящееся только к текущему скрипту. Для
скрипта выполнения этапа - это коллекция из одного текущего этапа. Для скрипта
построения шаблона этапов - это коллекция из всех этапов текущего шаблона. Для
скрипта построения и выполнения группы этапов - это коллекция из все этапов
текущей группы. Коллекция является неизменяемой. Если необходимо добавить
этап, то следует воспользоваться методов [AddStageAsync(String,
StageTypeDescriptor,
Int32)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrScript_AddStageAsync.htm).
В случае, когда нужно удалить этап, достаточно выполнить
Stages.RemoveAll(Predicate); Этапы в данной коллекции являются изменяемыми.  
[Db](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Db.htm)|
Объект, используемый для выполнения SQL-запросов к текущей БД. По умолчанию
уже открыто соединение к основной БД системы, но посредством вызова using
(DbScope.CreateNew("connectionAlias")) { ... } можно изменить базу данных,
доступную по свойству
[Db](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrScript_Db.htm),
может быть изменена. Пример выполнения запроса: int result =
Db.SetCommand("select @Result", Db.Parameter("Result",
42)).LogCommand().ExecuteScalar<int>(). Следует учесть, что
Db.Parameter("Result", 0) ведет себя нелогично и определит параметр типа
nvarchar со значением DbNull, т.к. будет использована некорректная перегрузка
метода Db.Parameter(). В связи с этим добавьте преобразование типа значения к
object: Db.Parameter("Result", (object)0).  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_DbScope.htm)|
Объект, обеспечивающий доступ к базам данных. Позволяет открывать соединение к
другим БД: using (DbScope.CreateNew("connectionAlias")) { ... }. Также
определяет тип СУБД, которая используется системой: DbScope.GetDbmsAsync.
Вместо вызова DbScope.Db для простоты рекомендуется использоваться свойство
[Db](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrScript_Db.htm).  
[DifferentContextCardID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_DifferentContextCardID.htm)|
Идентификатор контекста, в котором необходимо выполнить этап вместо текущего.  
[DifferentContextProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_DifferentContextProcessInfo.htm)|
Дополнительная информация о процессе, выполняемом в другом контексте.  
[DifferentContextSetupScriptType](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_DifferentContextSetupScriptType.htm)|
Место, где был установлен признак выполнения в другом контексте.  
[DifferentContextWholeCurrentGroup](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_DifferentContextWholeCurrentGroup.htm)|
Признак того, что необходимо выполнить в контексте карточки
[DifferentContextCardID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IContextChangeableScript_DifferentContextCardID.htm)
всю группу.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_DocTypeID.htm)|
Возвращает или задаёт идентификатор типа документа для текущей карточки, если
тип карточки поддерживает типы документов.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Info.htm)|
Возвращает произвольное хранилище для пользовательских данных. Не является
персистентным хранилищем, срок жизни не регламентируется.  
[InitialStages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_InitialStages.htm)|
Возвращает набор этапов на момент начала текущей обработки запроса подсистемой
маршрутов. Используется для поиска изменений в маршруте за время обработки
запроса. Использовать в скриптах напрямую не рекомендуется.  
[InitiationCause](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_InitiationCause.htm)|
Возвращает или задаёт причину запуска обработчика процесса.  
[Initiator](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Initiator.htm)|
Возвращает или задаёт инициатора (автора) основного процесса.  
[InitiatorComment](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_InitiatorComment.htm)|
Возвращает или задаёт комментарий инициатора основного процесса.  
[IsSealed](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[IsStagesReadonly](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_IsStagesReadonly.htm)|
Возвращает или задаёт значение, показывающее, можно ли менять настройки этапов
в шаблоне.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_KrComponents.htm)|
Возвращает или задаёт включенные настройки типового решения для текущей
карточки.  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_KrScope.htm)|
Объект для работы с текущим контекстом расширений типового расширения и
использования разделяемых объектов карточек.  
[KrScriptType](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_KrScriptType.htm)|
Текущее выполняемое действие.  
[KrTypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_KrTypesCache.htm)|
Кэш по типам карточек и документов, содержащих информацию по типовому решению.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_MainCardAccessStrategy.htm)|
Возвращает или задаёт стратегия загрузки основной карточки.  
[MainProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_MainProcessInfo.htm)|
Возвращает dynamic-обёртку над хранилищем Info основного процесса текущей
карточки.  
[MainProcessInfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_MainProcessInfoStorage.htm)|
Возвращает хранилище Info основного процесса текущей карточки.  
[Order](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Order.htm)|
Возвращает или задаёт порядок сортировки шаблона этапов. -1 если выполнение
происходит без конкретного шаблона.  
[Position](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Position.htm)|
Возвращает или задаёт значение определяющее положение относительно этапов,
добавленных вручную.  
[ProcessHolderSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ProcessHolderSatellite.htm)|
Возвращает или задаёт процессный сателлит для текущего процесса. Процессный
сателлит содержит в себе список этапов с секции KrStages с состояниями и
настройками. Для основного процесса процессный сателлит совпадает с
контекстуальным  
[ProcessID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ProcessID.htm)|
Возвращает или задаёт идентификатор текущего процесса.  
[ProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ProcessInfo.htm)|
Возвращает dynamic-обёртку состояния (Info) процесса. Представляет из себя
персистентное хранилище произвольных данных о процессе. Может использоваться
различными этапами для взаимодействия между собой. Пример использования:
ProcessInfo.CustomField = 5  
[ProcessInfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ProcessInfoStorage.htm)|
Возвращает хранилище состояния (Info) процесса. Представляет из себя
персистентное хранилище произвольных данных о процессе. Может использоваться
различными этапами для взаимодействия между собой. Пример использования:
ProcessInfoStorage["CustomField"] = 5  
[ProcessOwner](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ProcessOwner.htm)|
Возвращает или задаёт владельца основного процесса.  
[ProcessTypeName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ProcessTypeName.htm)|
Возвращает или задаёт тип текущего процесса.  
[PureProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_PureProcess.htm)|
Возвращает информацию о конфигурации текущего вторичного процесса.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_SecondaryProcess.htm)|
Возвращает или задаёт информацию о конфигурации текущего вторичного процесса.  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Session.htm)|
Сессия текущего пользователя. Используйте Session.User.ID, чтобы получить
идентификатор текущего пользователя.  
[Stage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Stage.htm)|
Возвращает или задаёт текущий этап.  
[StageGroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_StageGroupID.htm)|
Возвращает или задаёт идентификатор группы этапов для текущего скрипта.  
[StageGroupName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_StageGroupName.htm)|
Возвращает или задаёт название текущей группы этапов.  
[StageGroupOrder](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_StageGroupOrder.htm)|
Возвращает или задаёт порядок сортировки текущей группы этапов.  
[StageInfo](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_StageInfo.htm)|
Возвращает dynamic-обёртку состояния (Info) текущего этапа. Представляет из
себя персистентное хранилище произвольных данных об этапе. Может
использоваться скриптами и обработчиком этапа для хранения данных между
вызовами. Пример использования: StageInfo.CustomField = 5  
[StageInfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_StageInfoStorage.htm)|
Возвращает хранилище состояния (Info) текущего этапа. Представляет из себя
персистентное хранилище произвольных данных об этапе. Может использоваться
скриптами и обработчиком этапа для хранения данных между вызовами. Пример
использования: StageInfoStorage["CustomField"] = 5  
[Stages](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Stages.htm)|
Список этапов в маршруте.  
[StagesContainer](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_StagesContainer.htm)|
Возвращает или задаёт контейнер этапов, выполняющий составление маршрута и
сортировку маршрутов при пересчете. Использовать в скриптах напрямую не
рекомендуется.  
[StageSerializer](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_StageSerializer.htm)|
Сериализатор этапов.  
[TaskHistoryManager](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_TaskHistoryManager.htm)|
Текущий используемый менеджер истории заданий.  
[TaskHistoryResolver](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_TaskHistoryResolver.htm)|
Объект для работы с группами истории заданий.  
[TemplateID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_TemplateID.htm)|
Возвращает или задаёт идентификатор текущего шаблона этапов.  
[TemplateName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_TemplateName.htm)|
Возвращает или задаёт название текущего шаблона этапов.  
[TypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_TypeID.htm)|
Возвращает эффективный идентификатор типа. Это тип документа, если типы
документов включены для типа карточки, иначе тип карточки.  
[UnityContainer](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_UnityContainer.htm)|
IoC-контейнер для получения любых необходимых зависимостей в рамках системы.
Для более удобного использования есть метод Resolve<T>, о котором написано
ниже. Пример использования: var cardRepository =
UnityContainer.Resolve<ICardRepository>().  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ValidationResult.htm)|
Возвращает или задаёт результат валидации текущей обработки запроса.  
[WorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_WorkflowProcess.htm)|
Возвращает или задаёт объектную модель текущего процесса. Содержит полное
представление процесса, основанное на контекстуальном и процессном сателлитах.  
[WorkflowProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_WorkflowProcessInfo.htm)|
Возвращает или задаёт информацию о процессе из WorkflowAPI.  
[WorkflowSignalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_WorkflowSignalInfo.htm)|
Возвращает информацию о сигнале из WorkflowAPI.  
[WorkflowTaskInfo](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_WorkflowTaskInfo.htm)|
Возвращает информацию о задании из WorkflowAPI.  
## __Методы
[AddError](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddError.htm)|
Добавить сообщение в ValidationResult с уровнем Error.  
---|---  
[AddInfo](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddInfo.htm)|
Добавить сообщение в ValidationResult с уровнем Info.  
[AddPerformer(Guid, String, Stage, Int32,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddPerformer.htm)|
Добавляет исполнителя в этап с режимом множественных исполнителей
[Multiple](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).
Исполнитель будет добавлен только если на указанном месте для вставки стоит
другой исполнитель.  
[AddPerformer(String, String, Stage, Int32,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddPerformer_1.htm)|
Добавляет исполнителя для этапа с режимом множественных исполнителей
[Multiple](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).
Исполнитель будет добавлен только если на указанном месте для вставки стоит
другой исполнитель.  
[AddStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddStageAsync.htm)|
Добавляет новый этап в маршрут.  
[AddTaskHistoryRecordAsync(Guid, String, String, Guid, String, Nullable<Guid>,
String, Nullable<Int32>, Nullable<Int32>, Nullable<TimeSpan>,
Func<CardTaskHistoryItem,
ValueTask>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddTaskHistoryRecordAsync.htm)|
Асинхронно добавляет запись в текущую группу истории заданий.  
[AddTaskHistoryRecordAsync(Nullable<Guid>, Guid, String, String, Guid, String,
Nullable<Guid>, String, Nullable<Int32>, Nullable<Int32>, Nullable<TimeSpan>,
Func<CardTaskHistoryItem,
ValueTask>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddTaskHistoryRecordAsync_1.htm)|
Асинхронно добавляет запись в указанную группу истории заданий.  
[AddWarning](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AddWarning.htm)|
Добавить сообщение в ValidationResult с уровнем Warning.  
[AfterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_AfterAsync.htm)|
Сценарий постобработки.  
[BeforeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_BeforeAsync.htm)|
Сценарий инициализации.  
[CardRowsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_CardRowsAsync.htm)|
Возвращает строго типизированную коллекцию строк из секции основной карточки.  
[ConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ConditionAsync.htm)|
Сценарий C#-условия.  
[ContextChangePending](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ContextChangePending.htm)|
Смена контекста запланирована с помощью метода
[RunNextStageInContextAsync(Guid, Boolean, IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrScript_RunNextStageInContextAsync.htm)  
[DoNotChangeContext](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_DoNotChangeContext.htm)|
Отменить смену контекста.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecutionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ExecutionAsync.htm)|
Метод содержащий условие выполнимости процесса.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ForEachStage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ForEachStage.htm)|
Выполняет указанное действие над строкой (из коллекционной секции KrStages)
этапа текущего процесса в обход объектной модели. Секция KrStages получается
из ProcessHolder-сателлита.  
[ForEachStageInMainProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ForEachStageInMainProcessAsync.htm)|
Асинхронно выполняет указанное действие над строкой (из коллекционной секции
KrStages) этапа основного процесса карточки в обход объектной модели. Секция
KrStages получается из контекстуального сателлита.  
[GetCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetCardAsync.htm)|
Асинхронно возвращает dynamic-обёртку над строковыми секциями карточки
документа. Может использоваться для простого и лаконичного обращения к
строковым секциями.  
Например:  
Card.DocumentCommonInfo.Amount  
Card.MyCustomSection.CustomField  
[GetCardObjectAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetCardObjectAsync.htm)|
Асинхронно возвращает полный объект текущей карточки документа.  
[GetCardTablesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetCardTablesAsync.htm)|
Асинхронно возвращает dynamic-обёртку над коллекционными секциями карточки
документа. Может использоваться для простого и лаконичного обращения к
коллекционным секциями.  
Например:  
Card.Performers[0].UserID  
[GetContextualSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetContextualSatelliteAsync.htm)|
Асинхронно возвращает контекстуальный сателлит
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm)
текущей карточки. Данный сателлит является основным сателлитом для карточки в
подсистеме маршрутов, содержит состояние карточки и инициатора, а также
маршрут для вкладки "Маршруты" (т.е. контекстуальный сателлит по
совместительству процессный для основного процесса).  
[GetCurrentTaskHistoryGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetCurrentTaskHistoryGroupAsync.htm)|
Асинхронно возвращает идентификатор текущей группы истории заданий.  
[GetCycleAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetCycleAsync.htm)|
Асинхронно возвращает номер текущего цикла. Является прокси для поля в
ProcessInfo.Cycle основного процесса. В вторичных процессах каждое обращение
вызывает сериализацию/десериализацию состояния основного процесса, поэтому
следует минимизировать обращения к данному методу.  
[GetFilesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetFilesAsync.htm)|
Асинхронно возвращает список файлов карточки.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNewCardAccessStrategy](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetNewCardAccessStrategy.htm)|
Возвращает стратегию загрузки карточки, получаемой из
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Info.htm)
этапа по ключу
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).  
[GetNewCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetNewCardAsync.htm)|
Асинхронно возвращает карточку из
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Info.htm)
этапа по ключу
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).  
[GetOrAddStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetOrAddStageAsync.htm)|
Возвращает или добавляет новый этап в маршрут, если он отсутствует в маршруте.  
[GetPrimaryProcessInfoAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetPrimaryProcessInfoAsync.htm)|
Асинхронно возвращает хранилище Info для основного процесса карточки.  
[GetProcessInfoForBranch(Guid)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetProcessInfoForBranch.htm)|
Возвращает хранилище Info ветки вторичного процесса перед стартом. Актуально
только для этапа ветвления.  
[GetProcessInfoForBranch(String)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetProcessInfoForBranch_1.htm)|
Возвращает хранилище Info ветки вторичного процесса перед стартом. Актуально
только для этапа ветвления.  
[GetSecondaryProcessInfoAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetSecondaryProcessInfoAsync.htm)|
Асинхронно возвращает хранилище Info для вторичного процесса карточки.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetVersionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_GetVersionAsync.htm)|
Асинхронно возвращает версию карточки.  
[HasKrComponents(KrComponents)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_HasKrComponents.htm)|
Проверяет поддерживаются ли указанные компоненты настроек типового решения для
текущей карточки.  
[HasKrComponents(KrComponents[])](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_HasKrComponents_1.htm)|
Проверяет поддерживаются ли указанные компоненты настроек типового решения для
текущей карточки.  
[InvokeExtraAsync(String, Object,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_InvokeExtraAsync.htm)|
Асинхронно выполняет дополнительный метод, приложенный к текущему типу
скрипта.  
[InvokeExtraAsync<T>(String, Object,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_InvokeExtraAsync__1.htm)|
Асинхронно выполняет дополнительный метод, приложенный к текущему типу скрипта
и получить его результат.  
[IsMainProcess](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_IsMainProcess.htm)|
Текущий выполняемый процесс является основным (KrProcess)  
[IsMainProcessInactiveAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_IsMainProcessInactiveAsync.htm)|
Все этапы основного процесса (KrProcess) для текущей карточки находятся в
состоянии
[Inactive](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Inactive.htm)
.  
[IsMainProcessStartedAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_IsMainProcessStartedAsync.htm)|
Возвращает признак, показывающий, что для текущей карточки запущен основной
процесс (KrProcess).  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NewCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_NewCardAsync.htm)|
Возвращает dynamic обёртку над строковыми секциями карточки из Info этапа по
ключу
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).  
[NewCardTablesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_NewCardTablesAsync.htm)|
Возвращает dynamic обёртку над коллекционными секциями карточки из Info этапа
по ключу
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).  
[RemovePerformer(Guid, Stage,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RemovePerformer.htm)|
Удаляет исполнителя по идентификатору указанной роли для этапа с режимом
множественных исполнителей
[Multiple](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[RemovePerformer(Int32, Stage,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RemovePerformer_1.htm)|
Удаляет исполнителя расположенному по указанному порядковому индексу для этапа
с режимом множественных исполнителей
[Multiple](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[RemovePerformer(String, Stage,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RemovePerformer_2.htm)|
Удаляет исполнителя по роли для этапа с режимом множественных исполнителей
[Multiple](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[RemoveStage](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RemoveStage.htm)|
Удаляет этап из маршрута, добавленный ранее в скриптах.  
[ResetSinglePerformer](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ResetSinglePerformer.htm)|
Сбрасывает исполнителя для этапа с режимом одиночного исполнителя
[Single](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[Resolve<T>](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Resolve__1.htm)|
Получить из UnityContainer зависимость.  
[ResolveTaskHistoryGroup](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ResolveTaskHistoryGroup.htm)|
Возвращает группу истории заданий.  
[RunAfterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RunAfterAsync.htm)|
Выполняет сценарий постобработки
[AfterAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_AfterAsync.htm).  
[RunBeforeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RunBeforeAsync.htm)|
Выполняет сценарий инициализации
[BeforeAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_BeforeAsync.htm).  
[RunConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RunConditionAsync.htm)|
Выполняет C#-условие
[ConditionAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_ConditionAsync.htm).  
[RunExecutionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RunExecutionAsync.htm)|
Выполняет условие выполнимости процесса.  
[RunNextStageInContextAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RunNextStageInContextAsync.htm)|
Выполнить этап в другом контексте, т.е. в рамках другой карточки. Процесс
будет собран и выполнен как синхронный вторичный процесс. Если метод
вызывается в Before (Инициализация), то контекст будет переключен для текущего
этапа. Если метод вызывается в After (Постобработка), то контекст будет
переключен для следующего этапа.  
[RunVisibilityAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_RunVisibilityAsync.htm)|
Выполняет метод определения условия видимости.  
[Seal](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Seal.htm)|
Защищает объект от изменений.  
[SetContextualSatellite](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_SetContextualSatellite.htm)|
Задаёт контекстуальный сателлит
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm)
текущей карточки. Данный сателлит является основным сателлитом для карточки в
подсистеме маршрутов, содержит состояние карточки и инициатора, а также
маршрут для вкладки "Маршруты" (т.е. контекстуальный сателлит по
совместительству процессный для основного процесса).  
[SetCycleAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_SetCycleAsync.htm)|
Асинхронно задаёт номер текущего цикла. Является прокси для поля в
ProcessInfo.Cycle основного процесса. В вторичных процессах каждое обращение
вызывает сериализацию/десериализацию состояния основного процесса, поэтому
следует минимизировать обращения к данному методу.  
[SetSinglePerformer(Guid, String, Stage,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_SetSinglePerformer.htm)|
Устанавливает исполнителя для этапа с режимом одиночного исполнителя
[Single](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[SetSinglePerformer(String, String, Stage,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_SetSinglePerformer_1.htm)|
Устанавливает исполнителя для этапа с режимом одиночного исполнителя
[Single](T_Tessa_Extensions_Default_Shared_Workflow_PerformerUsageMode.htm).  
[SetStageStateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_SetStageStateAsync.htm)|
Асинхронно устанавливает состояние этапа в строке коллекционной секции
KrStages.  
[Show(IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show.htm)|
Вывести содержимое словаря в ValidationResult с уровнем Info.  
[Show(IEnumerable<Performer>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show_1.htm)|
Вывести информацию о нескольких исполнителях в ValidationResult с уровнем
Info.  
[Show(IEnumerable<Stage>)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show_2.htm)|
Вывести информацию о нескольких этапах в ValidationResult с уровнем Info.  
[Show(IStorageDictionaryProvider)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show_7.htm)|
Вывести содержимое хранилища в ValidationResult с уровнем Info.  
[Show(Object)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show_3.htm)|
Вывести объект в ValidationResult с уровнем Info.  
[Show(Performer)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show_5.htm)|
Вывести информацию об исполнителе в ValidationResult с уровнем Info.  
[Show(Stage)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show_6.htm)|
Вывод информации об этапе в ValidationResult с уровнем Info.  
[Show(String,
String)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_Show_4.htm)|
Вывести сообщение(message) с уточнением(details) в ValidationResult с уровнем
Info.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[VisibilityAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_VisibilityAsync.htm)|
Метод определяющий условие видимости.  
## __Поля
[ExtraMethods](F_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_KrScript_ExtraMethods.htm)|  
---|---  
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
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)
