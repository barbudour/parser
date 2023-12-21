# WfHelper - класс
Вспомогательные поля и методы для резолюций WfResolution.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WfHelper
VB __Копировать
     Public NotInheritable Class WfHelper
C++ __Копировать
     public ref class WfHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WfHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WfHelper
##  __Методы
[CanModifyTaskCard](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CanModifyTaskCard.htm)|
Возвращает признак того, что пользователь может изменять карточку-сателлит
задания.  
---|---  
[GetData](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_GetData.htm)|
Возвращает неструктурированную информацию по бизнес-процессам, содержащуюся в
карточке-сателлите Workflow. Если такая информация отсутствует в карточке, то
создаётся и возвращается новый объект
[WfData](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfData.htm).  
[GetResolutionState](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_GetResolutionState.htm)|
Возвращает состояние резолюции, полученное по её параметрам.  
[GetUsedComponentsAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_GetUsedComponentsAsync.htm)|
Возвращает используемые компоненты типового решения, по которым можно
определить возможность использования резолюций и других бизнес-процессов
Workflow.  
[HasWorkflowInfo](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_HasWorkflowInfo.htm)|
Возвращает признак того, что заданная запись истории заданий содержит
информацию из расширенной истории заданий Workflow.  
[LoadHistoryWorkflowInfoAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_LoadHistoryWorkflowInfoAsync.htm)|
Загружает расширенную информацию по бизнес-процессам Workflow для записей в
истории заданий, которые относятся к бизнес-процессам. Возвращает признак
того, что хотя бы для одной записи была установлена расширенная информация.  
[SatelliteWasNotFound](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SatelliteWasNotFound.htm)|
Возвращает признак того, что карточка-сателлит была установлена как
отсутствующая в пакете основной карточки.  
[SetController](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetController.htm)|
Устанавливает информацию о роли, на которую возвращается задание с контролем
исполнения. Устанавливать и проверять информацию имеет смысл только для
добавляемого задания task.  
[SetData](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetData.htm)|
Устанавливает неструктурированную информацию по бизнес-процессам для карточки-
сателлита Workflow.  
[SetResponseCard](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetResponseCard.htm)|
Устанавливает заданную карточку в ответе на запрос. При этом выполняется
компрессия карточки.  
[SetSatellite](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetSatellite.htm)|
Сохраняет карточку-сателлит в пакете основной карточки.  
[SetSatelliteID](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetSatelliteID.htm)|
Устанавливает идентификатор карточки-сателлита Workflow в контексте
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm). Установка
значения, равного null, удаляет информацию из контекста.  
[SetSatelliteMainCardID](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetSatelliteMainCardID.htm)|
Устанавливает идентификатор основной карточки для карточки-сателлита резолюций
Workflow.  
[TaskTypeIsResolution](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskTypeIsResolution.htm)|
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции.  
[TaskTypeIsResolutionWithoutControl](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskTypeIsResolutionWithoutControl.htm)|
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции, который не требует контроля исполнения.  
[TaskTypeIsResolutionWithoutOverdue](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskTypeIsResolutionWithoutOverdue.htm)|
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции, который не требует индикации просроченности.  
[TryCreateResolutionPerformerRoleAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryCreateResolutionPerformerRoleAsync.htm)|
Создаёт временную роль для исполнителей резолюции, объединяющую список ролей,
включая контекстные роли. Возвращает null, если создаваемая роль не содержит
пользователей. Метод имеет смысл использовать только в том случае, если
указано более одной роли исполнителей. Созданную роль необходимо сохранить
средствами [IRoleRepository](T_Tessa_Roles_IRoleRepository.htm), прежде чем
использовать.  
[TryGetController](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetController.htm)|
Возвращает информацию о роли, на которую возвращается задание с контролем
исполнения. Возвращает признак того, что контроль исполнения выполняется.  
[TryGetData](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetData.htm)|
Возвращает неструктурированную информацию по бизнес-процессам, содержащуюся в
карточке-сателлите Workflow, или null, если такая информация отсутствует в
карточке.  
[TryGetPerformers](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetPerformers.htm)|
Возвращает массив строк с ролями исполнителей, используемыми при отправке
резолюции, или null, если получить список невозможно или список пуст.
Возвращаемое значение не может быть пустым массивом.  
[TryGetResponseCard](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetResponseCard.htm)|
Возвращает карточку из ответа на запрос, установленную посредством метода
[SetResponseCard(CardResponseBase,
Card)](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetResponseCard.htm),
или null, если карточка не была установлена.  
[TryGetSatellite](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetSatellite.htm)|
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.  
[TryGetSatelliteID](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetSatelliteID.htm)|
Возвращает идентификатор карточки-сателлита Workflow, сохранённого в заданном
контексте [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm), или
null, если идентификатор не был установлен.  
[TryGetSatelliteIDAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита для резолюций Workflow по
идентификатору основной карточки или null, если карточка-сателлит отсутствует.  
[TypeSupportsWorkflowAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TypeSupportsWorkflowAsync.htm)|
Возвращает признак того, что тип поддерживает бизнес-процессы Workflow, на
основании настроек типового решения.  
## __Поля
[CardTypeSettingsSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CardTypeSettingsSection.htm)|
Название секции для настроек типа карточки в типовом решении.  
---|---  
[CheckSafeLimitKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CheckSafeLimitKey.htm)|
Ключ с количеством дней на которое срок исполненя дочерней резолюции может
привышать родительскую.  
[CommonInfoKindCaptionField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CommonInfoKindCaptionField.htm)|
Название поля, содержащего отображаемое имя для вида текущей резолюции для
секции
[CommonInfoSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CommonInfoSection.htm)
в задании резолюции.  
[CommonInfoKindIDField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CommonInfoKindIDField.htm)|
Название поля, содержащего идентификатор вида текущей резолюции для секции
[CommonInfoSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CommonInfoSection.htm)
в задании резолюции.  
[CommonInfoSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CommonInfoSection.htm)|
Название секции для задания резолюции, содержащий общую информацию по этой
резолюции, включая вид резолюции.  
[CopiedToMainCardKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CopiedToMainCardKey.htm)|
Признак того, что файл скопирован из карточки задачи в основную карточку и ещё
не сохранён. Доступен в виде значения bool на клиенте в IFile.Info.  
[CreateChildResolutionFlags](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CreateChildResolutionFlags.htm)|
Флаги, используемые при создании дочерней резолюции.  
[DisableChildResolutionDateCheckField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_DisableChildResolutionDateCheckField.htm)|
Название поля для указания признака того, что в резолюциях отключается
проверка на соответствие даты запланированного завершения дочерней резолюции к
дате запланированного завершения родительской резолюции в секциях
[CardTypeSettingsSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CardTypeSettingsSection.htm)
и
[DocTypeSettingsSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_DocTypeSettingsSection.htm).  
[DocTypeSettingsSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_DocTypeSettingsSection.htm)|
Название секции для настроек типа документа в типовом решении.  
[FileCountTaskKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_FileCountTaskKey.htm)|
Ключ, содержащий количество файлов (int), приложенных к задаче в
CardTask.Info. Может отсутствовать, тогда количество файлов равно 0.  
[FileIsExternalKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_FileIsExternalKey.htm)|
Ключ, по которому в CardFile.Info содержится признак того, что файл был
загружен как относящийся к другой карточке, например, к основной карточке или
к карточке задачи. Для таких файлов запрещено редактирование.  
[HistoryAliveSubtasksKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_HistoryAliveSubtasksKey.htm)|
Количество подзадач, отправленных без объединения исполнителей и ещё не
завершённых с учётом подзадач, которые были созданы до того, как выполнена
отправка. Указывается значение null, если отправки без объединения
исполнителей не было выполнено.  
[HistoryControlledKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_HistoryControlledKey.htm)|
Признак того, что задание отослано на контроль, в расширенной истории
Workflow. Значение равно null, если задание отослано без контроля исполнения,
false, если задание отослано с контролем исполнения, которых ещё не был
выслан, и true, если контроль исполнения уже был выслан.  
[HistoryControllerIDKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_HistoryControllerIDKey.htm)|
Идентификатор роли, которой высылается задание на контроль, в расширенной
истории Workflow.  
[HistoryControllerNameKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_HistoryControllerNameKey.htm)|
Имя роли, которой высылается задание на контроль, в расширенной истории
Workflow.  
[HistoryHasWorkflowInfoKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_HistoryHasWorkflowInfoKey.htm)|
Признак того, что запись в истории заданий содержит информацию из расширенной
истории Workflow.  
[IgnoreTimeLimitRestrictionsKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_IgnoreTimeLimitRestrictionsKey.htm)|
Признак в CardTask.Info задания, завершаемого вариантом
[SendToPerformer](F_Tessa_Extensions_Default_Shared_DefaultCompletionOptions_SendToPerformer.htm),
в котором при указании true отключается проверка на ограничение по времени
планируемого завершения дочерней задачи относительно родительской.  
[InProgressQuantsKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_InProgressQuantsKey.htm)|
Количество квантов бизнес-календаря типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32), в течение
которых задание было взято в работу. Значение не должно учитываться, если оно
не определено положительным числом или если задание было завершено.  
[MainCardCategoryCaption](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_MainCardCategoryCaption.htm)|
Отображаемое имя категории для файлов из основной карточки при отображении в
карточке заданий.  
[MainCardCategoryID](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_MainCardCategoryID.htm)|
Идентификатор категории для файлов из карточки при отображении в карточке
заданий: {EF065661-6613-4C87-BF93-0E1DD558A751}.  
[MainCardStateKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_MainCardStateKey.htm)|
Ключ, по которому в ICardEditorModel.Info содержится состояние главной формы
для основной карточки, чтобы это состояние могло быть восстановлено из
карточки-сателлита.  
[MetadataResolutionTaskTypeIDList](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_MetadataResolutionTaskTypeIDList.htm)|
Идентификаторы типов заданий, в которые копируется метаинформация из типа
задания с идентификатором
[WfResolutionTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_WfResolutionTypeID.htm).  
[NextCardIDKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_NextCardIDKey.htm)|
Идентификатор карточки (Guid), которую требуется открыть после успешного
сохранения карточки-сателлита
[WfTaskCardTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_WfTaskCardTypeID.htm).
Может отсутствовать, тогда обновляется текущая карточка.  
[NextCardTypeIDKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_NextCardTypeIDKey.htm)|
Идентификатор типа карточки (Guid), которую требуется открыть после успешного
сохранения. Если указан ключ
[NextCardIDKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_NextCardIDKey.htm),
но отсутствует этот ключ, то карточка открывается по идентификатору без
указания типа.  
[OverdueQuantsKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_OverdueQuantsKey.htm)|
Количество квантов бизнес-календаря типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32), на которое
задание просрочено, если оно находится в работе, или было просрочено на момент
завершения, если оно было завершено. Значение не должно учитываться, если оно
не определено положительным числом.  
[ParentPlannedKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ParentPlannedKey.htm)|
Ключ для плановой даты родителя при проверке SafeLimit для дочерней резолюции.  
[ResettingFieldsAfterTaskIsCompletedAsModifiedKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResettingFieldsAfterTaskIsCompletedAsModifiedKey.htm)|
Признак в информации по сохраняемому заданию task.Info[...], который
указывает, что выполняется сброс значений полей после завершения задания с
вариантом завершения, который не удаляет задание, например, "Создать
подзадачу".  
[ResolutionAuthorIDField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionAuthorIDField.htm)|
Название поля с идентификатором сотрудника, от имени которого отправляется
задание, для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionAuthorNameField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionAuthorNameField.htm)|
Название поля с именем сотрудника, от имени которого отправляется задание, для
секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionChildrenCompletedField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionChildrenCompletedField.htm)|
Поле с датой завершения дочерней резолюции или Null, если резолюция ещё не
была завершена. Поле должно содержаться в строке секций
[ResolutionChildrenVirtualSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionChildrenVirtualSection.htm)
или
[ResolutionChildrenSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionChildrenSection.htm).  
[ResolutionChildrenSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionChildrenSection.htm)|
Название секции для таблицы с информацией по завершённым дочерним резолюциям.  
[ResolutionChildrenVirtualSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionChildrenVirtualSection.htm)|
Название секции для таблицы с дочерними резолюциями.  
[ResolutionCommentField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionCommentField.htm)|
Название поля "комментарий" для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionCompleteProjectSignalName](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionCompleteProjectSignalName.htm)|
Сигнал процесса Workflow, выполняющий завершение постановки задачи с
указанными параметрами.  
[ResolutionControlFlags](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionControlFlags.htm)|
Флаги, используемые при отправке контроля исполнения резолюции.  
[ResolutionControllerIDField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionControllerIDField.htm)|
Название поля с идентификатором роли, которой отправляется задание на
контроль, для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionControllerNameField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionControllerNameField.htm)|
Название поля с именем роли, которой отправляется задание на контроль, для
секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionDurationInDaysField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionDurationInDaysField.htm)|
Название поля с длительностью выполнения создаваемой резолюции в рабочих днях
для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionKindCaptionField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionKindCaptionField.htm)|
Название поля, содержащего отображаемое имя для вида создаваемой резолюции для
секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionKindIDField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionKindIDField.htm)|
Название поля, содержащего идентификатор вида создаваемой резолюции для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionMajorPerformerField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionMajorPerformerField.htm)|
Название поля, содержащего признак того, что при отправке резолюции с
указанием нескольких ролей исполнителей без объединения, первый исполнитель
будет отмечен как ответственный для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionMassCreationField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionMassCreationField.htm)|
Название поля, содержащего признак того, что при создании дочерней резолюции
должно быть создано по одной резолюции на каждую роль из списка исполнителей,
для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionParentCommentField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionParentCommentField.htm)|
Название поля, содержащего комментарий родительской резолюции при создании
текущей резолюции, для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionPerformerOrderField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformerOrderField.htm)|
Поле с порядковым номером исполнителя. Поле должно содержаться в строке секции
[ResolutionPerformersSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformersSection.htm).  
[ResolutionPerformerRoleIDField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformerRoleIDField.htm)|
Поле с идентификатором роли исполнителя в задании резолюции. Поле должно
содержаться в строке секции
[ResolutionPerformersSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformersSection.htm).  
[ResolutionPerformerRoleName](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformerRoleName.htm)|
Имя временной роли для исполнителей резолюции, если таких исполнителей было
несколько.  
[ResolutionPerformerRoleNameField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformerRoleNameField.htm)|
Поле с именем роли исполнителя в задании резолюции. Поле должно содержаться в
строке секции
[ResolutionPerformersSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformersSection.htm).  
[ResolutionPerformersSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPerformersSection.htm)|
Название секции с ролями исполнителей для задания резолюции.  
[ResolutionPlannedField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionPlannedField.htm)|
Название поля с датой запланированного завершения для создаваемой резолюции
для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionProcessName](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionProcessName.htm)|
Название процесса для резолюций Workflow.  
[ResolutionProjectFlags](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionProjectFlags.htm)|
Флаги, используемые при отправке проекта резолюции.  
[ResolutionRevokeChildrenField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionRevokeChildrenField.htm)|
Название поля "отозвать дочерние" для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)|
Название основной секции для задания резолюции.  
[ResolutionShowAdditionalField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionShowAdditionalField.htm)|
Название поля "дополнительно" для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[ResolutionSubProcessName](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSubProcessName.htm)|
Название основного подпроцесса для резолюций Workflow.  
[ResolutionTaskTypeIDList](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionTaskTypeIDList.htm)|
Идентификаторы всех типов заданий, которые относятся к резолюциям Workflow.  
[ResolutionTaskWithoutControlTypeIDList](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionTaskWithoutControlTypeIDList.htm)|
Идентификаторы типов резолюций Workflow, для которых не выполняется проверка
на контроль исполнения.  
[ResolutionTaskWithoutOverdueTypeIDList](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionTaskWithoutOverdueTypeIDList.htm)|
Идентификаторы типов резолюций Workflow, для которых при визуализации не
индицируется факт просроченности.  
[ResolutionVirtualDigestField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualDigestField.htm)|
Название поля "комментарий" для секции
[ResolutionVirtualSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualSection.htm)
в задании резолюции.  
[ResolutionVirtualPlannedField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualPlannedField.htm)|
Название поля "дата выполнения" для секции
[ResolutionVirtualSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualSection.htm)
в задании резолюции.  
[ResolutionVirtualRoleIDField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualRoleIDField.htm)|
Название поля "идентификатор исполнителя" для секции
[ResolutionVirtualSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualSection.htm)
в задании резолюции.  
[ResolutionVirtualRoleNameField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualRoleNameField.htm)|
Название поля "имя исполнителя" для секции
[ResolutionVirtualSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualSection.htm)
в задании резолюции.  
[ResolutionVirtualSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionVirtualSection.htm)|
Название основной секции для задания резолюции.  
[ResolutionWithControlField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionWithControlField.htm)|
Название поля "с контролем" для секции
[ResolutionSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_ResolutionSection.htm)
в задании резолюции.  
[RevokeOrCancelFormName](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_RevokeOrCancelFormName.htm)|
Имя формы в задании резолюций, используемой для отзыва или отмены. Указывается
для варианта завершения с отменой проекта резолюции, который нельзя установить
через редактор.  
[SatelliteDataField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SatelliteDataField.htm)|
Имя поля с неструктурированными данными в секции
[SatelliteSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SatelliteSection.htm)
в карточке-сателлите Workflow.  
[SatelliteIDKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SatelliteIDKey.htm)|
Ключ, по которому идентификатор карточки-сателлита хранится в контексте
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm).  
[SatelliteKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SatelliteKey.htm)|
Ключ, по которому карточка-сателлит сериализуется в основной карточке.  
[SatelliteSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SatelliteSection.htm)|
Название основной секции для карточки-сателлита, в которой содержится ссылка
на основную карточку.  
[SendResolutionToPerformerFlags](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SendResolutionToPerformerFlags.htm)|
Флаги, используемые при отправки резолюции в результате отправки родительской
резолюции исполнителю.  
[StoreDateTimeKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_StoreDateTimeKey.htm)|
Ключ для времени сохранения для проверке SafeLimit для дочерней резолюции.  
[TaskSatelliteFileInfoListKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskSatelliteFileInfoListKey.htm)|
Ключ, по которому список объектов
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm) с
информацией по файлам, приложенным к карточкам-сателлитам, содержится в
контексте расширений context.Info. Список используется для удаления
местоположения контента файлов при отсутствии ошибок при удалении.  
[TaskSatelliteListKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskSatelliteListKey.htm)|
Ключ, по которому список карточек-сателлитов IList<object> сериализуется в
основной карточке при удалении в корзину или при административном экспорте.
Каждый объект в списке является хранилищем для [Card](T_Tessa_Cards_Card.htm).  
[TaskSatelliteMovedFileInfoListKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskSatelliteMovedFileInfoListKey.htm)|
Ключ, по которому список объектов
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm) с
информацией по файлам, приложенным к карточкам-сателлитам, содержится в
контексте расширений context.Info. Список используется для восстановления
местоположения контента файлов в случае ошибок при удалении.  
[TaskSatelliteSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskSatelliteSection.htm)|
Название строковой секции для карточки-сателлита для задач.  
[UntilCompletionQuantsKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_UntilCompletionQuantsKey.htm)|
Количество квантов бизнес-календаря типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32), которые
определяют время до завершения задания. Значение не должно учитываться, если
оно не определено положительным числом. Значение может быть равно null, тогда
оно также не должно учитываться.  
[UseResolutionsField](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_UseResolutionsField.htm)|
Название поля для указания признака того, следует ли использовать резолюции, в
секциях
[CardTypeSettingsSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CardTypeSettingsSection.htm)
и
[DocTypeSettingsSection](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_DocTypeSettingsSection.htm).  
[VirtualMainCardIDKey](F_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_VirtualMainCardIDKey.htm)|
Признак того, что карточка-сателлит открыта как виртуальная, поэтому при
сохранении надо будет её сначала создать; по ключу располагается идентификатор
основной карточки (Guid).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
