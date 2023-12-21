# Tessa.Extensions.Platform.Server.Roles - пространство имён
Расширения платформы на сервере, связанные с карточками ролей.
##  __Классы
[AddToRolesUserStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_AddToRolesUserStoreExtension.htm)|
При создании (первом сохранении) сотрудника сразу добавляет его в заданные
роли, если они указаны в запросе.  
---|---  
[ApplyUserSettingsToRolesRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_ApplyUserSettingsToRolesRequestExtension.htm)|  
[ChangePasswordRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_ChangePasswordRequestExtension.htm)|
Изменение пароля для текущего сотрудника с типом входа "Пользователь Tessa".  
[CheckParentRoleCycleStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_CheckParentRoleCycleStoreExtension.htm)|
При установке родительской роли проверяет её на дубликаты.  
[CheckPersonalRolePermissionsNewExtension](T_Tessa_Extensions_Platform_Server_Roles_CheckPersonalRolePermissionsNewExtension.htm)|
Расширение, запрещающая создавать карточку сотрудника пользователям, которые
не являются администраторами.  
[CheckRoleDeputiesStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_CheckRoleDeputiesStoreExtension.htm)|
Выполняет проверки для замещений (обычных RoleDeputies и внутри "Моих
замещений") внутри блокировки запись карточки.  
[CheckRoleSchedulingFieldsStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_CheckRoleSchedulingFieldsStoreExtension.htm)|
Проверяет, что из полей "Выражение Cron" и "Период в секундах" установлено
одно и только одно, причём установлено корректно. Проверка выполняется внутри
блокировки на запись карточки.  
[ContextRoleGetExtension](T_Tessa_Extensions_Platform_Server_Roles_ContextRoleGetExtension.htm)|
Загрузка контекстной роли возможна через кэш.  
[FixContextRoleStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixContextRoleStoreExtension.htm)|
Исправляет карточку контекстной роли перед её сохранением.  
[FixDeputiesManagementStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixDeputiesManagementStoreExtension.htm)|
Исправляет версию виртуальной карточки "Мои замещения" после сохранения.  
[FixDynamicRoleStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixDynamicRoleStoreExtension.htm)|
Исправляет карточку динамической роли перед её сохранением.  
[FixMetaRoleStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixMetaRoleStoreExtension.htm)|
Исправляет карточку персональной роли перед её сохранением.  
[FixPersonalRolesStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixPersonalRolesStoreExtension.htm)|
Исправляет карточку сотрудника перед её сохранением на сервере. Автоматически
задаёт краткое и полное имена сотрудника. Обновляет краткое имя в секциях,
связанных с составом и замещениями ролей. Расширение должно выполняться при
импорте, чтобы в состав роли был добавлен сам сотрудник.  
[FixPersonalRoleTemplateNewExtension](T_Tessa_Extensions_Platform_Server_Roles_FixPersonalRoleTemplateNewExtension.htm)|
При копировании или создании по шаблону сотрудника сбрасываем настройки
сотрудника в карточке-сателлите, т.е. будет создана новая карточка-сателлит
для нового сотрудника. Очистка сателлита не выполняется для экспорта, т.к.
после экспорта возможен импорт, а не только создание по шаблону.  
[FixRoleGeneratorStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRoleGeneratorStoreExtension.htm)|
Исправляет карточку генератора метаролей перед её сохранением.  
[FixRolesGetExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRolesGetExtension.htm)|  
[FixRolesNewExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRolesNewExtension.htm)|
Устанавливает минимальную и максимальную даты замещения в новых строках после
создания структуры карточек ролевой модели. А также устанавливает
идентификатор типа роли.  
[FixRolesTemplateNewExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRolesTemplateNewExtension.htm)|
Очищает поле Roles.Name при создании по шаблону, чтобы имя было заполнено из
других секций. Расширение регистрируется только для типов ролей, в которых имя
дублируется в других секциях.  
[FixRoleTypesStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRoleTypesStoreExtension.htm)|
Исправляет значение типа роли [RoleType](T_Tessa_Roles_RoleType.htm) перед
сохранением карточек ролевой модели. Тщательно обсудить перед любым изменением
или удалением.  
[FixRoleUsersWithDeputiesStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRoleUsersWithDeputiesStoreExtension.htm)|
Расширение гарантирует, что если в составе роли добавляемый пользователь уже
присутствует как заместитель, то он будет удалён, чтобы не было дважды
добавленных пользователей.  
[LimitUsersInRolesGetExtension](T_Tessa_Extensions_Platform_Server_Roles_LimitUsersInRolesGetExtension.htm)|
Расширение ограничивает количество пользователей, отображаемых в динамических
ролях и метаролях.  
[PersonalRoleDeleteExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleDeleteExtension.htm)|
Удаление карточки персональной роли, учитывающее удаление карточки-сателлита,
а также проверку прав для пользователя.  
[PersonalRoleDeputiesPermissionsNewExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleDeputiesPermissionsNewExtension.htm)|
Расширение, которое запрещает редактирование замещений на вкладке "Мои
замещения" при создании карточки сотрудника, которая ещё не сохранена. Запрет
чисто визуальный, нужен, чтобы администраторы системы не нарвались на ошибки,
поскольку такой сценарий не поддерживается.  
[PersonalRoleGetExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleGetExtension.htm)|  
[PersonalRoleImportExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleImportExtension.htm)|
Импорт персональной роли.  
[PersonalRoleNewExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleNewExtension.htm)|
Расширение на заполнение настроек нового пользователя "Мои настройки" из
карточки сотрудника System.  
[PersonalRoleNotificationSubscriptionsDeleteExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleNotificationSubscriptionsDeleteExtension.htm)|  
[PersonalRoleStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleStoreExtension.htm)|  
[RecalcDeputiesRolesStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_RecalcDeputiesRolesStoreExtension.htm)|
Перерасчитывает записи в RoleDeputies если необходимо.  
[RecalcDynamicRoleRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_RecalcDynamicRoleRequestExtension.htm)|  
[RecalcRoleGeneratorRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_RecalcRoleGeneratorRequestExtension.htm)|  
[Registrator](T_Tessa_Extensions_Platform_Server_Roles_Registrator.htm)|  
[RemoveUserFromRolesDeleteExtension](T_Tessa_Extensions_Platform_Server_Roles_RemoveUserFromRolesDeleteExtension.htm)|
Удаляет все записи о вхождении сотрудника в роль и замещения перед его
удалением.  
[RoleDeputiesManagementGetExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleDeputiesManagementGetExtension.htm)|
Расширение на загрузку секиций карточки "Мои замещения".  
[RoleDeputiesManagementStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleDeputiesManagementStoreExtension.htm)|
Расширение на сохранение виртуальных секций "Мои замещения".  
[RoleExportExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleExportExtension.htm)|
Расширение на экспорт карточек ролей или генераторов метаролей без замещений,
без информации о последней ошибке и др.  
[RolesDeputiesStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_RolesDeputiesStoreExtension.htm)|
Расширение должно выполняться строго до FixRoleTypesStoreExtension, чтобы
избежать бага с незаполненым TypeID. Должно выполняться перед тем, как будут
запущены валидаторы, которые должны уметь удалять дубликаты. Валидаторы
запускаются на уровне [Platform](T_Tessa_Extensions_ExtensionStage.htm), так
что мы будет выполняться в
[Initialize](T_Tessa_Extensions_ExtensionStage.htm).  
[RoleUsersVirtualGetExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleUsersVirtualGetExtension.htm)|
Записывает в секцию RoleUsersVirtual строки из RoleUsers, которые не
соответствуют замещениям.  
[RoleUsersVirtualStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_RoleUsersVirtualStoreExtension.htm)|
Расширение, преобразующее список из строк RoleUsersVirtual в RoleUsers при
сохранении карточки. Должно выполняться перед тем, как будут запущены
валидаторы, которые должны уметь удалять дубликаты. Валидаторы запускаются на
уровне [Platform](T_Tessa_Extensions_ExtensionStage.htm), так что мы будет
выполняться в [Initialize](T_Tessa_Extensions_ExtensionStage.htm).  
[SaveCardModelSettingsRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_SaveCardModelSettingsRequestExtension.htm)|
Расширение, выполняющее сохранение настроек, связанных с карточками.  
[SetDeputyDatesGetExtension](T_Tessa_Extensions_Platform_Server_Roles_SetDeputyDatesGetExtension.htm)|
Устанавливает минимальную и максимальную даты замещения в новых строках после
загрузки карточек ролевой модели.  
[StrictSecurityRoleNewGetExtension](T_Tessa_Extensions_Platform_Server_Roles_StrictSecurityRoleNewGetExtension.htm)|
В режимах [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) или
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
редактирование SQL-запросов в ролях.  
[StrictSecurityRoleStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_StrictSecurityRoleStoreExtension.htm)|
В режимах [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) или
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm) недоступно
редактирование SQL-запросов в ролях.  
[SyncAllDeputiesRequestExtension](T_Tessa_Extensions_Platform_Server_Roles_SyncAllDeputiesRequestExtension.htm)|  
[UniqueDepartmentNameStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_UniqueDepartmentNameStoreExtension.htm)|
Расширение, обеспечивающее уникальность имени подразделения при создании
карточки департамента или при изменении полей Roles.Name и Roles.ParentID. Не
гарантирует, что при одновременном создании или изменении подразделения с
таким же именем не нарушится уникальность имён в пределах типа. Уникальность
здесь гарантирует уникальный индекс.  
[UniqueRoleNameStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_UniqueRoleNameStoreExtension.htm)|
Расширение, обеспечивающее уникальность имени роли при создании карточки роли
или при изменении поля Roles.Name. При вводе неуникального имени выводит
предупреждение, т.е. не запрещает неуникальные имена, но предупреждает о них.
Не работает для подразделений, метаролей и ролей заданий. При поиске
уникального имени не учитывает роли заданий. Не гарантирует, что при
одновременном создании или изменении роли с таким же именем не нарушится
уникальность имён в пределах типа. Уникальность здесь гарантирует уникальный
индекс.
