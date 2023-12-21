# Tessa.Extensions.Platform.Server.Cards - пространство имён
Расширения платформы на сервере, связанные с платформенными карточками.
##  __Классы
[AccessGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_AccessGetFileContentExtension.htm)|  
---|---  
[AccessGetFileVersionsExtension](T_Tessa_Extensions_Platform_Server_Cards_AccessGetFileVersionsExtension.htm)|  
[ActionHistoryDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryDeleteExtension.htm)|
Запись в историю действий с карточкой при её удалении.  
[ActionHistoryGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryGetExtension.htm)|
Запись в историю действий с карточкой при её открытии.  
[ActionHistoryGetFileExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryGetFileExtension.htm)|
Запись в историю действий с карточкой при открытии контента файла.  
[ActionHistoryRecordGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryRecordGetExtension.htm)|
Расширение на получение виртуальной карточки по записи из истории действий.  
[ActionHistoryStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ActionHistoryStoreExtension.htm)|
Запись в историю действий с карточкой при её создании или изменении.  
[ApplicationExportExtension](T_Tessa_Extensions_Platform_Server_Cards_ApplicationExportExtension.htm)|  
[ApplicationFileHashingStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ApplicationFileHashingStoreExtension.htm)|
Определяет необходимость вычислить хеш-сумму сохраняемых файлов в карточках
"Приложение" и "Приложение Web". Расширение выполняется при сохранении
карточки и при импорте.  
[ApplicationImportExtension](T_Tessa_Extensions_Platform_Server_Cards_ApplicationImportExtension.htm)|  
[ApplicationStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ApplicationStoreExtension.htm)|
Используется в карточках "Приложение" и "Приложение Web"  
[AutoStartTaskInfo](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskInfo.htm)|
Предоставляет информацию о состоянии задания до его обработки расширением
[AutoStartTaskStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskStoreExtension.htm).  
[AutoStartTaskRollbackStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskRollbackStoreExtension.htm)|
Расширение на сохранение карточки выполняющее откат действий выполненных
расширением
[AutoStartTaskStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskStoreExtension.htm),
если в процессе сохранения карточки произошли ошибки.  
[AutoStartTaskStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskStoreExtension.htm)|
Расширение, управляющее сохранением заданий, которые автоматически берутся в
работу. Такие задания берутся в работу в BeforeRequest.Finalize, а завершаются
уже штатным образом внутри транзакции.  
[BackupCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_BackupCardDeleteExtension.htm)|
Создание резервной копии карточки перед её удалением.  
[BackupForAdminGetExtension](T_Tessa_Extensions_Platform_Server_Cards_BackupForAdminGetExtension.htm)|
Расширение, которое запрещает запросы
[Backup](T_Tessa_Cards_CardGetMethod.htm) для любых пользователей, кроме
администраторов.  
[BusinessProcessCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardDeleteExtension.htm)|  
[BusinessProcessCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardGetExtension.htm)|  
[BusinessProcessCardHelper](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper.htm)|
Вспомогательные методы для работы с карточкой шаблона процесса  
[BusinessProcessCardImportExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardImportExtension.htm)|
Расширение, которое сбрасывает кеши бизнес-процессов при импорте карточки
шаблона бизнес-процесса.  
[BusinessProcessCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardNewExtension.htm)|  
[BusinessProcessCardStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardStoreExtension.htm)|  
[CardCompilationHelper](T_Tessa_Extensions_Platform_Server_Cards_CardCompilationHelper.htm)|  
[CardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurity.htm)|
Объект для установки и проверки доступа к карточке при наличии ограничений в
конфигурации.  
[CardStrictSecurityDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurityDeleteExtension.htm)|  
[CardStrictSecurityNewGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurityNewGetExtension.htm)|  
[CardStrictSecurityResolver](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurityResolver.htm)|  
[CardStrictSecurityStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurityStoreExtension.htm)|  
[CardTaskDialogActionStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_CardTaskDialogActionStoreExtension.htm)|
Расширение на сохранение задания диалога.  
[CheckFilesStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckFilesStoreExtension.htm)|
Проверяет свойства файлов перед загрузкой на сервер, в т.ч. их размер. Может
возвращать ошибки или устанавливать теги для файлов.  
[CheckRequestDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckRequestDeleteExtension.htm)|
Выполняет проверку запроса на удаление карточки, который пришёл с клиента.  
[CheckRequestGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckRequestGetExtension.htm)|
Выполняет проверку запроса на загрузку карточки, который пришёл с клиента.  
[CheckRequestGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckRequestGetFileContentExtension.htm)|  
[CheckRequestStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckRequestStoreExtension.htm)|
Выполняет проверку запроса на сохранение карточки, который пришёл с клиента.  
[CheckTaskAccessHelper](T_Tessa_Extensions_Platform_Server_Cards_CheckTaskAccessHelper.htm)|  
[CheckTaskAccessStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckTaskAccessStoreExtension.htm)|
Расширение на проверку прав доступа на изменение задания  
[CheckTaskModeGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CheckTaskModeGetExtension.htm)|  
[CompletionOptionDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_CompletionOptionDeleteExtension.htm)|
Расширение на удаление виртуальной карточки варианта завершения.  
[CompletionOptionGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CompletionOptionGetExtension.htm)|
Расширение на получение виртуальной карточки варианта завершения.  
[CompletionOptionNewExtension](T_Tessa_Extensions_Platform_Server_Cards_CompletionOptionNewExtension.htm)|
Расширение на создание виртуальной карточки варианта завершения.  
[CompletionOptionStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_CompletionOptionStoreExtension.htm)|
Расширение на сохранение виртуальной карточки варианта завершения.  
[CompressCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CompressCardGetExtension.htm)|
Выполняет компрессию карточки после успешного запроса на её получение.  
[CompressCardGetFileVersionsExtension](T_Tessa_Extensions_Platform_Server_Cards_CompressCardGetFileVersionsExtension.htm)|
Выполняет компрессию списка версий файла после успешного запроса на его
получение.  
[ConditionCardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_ConditionCardStrictSecurity.htm)|
Объект для установки и проверки доступа к карточке "Тип условия" при наличии
ограничений в конфигурации.  
[ConditionRepairManagerRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_ConditionRepairManagerRequestExtension.htm)|
Расширение для обработки клиентских запросов
[IConditionRepairManager](T_Tessa_Platform_Conditions_IConditionRepairManager.htm).  
[ConditionTypeDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ConditionTypeDeleteExtension.htm)|  
[ConditionTypeStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ConditionTypeStoreExtension.htm)|  
[ConfigurationVersionDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ConfigurationVersionDeleteExtension.htm)|
Увеличивает версию конфигурации при удалении карточек, загружаемых при
инициализации.  
[ConfigurationVersionStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ConfigurationVersionStoreExtension.htm)|
Увеличивает версию конфигурации при изменении карточек, загружаемых при
инициализации, у которых также увеличивается версия.  
[ConverterFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_ConverterFileContentExtension.htm)|  
[DefaultFileSourceRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_DefaultFileSourceRequestExtension.htm)|
Независимо от параметров файла устанавливаем местоположение файла по
умолчанию.  
[DeferredNotificationSendStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_DeferredNotificationSendStoreExtension.htm)|  
[DeletedCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_DeletedCardDeleteExtension.htm)|
Восстановление карточки, которая была удалена, совместно с удалением удалённой
карточки.  
[DeletedCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_DeletedCardGetExtension.htm)|
Загрузка виртуальных секций для карточки Deleted, а также установка
разрешений.  
[DeleteNotificationSubscriptionRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_DeleteNotificationSubscriptionRequestExtension.htm)|  
[DocLoadStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_DocLoadStoreExtension.htm)|
Проверка при сохранении карточки настроек потокового ввода документов  
[ErrorDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ErrorDeleteExtension.htm)|  
[ErrorGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ErrorGetExtension.htm)|  
[ErrorStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ErrorStoreExtension.htm)|
Расширение, которое создаёт запись в истории действий при создании карточки
"Ошибка".  
[ExecuteValidationTransactionActionsStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ExecuteValidationTransactionActionsStoreExtension.htm)|  
[ExportCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ExportCardGetExtension.htm)|
Действия для экспорта карточки, дополняющие стандартное API.  
[FileConverterCacheGetExtension](T_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheGetExtension.htm)|
Загружает информацию для отображения в карточке настроек. При наличии ключа
[LightweightLoadingKey](F_Tessa_FileConverters_FileConverterHelper_LightweightLoadingKey.htm)
будет загружена информация только из виртуальной секции.  
[FileConverterCacheNewExtension](T_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheNewExtension.htm)|
Карточка кэша должна всегда иметь идентификатор карточки
[CacheCardID](F_Tessa_FileConverters_FileConverterHelper_CacheCardID.htm).  
[FileConverterCacheStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheStoreExtension.htm)|
Расширение учитывает наличие в запросе ключа
[OldestPreviewRequestTimeKey](F_Tessa_FileConverters_FileConverterHelper_OldestPreviewRequestTimeKey.htm),
по которому должна быть выполнена очистка кэша. Тип карточки административный,
поэтому доступ к очистке кэша могут иметь только администраторы.  
[FileSatelliteCardStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FileSatelliteCardStoreExtension.htm)|
Расширение, которое сохраняет файловый сателлит в
[BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm).
Расширение выполняется с регистрацией
[Finalize](T_Tessa_Extensions_ExtensionStage.htm).  
[FileSatelliteGetFileContentExtension](T_Tessa_Extensions_Platform_Server_Cards_FileSatelliteGetFileContentExtension.htm)|
Данное расширение получает контент файлы из файлового сателлита по ID основной
карточке.  
[FileSatelliteHelper](T_Tessa_Extensions_Platform_Server_Cards_FileSatelliteHelper.htm)|
Класс с вспомогательными методами для удобной работы с файловым сателлитом.  
[FileSatelliteTaskDeleteTaskStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FileSatelliteTaskDeleteTaskStoreExtension.htm)|
Данное расширение удаляет файлы из файлового сателлита, которые относятся к
удаляемому заданию.  
[FileSignaturesStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FileSignaturesStoreExtension.htm)|
Запрещает удаление строк с подписями, если пользователь не является
администратором.  
[FileTemplateCardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateCardStrictSecurity.htm)|
Объект для установки и проверки доступа к карточке "Шаблон файла" при наличии
ограничений в конфигурации.  
[FileTemplateCompilationStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateCompilationStoreExtension.htm)|  
[FileTemplateCompileAllRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateCompileAllRequestExtension.htm)|  
[FileTemplateDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateDeleteExtension.htm)|  
[FileTemplateGetContentExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateGetContentExtension.htm)|
Расширение производит загрузку контента файла из карточки шаблона с заменой
плейсхолдеров в файле  
[FileTemplateStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateStoreExtension.htm)|
Проверяем количество файлов в карточке и, в случае изменения файлов, очищаем
предзаписанную информацию о плейсхолдерах шаблона.  
[FileTemplateValidatorStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FileTemplateValidatorStoreExtension.htm)|  
[FixNumberWhenSavingTemplateRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_FixNumberWhenSavingTemplateRequestExtension.htm)|
Исправляет карточку, отредактированную в шаблоне, в соответствие с API
номеров.  
[FixSignatureVersionsStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FixSignatureVersionsStoreExtension.htm)|
Расширение исправляет идентификатор версии файла для тех строк ЭЦП, которые
указаны как связанные с последней версией.  
[FunctionRoleDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_FunctionRoleDeleteExtension.htm)|
Расширение на удаление виртуальной карточки варианта завершения.  
[FunctionRoleGetExtension](T_Tessa_Extensions_Platform_Server_Cards_FunctionRoleGetExtension.htm)|
Расширение на получение виртуальной карточки варианта завершения.  
[FunctionRoleNewExtension](T_Tessa_Extensions_Platform_Server_Cards_FunctionRoleNewExtension.htm)|
Расширение на создание виртуальной карточки варианта завершения.  
[FunctionRoleStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_FunctionRoleStoreExtension.htm)|
Расширение на сохранение виртуальной карточки варианта завершения.  
[GetTypeIDListRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_GetTypeIDListRequestExtension.htm)|  
[GetVersionSignaturesRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_GetVersionSignaturesRequestExtension.htm)|
Запрос на загрузку подписей для заданной версии файла.  
[HideTasksFromAuthorStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_HideTasksFromAuthorStoreExtension.htm)|
Установка флага HiddenFromAuthor для создаваемых заданий.  
[HtmlPlaceholderDocumentBuilder](T_Tessa_Extensions_Platform_Server_Cards_HtmlPlaceholderDocumentBuilder.htm)|  
[ImportCardStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ImportCardStoreExtension.htm)|
Действия для импорта карточки, дополняющие стандартное API.  
[LicenseGetExtension](T_Tessa_Extensions_Platform_Server_Cards_LicenseGetExtension.htm)|
Расширение, заполняющее поля для карточки настроек лицензии при её загрузке.  
[LicenseNewExtension](T_Tessa_Extensions_Platform_Server_Cards_LicenseNewExtension.htm)|
Расширение, заполняющее поля для карточки настроек лицензии при её создании.  
[LicenseStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_LicenseStoreExtension.htm)|
Расширение, заполняющее поля для карточки настроек лицензии при её сохранении
(как при первом, так и при последующих).  
[LoadFileSignaturesGetExtension](T_Tessa_Extensions_Platform_Server_Cards_LoadFileSignaturesGetExtension.htm)|
Загружает секцию с подписями для всех файлов. Платформенный компонент не
загружает эту секцию, т.к. в неё включена колонка Data, а также для
оптимизации загрузки по всем файлам. Выполняемся на
[Platform](T_Tessa_Extensions_ExtensionStage.htm), чтобы для виртуальных
файлов можно было загрузить подписи.  
[MakeReadonlyGetExtension](T_Tessa_Extensions_Platform_Server_Cards_MakeReadonlyGetExtension.htm)|
Устанавливает поле в состояние "только для чтения" после первого сохранения
карточки [MakeReadonly](F_Tessa_Cards_CardTypeExtensionTypes_MakeReadonly.htm)
для типа карточки, файла или задания.  
[MergeWithBilletCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_MergeWithBilletCardNewExtension.htm)|
Инициализирует созданную карточку данными из заготовки карточки
([NewCardBilletKey](F_Tessa_Cards_CardHelper_NewCardBilletKey.htm)).  
[MySettingsNotificationPlaceholderCardRequest](T_Tessa_Extensions_Platform_Server_Cards_MySettingsNotificationPlaceholderCardRequest.htm)|  
[NotificationCardsStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_NotificationCardsStrictSecurity.htm)|
Объект для установки и проверки доступа к карточке "Уведомление" при наличии
ограничений в конфигурации.  
[NotificationCompilationStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationCompilationStoreExtension.htm)|  
[NotificationDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationDeleteExtension.htm)|  
[NotificationSubscriptionsBackupExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsBackupExtension.htm)|  
[NotificationSubscriptionsCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsCardDeleteExtension.htm)|  
[NotificationSubscriptionsCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsCardGetExtension.htm)|  
[NotificationSubscriptionsCardStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsCardStoreExtension.htm)|  
[NotificationSubscriptionsRestoreExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsRestoreExtension.htm)|  
[NotificationTypeDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationTypeDeleteExtension.htm)|  
[NotificationTypeStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationTypeStoreExtension.htm)|  
[OperationGetExtension](T_Tessa_Extensions_Platform_Server_Cards_OperationGetExtension.htm)|
Расширение на получение виртуальной карточки операции.  
[PlaceholderCompilationStoreRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_PlaceholderCompilationStoreRequestExtension.htm)|  
[PlaceholderDocumentBuilderContainer](T_Tessa_Extensions_Platform_Server_Cards_PlaceholderDocumentBuilderContainer.htm)|  
[PrepareCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_PrepareCardDeleteExtension.htm)|
Проверяет и подготавливает запрос на удаление карточки перед тем, как его
получат остальные расширения при передаче запроса через веб-сервис.  
[Registrator](T_Tessa_Extensions_Platform_Server_Cards_Registrator.htm)|  
[ResetUserSettingsRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_ResetUserSettingsRequestExtension.htm)|  
[ResolveUserCipherInfoRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_ResolveUserCipherInfoRequestExtension.htm)|
Запрос на получение актуализированной информации по ключам шифрования для
текущего пользователя
[ResolveUserCipherInfo](F_Tessa_Cards_CardRequestTypes_ResolveUserCipherInfo.htm).  
[SealedApplicationDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedApplicationDeleteExtension.htm)|
В режиме [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
создание, изменение и удаление карточек приложений, а также их импорт. При
этом структуру карточки можно создать, но при первом сохранении будет ошибка.  
[SealedApplicationNewGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedApplicationNewGetExtension.htm)|
В режиме [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
создание, изменение и удаление карточек приложений, а также их импорт. При
этом структуру карточки можно создать, но при первом сохранении будет ошибка.  
[SealedApplicationStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedApplicationStoreExtension.htm)|
В режиме [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
создание, изменение и удаление карточек приложений, а также их импорт. При
этом структуру карточки можно создать, но при первом сохранении будет ошибка.  
[SealedSingletonDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedSingletonDeleteExtension.htm)|
В режиме [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
создание, изменение и удаление карточек-синглтонов, а также их импорт. При
этом структуру карточки можно создать, но при первом сохранении будет ошибка.  
[SealedSingletonNewGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedSingletonNewGetExtension.htm)|
В режиме [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
создание, изменение и удаление карточек-синглтонов, а также их импорт. При
этом структуру карточки можно создать, но при первом сохранении будет ошибка.  
[SealedSingletonStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedSingletonStoreExtension.htm)|
В режиме [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
создание, изменение и удаление карточек-синглтонов, а также их импорт. При
этом структуру карточки можно создать, но при первом сохранении будет ошибка.  
[SequenceGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SequenceGetExtension.htm)|  
[SequenceNewExtension](T_Tessa_Extensions_Platform_Server_Cards_SequenceNewExtension.htm)|
Расширение на создание карточки последовательности, в которой дописывается
один интервал со свободными номерами и устанавливаются разрешения на
редактирование.  
[SequenceStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_SequenceStoreExtension.htm)|
Расширение, проверяющее целостность интервалов и зарезервированных номеров, а
также уникальность названия последовательности в транзакции на сохранение
карточки последовательности.  
[ServerInstanceDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_ServerInstanceDeleteExtension.htm)|
Расширение удаляет информацию для физической таблицы FileSources, т.к. её
содержимое настраивается удаляемой карточкой.  
[ServerInstanceGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ServerInstanceGetExtension.htm)|
Расширение загружает информацию для виртуальной секции FileSourcesVirtual из
физической таблицы FileSources.  
[ServerInstanceStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ServerInstanceStoreExtension.htm)|
Расширение изменяет информацию для физической таблицы FileSources по данным
виртуальной секции FileSourcesVirtual.  
[SetFileSourceStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_SetFileSourceStoreExtension.htm)|  
[SingletonDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_SingletonDeleteExtension.htm)|
Удаление карточки-синглтона возможно без указания CardID.  
[SingletonExtensionHelper](T_Tessa_Extensions_Platform_Server_Cards_SingletonExtensionHelper.htm)|  
[SingletonGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SingletonGetExtension.htm)|
Загрузка карточки-синглтона возможна через кэш без указания CardID.  
[SingletonNewExtension](T_Tessa_Extensions_Platform_Server_Cards_SingletonNewExtension.htm)|
Невозможно создание карточки-синглтона, когда экземпляр карточки уже создан.  
[SingletonStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_SingletonStoreExtension.htm)|
Невозможно создание карточки-синглтона, когда экземпляр карточки уже создан.  
[SortRowsGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SortRowsGetExtension.htm)|
Упорядочиваем строки коллекционных секций при выполнении расширения
[SortRows](F_Tessa_Cards_CardTypeExtensionTypes_SortRows.htm) для типа
карточки, файла или задания.  
[StorageForAdminGetExtension](T_Tessa_Extensions_Platform_Server_Cards_StorageForAdminGetExtension.htm)|
Расширение, которое запрещает запросы
[Storage](T_Tessa_Cards_CardGetMethod.htm) для любых пользователей, кроме
администраторов.  
[StorageMappingExportExtension](T_Tessa_Extensions_Platform_Server_Cards_StorageMappingExportExtension.htm)|
Действия для экспорта карточки, дополняющие стандартное API. Данное расширение
задает параметры сериализации для выгрузки контента карточек во внешние файлы.  
[StrictSecurityStorageGetExtension](T_Tessa_Extensions_Platform_Server_Cards_StrictSecurityStorageGetExtension.htm)|
В режиме [StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)
недоступна административная загрузка карточки с игнорированием расширений для
просмотра структуры.  
[TaskKindGetExtension](T_Tessa_Extensions_Platform_Server_Cards_TaskKindGetExtension.htm)|  
[TemplateByTemplateNewExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateByTemplateNewExtension.htm)|
Создание копии для карточки шаблона или создание карточки шаблона по
экспортированной карточке. Запрещаем редактировать приложенные файлы,
разрешать будем только после сохранения при редактировании карточки в шаблоне.  
[TemplateCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateCardNewExtension.htm)|
Перенос карточки, создаваемой по шаблону, из Info в Response. При этом не
будет выполняться стандартный Request. Переносимая карточка не клонируется,
т.е. изменения в Info сразу же отражаются на Response. Если пользовательские
расширения уже записали Response, то действий не выполняется.  
[TemplateDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateDeleteExtension.htm)|
Проверка прав перед удалением карточки шаблона.  
[TemplateEditCardRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateEditCardRequestExtension.htm)|
Редактирование карточки в шаблоне
[EditCardInTemplate](F_Tessa_Cards_CardRequestTypes_EditCardInTemplate.htm).  
[TemplateExtensionHelper](T_Tessa_Extensions_Platform_Server_Cards_TemplateExtensionHelper.htm)|
Вспомогательные методы и константы для расширений на карточки шаблонов.  
[TemplateGetExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateGetExtension.htm)|
Проверка прав на шаблон перед его загрузкой и установка прав при загрузке
карточки шаблона. Заполнение виртуальных секций шаблона.  
[TemplateNewExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateNewExtension.htm)|
Создание карточки шаблона по карточке, переданной в Request или создание
карточки по идентификатору шаблона, переданного в Request. Заполнение
виртуальных секций шаблона.  
[TemplateSaveCardRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateSaveCardRequestExtension.htm)|
Сохранение отредактированной карточки в шаблоне
[SaveCardInTemplate](F_Tessa_Cards_CardRequestTypes_SaveCardInTemplate.htm).  
[TemplateStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateStoreExtension.htm)|
Проверка прав перед изменением карточки шаблона и её первичное сохранение, в
процессе которого копируются приложенные файлы.  
[TemplateUniqueValidatorRequestExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateUniqueValidatorRequestExtension.htm)|
Выполнение валидаторов уникальности при сохранении в шаблоне.  
[TextPlaceholderDocumentBuilder](T_Tessa_Extensions_Platform_Server_Cards_TextPlaceholderDocumentBuilder.htm)|  
[ValidateNotNullTableStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ValidateNotNullTableStoreExtension.htm)|
Выполняет проверку на то, что в секциях, обнаруженных валидаторами
[NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm), есть хотя
бы одна строка на этапе
[BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm).  
[ValidateUniqueStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ValidateUniqueStoreExtension.htm)|
Выполняет проверку на то, что в полях, обнаруженных валидаторами
[Unique](F_Tessa_Cards_CardValidatorTypes_Unique.htm), значения уникальны на
этапе
[AfterBeginTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterBeginTransaction.htm).
Также выполняет проверки и удаляет дубликаты на этапе
[BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeRequest.htm),
если соотвествующая настройка включена в валидаторе.  
[ViewCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_ViewCardGetExtension.htm)|
Расширение на загрузку виртуальной карточки "Представление"
[ViewTypeID](F_Tessa_Cards_CardHelper_ViewTypeID.htm). Только администратор
системы может видеть поля такой карточки.  
[ViewCardStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_ViewCardStoreExtension.htm)|
Расширение на сохранение ролей для виртуальной карточки "Представление"
[ViewTypeID](F_Tessa_Cards_CardHelper_ViewTypeID.htm). Только администратор
системы может изменять такую карточку.  
[WebApplicationExportExtension](T_Tessa_Extensions_Platform_Server_Cards_WebApplicationExportExtension.htm)|  
[WebApplicationImportExtension](T_Tessa_Extensions_Platform_Server_Cards_WebApplicationImportExtension.htm)|  
[WorkflowInstanceCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_WorkflowInstanceCardDeleteExtension.htm)|  
[WorkplaceCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_WorkplaceCardGetExtension.htm)|
Расширение на загрузку виртуальной карточки "Рабочее место"
[ViewTypeID](F_Tessa_Cards_CardHelper_ViewTypeID.htm). Только администратор
системы может видеть поля такой карточки.  
[WorkplaceCardStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_WorkplaceCardStoreExtension.htm)|
Расширение на сохранение ролей для виртуальной карточки "Рабочее место"
[WorkplaceTypeID](F_Tessa_Cards_CardHelper_WorkplaceTypeID.htm). Только
администратор системы может изменять такую карточку.  
## __Интерфейсы
[ICardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_ICardStrictSecurity.htm)|
Объект для установки и проверки доступа к карточке при наличии ограничений в
конфигурации.  
---|---  
[ICardStrictSecurityResolver](T_Tessa_Extensions_Platform_Server_Cards_ICardStrictSecurityResolver.htm)|  
[IPlaceholderDocumentBuilderContainer](T_Tessa_Extensions_Platform_Server_Cards_IPlaceholderDocumentBuilderContainer.htm)|  
## __Делегаты
[PlaceholderDocumentBuilderFunc](T_Tessa_Extensions_Platform_Server_Cards_PlaceholderDocumentBuilderFunc.htm)|
Функция, создающая и возвращающая документ для заданного потока с содержимым
documentStream. Также возвращается функция getDocumentContentFunc, которая
получает контент изменённого документа в форме массива байт при успешной
замене плейсхолдеров.  
---|---
