# Tessa.Roles - пространство имён
API ролевой модели.
##  __Классы
[AdvancedRoleManager](T_Tessa_Roles_AdvancedRoleManager.htm)|  Объект,
выполняющий задания, связанные с пересчётом ролей и замещений. Доступен на
сервере.  
---|---  
[ContextRole](T_Tessa_Roles_ContextRole.htm)|  Контекстная роль.  
[DepartmentRole](T_Tessa_Roles_DepartmentRole.htm)|  Роль департамента.  
[DynamicRole](T_Tessa_Roles_DynamicRole.htm)|  Динамическая роль.  
[MetaRole](T_Tessa_Roles_MetaRole.htm)|  Метароль.  
[MetaRoleDmlQueryExecutor](T_Tessa_Roles_MetaRoleDmlQueryExecutor.htm)|
Выполняет построение DML-команд для SQL Server, изменяющих состав списка
метаролей.  
[MetaRoleInternalIDComparer](T_Tessa_Roles_MetaRoleInternalIDComparer.htm)|
Сравнивает метароли по внутренним идентификаторам.  
[MetaRoleItem](T_Tessa_Roles_MetaRoleItem.htm)|  Запись о метароли и одном из
пользователей, входящих в её состав.  
[PersonalRole](T_Tessa_Roles_PersonalRole.htm)|  Персональная роль
(пользователь).  
[Role](T_Tessa_Roles_Role.htm)|  Роль.  
[RoleDeputiesManagementHelper](T_Tessa_Roles_RoleDeputiesManagementHelper.htm)|  
[RoleDeputyIsActiveQueryExecutor](T_Tessa_Roles_RoleDeputyIsActiveQueryExecutor.htm)|
Выполняет построение команд для активации и деактивации записей о замещении.
Активация подразумевает установленный бит в колонке IsActive.  
[RoleDeputyRecord](T_Tessa_Roles_RoleDeputyRecord.htm)|  Запись о замещении на
роль.  
[RoleDeputyRecordDistinctComparer](T_Tessa_Roles_RoleDeputyRecordDistinctComparer.htm)|
Сравнивает записи о заместителях на роль по свойствам
[ID](P_Tessa_Platform_CollectionRecord_ID.htm) и
[DeputyID](P_Tessa_Roles_RoleDeputyRecord_DeputyID.htm).  
[RoleDeputyRecordValueComparer](T_Tessa_Roles_RoleDeputyRecordValueComparer.htm)|
Сравнивает записи о заместителях на роль по всем свойствам.  
[RoleGenerator](T_Tessa_Roles_RoleGenerator.htm)|  Генератор метаролей.  
[RoleGeneratorValueComparer](T_Tessa_Roles_RoleGeneratorValueComparer.htm)|
Сравнивает генераторы метаролей по всем свойствам.  
[RoleHelper](T_Tessa_Roles_RoleHelper.htm)|  Хэлперы и константы для
взаимодействия с ролевой моделью.  
[RoleManager](T_Tessa_Roles_RoleManager.htm)|  Объект, выполняющий задания,
связанные с пересчётом ролей и замещений. Доступен на сервере.  
[RoleManagerService](T_Tessa_Roles_RoleManagerService.htm)|  Объект,
выполняющий задания, связанные с пересчётом ролей и замещений. Доступен на
сервере, а также на клиенте при условии, что на клиенте зарегистрированы API
карточек и платформенные расширения.  
[RoleRepository](T_Tessa_Roles_RoleRepository.htm)|  Репозиторий для
управления ролевой моделью.  
[RoleSchedulingComparer](T_Tessa_Roles_RoleSchedulingComparer.htm)|
Сравнивает объекты ролевой модели по свойствам, ответственным за планирование.
Используется для проверки необходимости того, что объект необходимо
запланировать по другому расписанию.  
[RolesExtensions](T_Tessa_Roles_RolesExtensions.htm)|  Расширения разметки для
пространства имён Tessa.Roles.  
[RoleStrings](T_Tessa_Roles_RoleStrings.htm)|  Строковые константы,
используемые в ролевой модели.  
[RoleTypePermissionsManager](T_Tessa_Roles_RoleTypePermissionsManager.htm)|  
[RoleUserDmlQueryExecutor](T_Tessa_Roles_RoleUserDmlQueryExecutor.htm)|
Выполняет построение DML-команды для SQL Server, управляющей содержимым
состава указанной роли.  
[RoleUserIDComparer<T>](T_Tessa_Roles_RoleUserIDComparer_1.htm)|  Сравнивает
записи о пользователях роли [IRoleUser](T_Tessa_Roles_IRoleUser.htm) по
идентификаторам пользователей [ID](P_Tessa_Roles_IRoleUser_ID.htm).  
[RoleUserRecord](T_Tessa_Roles_RoleUserRecord.htm)|  Запись о составе роли.  
[RoleUserRecordUserIDComparer](T_Tessa_Roles_RoleUserRecordUserIDComparer.htm)|
Сравнивает записи о пользователях роли
[RoleUserRecord](T_Tessa_Roles_RoleUserRecord.htm) по идентификаторам
пользователей [UserID](P_Tessa_Roles_RoleUserRecord_UserID.htm).  
[RoleUserRecordValueComparer](T_Tessa_Roles_RoleUserRecordValueComparer.htm)|
Сравнивает записи о составе роли по всем свойствам.  
[RoleValueComparer](T_Tessa_Roles_RoleValueComparer.htm)|  Сравнивает роли по
всем свойствам с учётом возможных наследников [Role](T_Tessa_Roles_Role.htm).  
[StaticRole](T_Tessa_Roles_StaticRole.htm)|  Статическая роль.  
[SyncDeputiesContext](T_Tessa_Roles_SyncDeputiesContext.htm)|  Контекст
сихнронизации заместителей.  
[TaskRole](T_Tessa_Roles_TaskRole.htm)|  Роль задания, т.е. временная роль, на
которую назначено задание.  
## __Структуры
[RoleUser](T_Tessa_Roles_RoleUser.htm)|  Информация о пользователе,
используемая в ролевой модели. Представлена в виде неизменяемого типа
значения.  
---|---  
## __Интерфейсы
[IRoleLastErrorContainer](T_Tessa_Roles_IRoleLastErrorContainer.htm)|  Объект
ролевой модели, содержащий информацию о последней ошибке.  
---|---  
[IRoleManager](T_Tessa_Roles_IRoleManager.htm)|  Объект, выполняющий задания,
связанные с пересчётом ролей и замещений. Доступен на сервере.  
[IRoleManagerService](T_Tessa_Roles_IRoleManagerService.htm)|  Объект,
выполняющий задания, связанные с пересчётом ролей и замещений. Доступен на
сервере, а также на клиенте при условии, что на клиенте зарегистрированы API
карточек и платформенные расширения.  
[IRoleRepository](T_Tessa_Roles_IRoleRepository.htm)|  Репозиторий для
управления ролевой моделью.  
[IRoleSchedulingProvider](T_Tessa_Roles_IRoleSchedulingProvider.htm)|
Определяет расписание выполнения запланированных действий с ролевой моделью.  
[IRoleTypePermissionsManager](T_Tessa_Roles_IRoleTypePermissionsManager.htm)|
Объект для получения информации о используемых настроек доступа для карточек
ролей  
[IRoleUser](T_Tessa_Roles_IRoleUser.htm)|  Информация о пользователе,
используемая в ролевой модели.  
## __Перечисления
[MetaRoleType](T_Tessa_Roles_MetaRoleType.htm)|  Тип метароли.  
---|---  
[RoleEntryType](T_Tessa_Roles_RoleEntryType.htm)|  Тип сущности ролевой
модели.  
[RoleType](T_Tessa_Roles_RoleType.htm)|  Тип роли.  
[RoleUserSyncMethod](T_Tessa_Roles_RoleUserSyncMethod.htm)|  Метод
синхронизации списков пользователей.  
[SchedulingType](T_Tessa_Roles_SchedulingType.htm)|  Способ указания
расписания для выполнения действий с ролевой моделью.
