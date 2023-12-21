# RoleHelper - класс
Хэлперы и константы для взаимодействия с ролевой моделью.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class RoleHelper
VB __Копировать
     Public NotInheritable Class RoleHelper
C++ __Копировать
     public ref class RoleHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type RoleHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleHelper
##  __Свойства
[MaxDeputyDate](P_Tessa_Roles_RoleHelper_MaxDeputyDate.htm)|  Максимальная
дата замещения. Используется для определения постоянного замещения.  
---|---  
[MinDeputyDate](P_Tessa_Roles_RoleHelper_MinDeputyDate.htm)|  Минимальная дата
замещения. Используется для определения постоянного замещения.  
[RolesLockTimeoutSeconds](P_Tessa_Roles_RoleHelper_RolesLockTimeoutSeconds.htm)|
Таймаут выполнения операции в секундах.  
## __Методы
[CanEditDeputies](M_Tessa_Roles_RoleHelper_CanEditDeputies.htm)|  Метод для
проверки, может ли сотрудник userID менять заместителей для карточки cardID  
---|---  
[CreatePersonalRole](M_Tessa_Roles_RoleHelper_CreatePersonalRole.htm)|
Создаёт объект [PersonalRole](T_Tessa_Roles_PersonalRole.htm) для заданного
пользователя.  
[CreateTaskRole<T>(T[])](M_Tessa_Roles_RoleHelper_CreateTaskRole__1_1.htm)|
Создаёт роль задания по списку пользователей.  
[CreateTaskRole<T>(Guid,
T[])](M_Tessa_Roles_RoleHelper_CreateTaskRole__1.htm)|  Создаёт роль задания
по идентификатору роли и списку пользователей.  
[DeleteGeneratorRolesAsync](M_Tessa_Roles_RoleHelper_DeleteGeneratorRolesAsync.htm)|
Удаляет метароли, которые были сгенерированы заданным генератором метаролей,
посредством переданного объекта
[IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm). Метод должен
выполняться в пределах одного и того же await using (dbScope.Create()) { ...
}, чтобы гарантировать корректную работу с временными таблицами.  
[DeleteRoleGeneratorsAsync](M_Tessa_Roles_RoleHelper_DeleteRoleGeneratorsAsync.htm)|
Удаляет заданные генераторы метаролей посредством переданного объекта
[IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm). Метод должен
выполняться в пределах одного и того же await using (dbScope.Create()) { ...
}, чтобы гарантировать корректную работу с временными таблицами.  
[DeleteRolesAsync](M_Tessa_Roles_RoleHelper_DeleteRolesAsync.htm)|  Удаляет
заданные роли указанного типа посредством переданного объекта
[IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm). Метод должен
выполняться в пределах одного и того же await using (dbScope.Create()) { ...
}, чтобы гарантировать корректную работу с временными таблицами.  
[EscapeRoleNameForLocalization](M_Tessa_Roles_RoleHelper_EscapeRoleNameForLocalization.htm)|
Выполняет замену имени роли для локализации таким образом, чтобы оно было
локализовано как плейсхолдер {$Name}, если оно является строкой локализации,
начинающейся с доллара.  
[FieldStringsAreEqual](M_Tessa_Roles_RoleHelper_FieldStringsAreEqual.htm)|
Строковые поля в объектах данных должны сравниваться этим методом.  
[GenerateDynamicUsersAsync](M_Tessa_Roles_RoleHelper_GenerateDynamicUsersAsync.htm)|
Возвращает список записей о составе указанной динамической роли, полученный из
SQL-запроса этой роли.  
[GenerateIDForRoleWithUsers](M_Tessa_Roles_RoleHelper_GenerateIDForRoleWithUsers.htm)|
Создаёт уникальный идентификатор заданной роли и устанавливает его для каждой
из записей о её составе, определённой в свойстве
[Users](P_Tessa_Roles_Role_Users.htm).  
[GenerateMetaRoleItemsAsync](M_Tessa_Roles_RoleHelper_GenerateMetaRoleItemsAsync.htm)|
Возвращает список метаролей и записей об их составе, сгенерированный заданным
генератором метаролей.  
[GetActiveDeputiesAsync](M_Tessa_Roles_RoleHelper_GetActiveDeputiesAsync.htm)|
Возвращает список записей о замещении, которые отмечены как активные или
активны в настоящий момент.  
[GetDeputyUsersAsync](M_Tessa_Roles_RoleHelper_GetDeputyUsersAsync.htm)|
Возвращает список записей о составе роли, добавленных как пользователь или
замещение для типов ролей, в которых разрешено замещение.  
[GetGeneratorMetaRolesAsync](M_Tessa_Roles_RoleHelper_GetGeneratorMetaRolesAsync.htm)|
Возвращает список всех метаролей генератора с заданным идентификатором, у
которых заполнены свойства [ID](P_Tessa_Platform_NamedEntry_ID.htm),
[Name](P_Tessa_Platform_NamedEntry_Name.htm),
[MetaRoleType](P_Tessa_Roles_MetaRole_MetaRoleType.htm),
[IDGuid](P_Tessa_Roles_MetaRole_IDGuid.htm),
[IDInteger](P_Tessa_Roles_MetaRole_IDInteger.htm) и
[IDString](P_Tessa_Roles_MetaRole_IDString.htm).  
[GetGeneratorMetaUsersAsync](M_Tessa_Roles_RoleHelper_GetGeneratorMetaUsersAsync.htm)|
Возвращает список записей о составе метаролей, созданных генератором с
заданным [ID](P_Tessa_Platform_NamedEntry_ID.htm), без учёта замещений. У
метаролей будут заполнены свойства
[ID](P_Tessa_Platform_CollectionRecord_ID.htm),
[RowID](P_Tessa_Platform_CollectionRecord_RowID.htm),
[IsDeputy](P_Tessa_Roles_RoleUserRecord_IsDeputy.htm),
[RoleType](P_Tessa_Roles_RoleUserRecord_RoleType.htm),
[UserID](P_Tessa_Roles_RoleUserRecord_UserID.htm) и
[UserName](P_Tessa_Roles_RoleUserRecord_UserName.htm).  
[GetMetaRoles](M_Tessa_Roles_RoleHelper_GetMetaRoles.htm)|  Возвращает
коллекцию метаролей, полученных из записей о метаролях и их составе, созданных
генератором метаролей.  
[GetRoleName<T>](M_Tessa_Roles_RoleHelper_GetRoleName__1.htm)|  Создаёт имя
роли из совокупности имён пользователей из заданного списка.  
[GetUserNameWithContextRole](M_Tessa_Roles_RoleHelper_GetUserNameWithContextRole.htm)|
Возвращает имя пользователя с указанием контекстной роли, в которую он входит.  
[IsAdminUserAsync(IDbScope, Guid,
CancellationToken)](M_Tessa_Roles_RoleHelper_IsAdminUserAsync.htm)|  Метод
возвращает true, если сотрудник с данным ID является админом, иначе false  
[IsAdminUserAsync(IDbScope, Card,
CancellationToken)](M_Tessa_Roles_RoleHelper_IsAdminUserAsync_1.htm)|  Метод
возвращает true, если сотрудник, описанный данной карточкой является админом,
иначе false  
[IsRole](M_Tessa_Roles_RoleHelper_IsRole.htm)|  Возвращает признак того, что
идентификатор типа карточки относится к одному из видов ролей. Генератор
метаролей не является ролью.  
[IsRoleOrGenerator](M_Tessa_Roles_RoleHelper_IsRoleOrGenerator.htm)|
Возвращает признак того, что идентификатор типа карточки относится к одному из
видов ролей или к генератору метаролей.  
[ParseSqlTextForCard](M_Tessa_Roles_RoleHelper_ParseSqlTextForCard.htm)|
Выполняет разбор строки SQL-запроса контекстной роли для определения состава
роли в контексте карточки.  
[ParseSqlTextForUserAsync](M_Tessa_Roles_RoleHelper_ParseSqlTextForUserAsync.htm)|
Выполняет разбор строки SQL-запроса контекстной роли для определения состава
роли в контексте карточки.  
[SetupIDForRoleWithUsers](M_Tessa_Roles_RoleHelper_SetupIDForRoleWithUsers.htm)|
Устанавливает значение свойства [ID](P_Tessa_Platform_NamedEntry_ID.htm) для
заданной роли, а также значение свойства
[ID](P_Tessa_Platform_CollectionRecord_ID.htm) для записей о составе ролей?
определённых в свойстве [Users](P_Tessa_Roles_Role_Users.htm).  
[SetupUserNamesAsync](M_Tessa_Roles_RoleHelper_SetupUserNamesAsync.htm)|
Загружает из базы данных имена пользователей и записывает их в заданные записи
о составе роли.  
[SyncUsers](M_Tessa_Roles_RoleHelper_SyncUsers.htm)|  Добавляет SQL-команды
для преобразования исходного списка пользователей в новый, используя заданный
объект для построения команд.  
## __Поля
[CheckContextUserIDKeyword](F_Tessa_Roles_RoleHelper_CheckContextUserIDKeyword.htm)|
Ключевое слово для оператора #and_user_id_is.  
---|---  
[CheckContextUserIDKeywordName](F_Tessa_Roles_RoleHelper_CheckContextUserIDKeywordName.htm)|
Имя ключевого слова для оператора #and_user_id_is.  
[ContextCardIDKeyword](F_Tessa_Roles_RoleHelper_ContextCardIDKeyword.htm)|
Ключевое слово для оператора #context_card_id.  
[ContextCardIDKeywordName](F_Tessa_Roles_RoleHelper_ContextCardIDKeywordName.htm)|
Имя ключевого слова для оператора #context_card_id.  
[ContextCardIDParam](F_Tessa_Roles_RoleHelper_ContextCardIDParam.htm)|
Параметр SQL-запроса контекстной роли, определяющий идентификатор текущей
карточки.  
[ContextCardIDParamName](F_Tessa_Roles_RoleHelper_ContextCardIDParamName.htm)|
Имя параметра SQL-запроса контекстной роли, определяющего идентификатор
текущей карточки.  
[ContextDistinctKeyword](F_Tessa_Roles_RoleHelper_ContextDistinctKeyword.htm)|
Ключевое слово для оператора #distinct.  
[ContextDistinctKeywordName](F_Tessa_Roles_RoleHelper_ContextDistinctKeywordName.htm)|
Имя ключевого слова для оператора #distinct.  
[ContextRoleIDKeyword](F_Tessa_Roles_RoleHelper_ContextRoleIDKeyword.htm)|
Ключевое слово для оператора #role_id.  
[ContextRoleIDKeywordName](F_Tessa_Roles_RoleHelper_ContextRoleIDKeywordName.htm)|
Имя ключевого слова для оператора #role_id.  
[ContextRoleIDParam](F_Tessa_Roles_RoleHelper_ContextRoleIDParam.htm)|
Параметр SQL-запроса контекстной роли, определяющий идентификатор роли.  
[ContextRoleIDParamName](F_Tessa_Roles_RoleHelper_ContextRoleIDParamName.htm)|
Имя параметра SQL-запроса контекстной роли, определяющего идентификатор роли.  
[ContextRoleNameKeyword](F_Tessa_Roles_RoleHelper_ContextRoleNameKeyword.htm)|
Ключевое слово для оператора #role_name.  
[ContextRoleNameKeywordName](F_Tessa_Roles_RoleHelper_ContextRoleNameKeywordName.htm)|
Имя ключевого слова для оператора #role_name.  
[ContextRoleNameParam](F_Tessa_Roles_RoleHelper_ContextRoleNameParam.htm)|
Параметр SQL-запроса контекстной роли, определяющий имя роли.  
[ContextRoleNameParamName](F_Tessa_Roles_RoleHelper_ContextRoleNameParamName.htm)|
Имя параметра SQL-запроса контекстной роли, определяющего имя роли.  
[ContextRoleTableNames](F_Tessa_Roles_RoleHelper_ContextRoleTableNames.htm)|
Названия таблиц, используемых в контекстных ролях и расположенных в порядке
удаления.  
[ContextRoleTypeCaption](F_Tessa_Roles_RoleHelper_ContextRoleTypeCaption.htm)|
Отображаемое название типа карточки контекстной роли.  
[ContextRoleTypeID](F_Tessa_Roles_RoleHelper_ContextRoleTypeID.htm)|
Идентификатор типа карточки статической роли.  
[ContextRoleTypeName](F_Tessa_Roles_RoleHelper_ContextRoleTypeName.htm)|  Имя
типа карточки контекстной роли.  
[ContextTopOneKeyword](F_Tessa_Roles_RoleHelper_ContextTopOneKeyword.htm)|
Ключевое слово для оператора #top_1.  
[ContextTopOneKeywordName](F_Tessa_Roles_RoleHelper_ContextTopOneKeywordName.htm)|
Имя ключевого слова для оператора #top_1.  
[ContextUserIDParam](F_Tessa_Roles_RoleHelper_ContextUserIDParam.htm)|
Параметр SQL-запроса контекстной роли, определяющий идентификатор текущего
пользователя.  
[ContextUserIDParamName](F_Tessa_Roles_RoleHelper_ContextUserIDParamName.htm)|
Имя параметра SQL-запроса контекстной роли, определяющего идентификатор
текущего пользователя.  
[CronMaxLength](F_Tessa_Roles_RoleHelper_CronMaxLength.htm)|  Максимальная
длина строки Cron.  
[DefaultRolesLockTimeoutSeconds](F_Tessa_Roles_RoleHelper_DefaultRolesLockTimeoutSeconds.htm)|
Значение свойства
[RolesLockTimeoutSeconds](P_Tessa_Roles_RoleHelper_RolesLockTimeoutSeconds.htm),
если в файле конфигурации настройка отсутствует или задана с ошибкой. В
текущей версии системы значение равно 300.  
[DepartmentRoleTableNames](F_Tessa_Roles_RoleHelper_DepartmentRoleTableNames.htm)|
Названия таблиц, используемых в ролях департаментов и расположенных в порядке
удаления.  
[DepartmentRoleTypeCaption](F_Tessa_Roles_RoleHelper_DepartmentRoleTypeCaption.htm)|
Отображаемое название типа карточки роли департамента.  
[DepartmentRoleTypeID](F_Tessa_Roles_RoleHelper_DepartmentRoleTypeID.htm)|
Идентификатор типа карточки роли департамента.  
[DepartmentRoleTypeName](F_Tessa_Roles_RoleHelper_DepartmentRoleTypeName.htm)|
Имя типа карточки роли департамента.  
[DynamicRoleTableNames](F_Tessa_Roles_RoleHelper_DynamicRoleTableNames.htm)|
Названия таблиц, используемых в динамических ролях и расположенных в порядке
удаления.  
[DynamicRoleTypeCaption](F_Tessa_Roles_RoleHelper_DynamicRoleTypeCaption.htm)|
Отображаемое название типа карточки динамической роли.  
[DynamicRoleTypeID](F_Tessa_Roles_RoleHelper_DynamicRoleTypeID.htm)|
Идентификатор типа карточки динамический роли.  
[DynamicRoleTypeName](F_Tessa_Roles_RoleHelper_DynamicRoleTypeName.htm)|  Имя
типа карточки динамической роли.  
[ErrorTextMaxLength](F_Tessa_Roles_RoleHelper_ErrorTextMaxLength.htm)|
Максимальная длина строки с сообщением об ошибке.  
[GeneratorNameMaxLength](F_Tessa_Roles_RoleHelper_GeneratorNameMaxLength.htm)|
Максимальная длина строки с именем генератора метаролей.  
[GeneratorTypeCaption](F_Tessa_Roles_RoleHelper_GeneratorTypeCaption.htm)|
Отображаемое название типа карточки генератора метаролей.  
[GeneratorTypeID](F_Tessa_Roles_RoleHelper_GeneratorTypeID.htm)|
Идентификатор типа карточки генератора метаролей.  
[GeneratorTypeName](F_Tessa_Roles_RoleHelper_GeneratorTypeName.htm)|  Имя типа
карточки генератора метаролей.  
[LockOperationID](F_Tessa_Roles_RoleHelper_LockOperationID.htm)|
Идентификатор типа операций, а также любой операции этого типа, которая
выполняет сквозной пересчёт состава или замещений для всех ролей. Одновременно
может выполняться только одна такая операция для избежания deadlock-ов.  
[MetaRoleTableNames](F_Tessa_Roles_RoleHelper_MetaRoleTableNames.htm)|
Названия таблиц, используемых в метаролях и расположенных в порядке удаления.  
[MetaRoleTypeCaption](F_Tessa_Roles_RoleHelper_MetaRoleTypeCaption.htm)|
Отображаемое название типа карточки метароли.  
[MetaRoleTypeID](F_Tessa_Roles_RoleHelper_MetaRoleTypeID.htm)|  Идентификатор
типа карточки статической роли.  
[MetaRoleTypeName](F_Tessa_Roles_RoleHelper_MetaRoleTypeName.htm)|  Имя типа
карточки метароли.  
[PersonalRoleDeputiesSections](F_Tessa_Roles_RoleHelper_PersonalRoleDeputiesSections.htm)|
Список секций, относящихся к подсистеме замещения  
[PersonalRoleNotificationSettingsSections](F_Tessa_Roles_RoleHelper_PersonalRoleNotificationSettingsSections.htm)|
Список секций, относящихся к подсистеме правил уведомления  
[PersonalRoleSatelliteTableNames](F_Tessa_Roles_RoleHelper_PersonalRoleSatelliteTableNames.htm)|
Названия таблиц, используемых в сателлитах персональных ролей и расположенных
в порядке удаления.  
[PersonalRoleSatelliteTypeCaption](F_Tessa_Roles_RoleHelper_PersonalRoleSatelliteTypeCaption.htm)|
Отображаемое название типа карточки-сателлита сотрудника. Тип карточки не
считается ролью для методов
[IsRole(Guid)](M_Tessa_Roles_RoleHelper_IsRole.htm) и
[IsRoleOrGenerator(Guid)](M_Tessa_Roles_RoleHelper_IsRoleOrGenerator.htm).  
[PersonalRoleSatelliteTypeID](F_Tessa_Roles_RoleHelper_PersonalRoleSatelliteTypeID.htm)|
Идентификатор типа карточки-сателлита сотрудника. Тип карточки не считается
ролью для методов [IsRole(Guid)](M_Tessa_Roles_RoleHelper_IsRole.htm) и
[IsRoleOrGenerator(Guid)](M_Tessa_Roles_RoleHelper_IsRoleOrGenerator.htm).  
[PersonalRoleSatelliteTypeName](F_Tessa_Roles_RoleHelper_PersonalRoleSatelliteTypeName.htm)|
Имя типа карточки-сателлита сотрудника. Тип карточки не считается ролью для
методов [IsRole(Guid)](M_Tessa_Roles_RoleHelper_IsRole.htm) и
[IsRoleOrGenerator(Guid)](M_Tessa_Roles_RoleHelper_IsRoleOrGenerator.htm).  
[PersonalRoleTableNames](F_Tessa_Roles_RoleHelper_PersonalRoleTableNames.htm)|
Названия таблиц, используемых в персональных ролях и расположенных в порядке
удаления.  
[PersonalRoleTypeCaption](F_Tessa_Roles_RoleHelper_PersonalRoleTypeCaption.htm)|
Отображаемое название типа карточки персональной роли.  
[PersonalRoleTypeID](F_Tessa_Roles_RoleHelper_PersonalRoleTypeID.htm)|
Идентификатор типа карточки персональной роли.  
[PersonalRoleTypeName](F_Tessa_Roles_RoleHelper_PersonalRoleTypeName.htm)|
Имя типа карточки персональной роли.  
[RoleDeputiesManagementTypeID](F_Tessa_Roles_RoleHelper_RoleDeputiesManagementTypeID.htm)|
Идентификатор типа карточки "Мои замещения".  
[RoleDeputiesManagementTypeName](F_Tessa_Roles_RoleHelper_RoleDeputiesManagementTypeName.htm)|
Имя типа карточки "Мои замещения".  
[RoleGeneratorTableNames](F_Tessa_Roles_RoleHelper_RoleGeneratorTableNames.htm)|
Названия таблиц, используемых в генераторах метаролей и расположенных в
порядке удаления.  
[RoleNameMaxLength](F_Tessa_Roles_RoleHelper_RoleNameMaxLength.htm)|
Максимальная длина строки с именем роли.  
[StaticRoleTableNames](F_Tessa_Roles_RoleHelper_StaticRoleTableNames.htm)|
Названия таблиц, используемых в статических ролях и расположенных в порядке
удаления.  
[StaticRoleTypeCaption](F_Tessa_Roles_RoleHelper_StaticRoleTypeCaption.htm)|
Отображаемое название типа карточки статической роли.  
[StaticRoleTypeID](F_Tessa_Roles_RoleHelper_StaticRoleTypeID.htm)|
Идентификатор типа карточки статической роли.  
[StaticRoleTypeName](F_Tessa_Roles_RoleHelper_StaticRoleTypeName.htm)|  Имя
типа карточки статической роли.  
[TaskRoleTableNames](F_Tessa_Roles_RoleHelper_TaskRoleTableNames.htm)|
Названия таблиц, используемых в ролях заданий и расположенных в порядке
удаления.  
[TaskRoleTypeCaption](F_Tessa_Roles_RoleHelper_TaskRoleTypeCaption.htm)|
Отображаемое название типа карточки роли задания.  
[TaskRoleTypeID](F_Tessa_Roles_RoleHelper_TaskRoleTypeID.htm)|  Идентификатор
типа карточки роли задания.  
[TaskRoleTypeName](F_Tessa_Roles_RoleHelper_TaskRoleTypeName.htm)|  Имя типа
карточки роли задания.  
[TimeZoneCodeNameMaxLength](F_Tessa_Roles_RoleHelper_TimeZoneCodeNameMaxLength.htm)|
Максимальная длинна CodeName временной зоны  
[TimeZoneShortNameMaxLength](F_Tessa_Roles_RoleHelper_TimeZoneShortNameMaxLength.htm)|
Максимальная длинна ShortName временной зоны  
[UserEmailMaxLength](F_Tessa_Roles_RoleHelper_UserEmailMaxLength.htm)|
Максимальная длина адреса электронной почты пользователя.  
[UserFaxMaxLength](F_Tessa_Roles_RoleHelper_UserFaxMaxLength.htm)|
Максимальная длина факса пользователя.  
[UserFirstNameMaxLength](F_Tessa_Roles_RoleHelper_UserFirstNameMaxLength.htm)|
Максимальная длина имени пользователя.  
[UserFullNameMaxLength](F_Tessa_Roles_RoleHelper_UserFullNameMaxLength.htm)|
Максимальная длина полного имени пользователя.  
[UserHomePhoneMaxLength](F_Tessa_Roles_RoleHelper_UserHomePhoneMaxLength.htm)|
Максимальная длина домашнего телефона пользователя.  
[UserIPPhoneMaxLength](F_Tessa_Roles_RoleHelper_UserIPPhoneMaxLength.htm)|
Максимальная длина IP-телефона пользователя.  
[UserLastNameMaxLength](F_Tessa_Roles_RoleHelper_UserLastNameMaxLength.htm)|
Максимальная длина фамилии пользователя.  
[UserLoginMaxLength](F_Tessa_Roles_RoleHelper_UserLoginMaxLength.htm)|
Максимальная длина имени логина пользователя или доменного имени.  
[UserMiddleNameMaxLength](F_Tessa_Roles_RoleHelper_UserMiddleNameMaxLength.htm)|
Максимальная длина отчества пользователя.  
[UserMobilePhoneMaxLength](F_Tessa_Roles_RoleHelper_UserMobilePhoneMaxLength.htm)|
Максимальная длина мобильного телефона пользователя.  
[UserPhoneMaxLength](F_Tessa_Roles_RoleHelper_UserPhoneMaxLength.htm)|
Максимальная длина контактного телефона пользователя.  
[UserPositionMaxLength](F_Tessa_Roles_RoleHelper_UserPositionMaxLength.htm)|
Максимальная длина должности пользователя.  
## __См. также
#### Ссылки
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
