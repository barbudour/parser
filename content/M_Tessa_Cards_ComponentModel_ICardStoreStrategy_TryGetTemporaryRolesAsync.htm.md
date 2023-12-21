# ICardStoreStrategy.TryGetTemporaryRolesAsync - метод
Заполняет в карточке отсутствующую информацию по временным ролям, на которые
назначены сохраняемые задания, а именно имена этих ролей, а также по авторам
задания, а именно по идентификатору, имени и должности автора. Возвращает
список временных ролей, которые требуется заполнить и добавить в процессе
сохранения карточки, или null, если при формировании списка произошли ошибки и
выполнение следует прервать.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<List<ICardTemporaryRole>> TryGetTemporaryRolesAsync(
    	IEnumerable<CardTask> tasks,
    	Guid cardID,
    	bool overrideRoleTypeID,
    	DateTime storeDateTime,
    	RoleUser defaultAuthor,
    	DbManager db,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetTemporaryRolesAsync ( 
    	tasks As IEnumerable(Of CardTask),
    	cardID As Guid,
    	overrideRoleTypeID As Boolean,
    	storeDateTime As DateTime,
    	defaultAuthor As RoleUser,
    	db As DbManager,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of ICardTemporaryRole))
C++ __Копировать
    Task<List<ICardTemporaryRole^>^>^ TryGetTemporaryRolesAsync(
    	IEnumerable<CardTask^>^ tasks, 
    	Guid cardID, 
    	bool overrideRoleTypeID, 
    	DateTime storeDateTime, 
    	RoleUser defaultAuthor, 
    	DbManager^ db, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetTemporaryRolesAsync : 
            tasks : IEnumerable<CardTask> * 
            cardID : Guid * 
            overrideRoleTypeID : bool * 
            storeDateTime : DateTime * 
            defaultAuthor : RoleUser * 
            db : DbManager * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<ICardTemporaryRole>> 
#### Параметры
tasks
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTask](T_Tessa_Cards_CardTask.htm)>
    Сохраняемые задания.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор сохраняемой карточки.
overrideRoleTypeID
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
Признак того, что для всех заданий карточки требуется выполнить запрос,
определяющий идентификатор типа роли, на которую назначено задание.
Рекомендуется устанавливать значение true всегда, кроме случаев, когда
карточка сохраняется особым образом, причём некоторые роли могут быть не
созданы на момент вызова метода, но создаются позже в расширении на
транзакцию.
storeDateTime
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Время сохранения карточки в формате UTC.
defaultAuthor [RoleUser](T_Tessa_Roles_RoleUser.htm)
    Информация о пользователе, который используется в качестве автора, если автор не указан.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, посредством которого осуществляется взаимодействие с базой данных.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, используемый для выполнения запросов, изменяющих данные в базе данных.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ICardTemporaryRole](T_Tessa_Cards_ComponentModel_ICardTemporaryRole.htm)>>  
Список временных ролей, которые требуется заполнить и добавить в процессе
сохранения карточки, или null, если при формировании списка произошли ошибки и
выполнение следует прервать.
## __См. также
#### Ссылки
[ICardStoreStrategy - ](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
