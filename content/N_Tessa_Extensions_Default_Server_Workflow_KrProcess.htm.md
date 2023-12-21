# Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство имён
Расширения типового решения на сервере, связанные с выполнением процессов
маршрутов.
##  __Классы
[FillCommentsVirtualSectionGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_FillCommentsVirtualSectionGetExtension.htm)|
Расширение заполняет виртуальную секцию результатов комментирования, чтобы
была возможность отобржать результаты в таблице в кратком виде, а по двойному
клику - в полном  
---|---  
[FixTaskHistoryCardStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_FixTaskHistoryCardStoreExtension.htm)|  
[KrAcquaintanceSettingsStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrAcquaintanceSettingsStoreExtension.htm)|  
[KrAdditionalApprovalCardGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrAdditionalApprovalCardGetExtension.htm)|
Расширение на получение карточки. Заполняет виртуальные секции отображающие
информацию о дополнительных согласованиях.  
[KrAdditionalApprovalCardStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrAdditionalApprovalCardStoreExtension.htm)|  
[KrCardMetadataExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrCardMetadataExtension.htm)|
Серверное расширение метаданных для карточек типового решения. Расширяет
карточки KrCard, KrStageTemplate, KrSecondaryProcess. Добавляет этапы
маршрутов.  
[KrCardServerPermissionsProvider](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrCardServerPermissionsProvider.htm)|
Предоставляет права доступа на сервере в соответствии с типовым решением.  
[KrCreateBasedOnNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrCreateBasedOnNewExtension.htm)|
Расширение для инициализации карточки при создании на основании другой
карточки.  
[KrErrorHelper](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrErrorHelper.htm)|
Предоставляет вспомогательные методы для формирования сообщений об ошибках
выполнения маршрутов документов.  
[KrGetDocTypesCardExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrGetDocTypesCardExtension.htm)|  
[KrNotificationSettingsStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrNotificationSettingsStoreExtension.htm)|  
[KrReassignAdditionalApprovalStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrReassignAdditionalApprovalStoreExtension.htm)|  
[KrResolutionStoreExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrResolutionStoreExtensions.htm)|
Расширение на сохранение задания. Уведомляет подсистему маршрутов или Workflow
Engine о завершении следующих типов заданий:
[WfResolutionTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_WfResolutionTypeID.htm),
[WfResolutionChildTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_WfResolutionChildTypeID.htm),
[WfResolutionControlTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_WfResolutionControlTypeID.htm).  
[KrScopeMainCardAccessStrategy](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrScopeMainCardAccessStrategy.htm)|
Представляет стратегию доступа к карточке. Является обёрткой над
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[KrSecondaryProcessExportExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSecondaryProcessExportExtension.htm)|
Десериализует настройки в таблице с условиями так, чтобы они выгружались в
файл как единый json вместо строки с json.  
[KrSecondaryProcessMetadataExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSecondaryProcessMetadataExtension.htm)|  
[KrSetDefaultSettingsValuesGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSetDefaultSettingsValuesGetExtension.htm)|  
[KrSetDefaultSettingsValuesNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSetDefaultSettingsValuesNewExtension.htm)|  
[KrSetTemplateDocTypeNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSetTemplateDocTypeNewExtension.htm)|
Использует тип документа вместо типа карточки при создании шаблона.  
[KrStageRowChecker](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStageRowChecker.htm)|
Объект, определяющий наличие изменений в порядке и параметрах этапов.  
[KrStagesExportExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStagesExportExtension.htm)|  
[KrStagesImportExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStagesImportExtension.htm)|  
[KrStrictSecurityCardDeleteExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStrictSecurityCardDeleteExtension.htm)|
В режиме [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
удаление объектов маршрутов, связанных со скриптами.  
[KrStrictSecurityCardNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStrictSecurityCardNewGetExtension.htm)|
В режимах [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) или
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
редактирование C#-скриптов и SQL-запросов в объектах маршрутов.  
[KrStrictSecurityCardStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStrictSecurityCardStoreExtension.htm)|
В режимах [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) или
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
редактирование C#-скриптов и SQL-запросов в объектах маршрутов.  
[KrStrictSecurityHelper](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStrictSecurityHelper.htm)|  
[KrTaskHistoryResolver](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTaskHistoryResolver.htm)|
Объект, позволяющий определить группу в истории заданий.  
[KrTokenProvider](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider.htm)|
Объект, обеспечивающий создание и валидацию токена безопасности для типового
решения.  
[KrTokenProviderExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProviderExtensions.htm)|
Методы расширений для
[IKrTokenProvider](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTokenProvider.htm).  
[KrUniversalTaskSettingsGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskSettingsGetExtension.htm)|
Расширение необходимо для заполнения поля Order для старых этапов до
добавления этого поля.  
[KrUniversalTaskSettingsStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskSettingsStoreExtension.htm)|  
[KrUniversalTaskStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskStoreExtension.htm)|
Расширение на сохранение задания
[KrUniversalTaskTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrUniversalTaskTypeID.htm).
Сохраняет вариант завершения задания, с которым оно было завершено, и
комментарий в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm). Завершает
задание с вариантом завершения
[Approve](F_Tessa_Extensions_Default_Shared_DefaultCompletionOptions_Approve.htm).  
[NullMainCardAccessStrategy](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_NullMainCardAccessStrategy.htm)|
Представляет стратегию доступа к карточке. Методы возвращающие значения
возвращают значение - null.  
[ObviousMainCardAccessStrategy](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_ObviousMainCardAccessStrategy.htm)|
Представляет стратегию доступа к карточке. Используется явно заданная карточка
или карточка возвращаемая функцией.  
[OrderColumn](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_OrderColumn.htm)|  
[ProcessInfoCacheHelper](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_ProcessInfoCacheHelper.htm)|  
[ReferenceToStage](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_ReferenceToStage.htm)|
Описание прямого ребенка секции KrStages  
[Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Registrator.htm)|  
[StageRowMigrationHelper](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_StageRowMigrationHelper.htm)|
Предоставляет методы позволяющие выполнить миграцию строк этапов из одной
карточки в другую.  
## __Структуры
[KrProcessSectionMapper](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrProcessSectionMapper.htm)|
Объект, предоставляющий методы для переноса данных между секциями.  
---|---  
## __Интерфейсы
[IKrStageRowChecker](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrStageRowChecker.htm)|
Объект, определяющий наличие изменений в порядке и параметрах этапов.  
---|---  
[IKrTaskHistoryResolver](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTaskHistoryResolver.htm)|
Описывает объект, позволяющий определить группу в истории заданий.  
[IKrTokenProvider](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTokenProvider.htm)|
Объект, обеспечивающий создание и валидацию токена безопасности для типового
решения.  
[IMainCardAccessStrategy](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IMainCardAccessStrategy.htm)|
Описывает стратегию доступа к карточке.  
## __Перечисления
[KrProcessSerializerHiddenStageMode](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrProcessSerializerHiddenStageMode.htm)|
Режим обработки скрываемых этапов.  
---|---  
[KrTokenValidationResult](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenValidationResult.htm)|
