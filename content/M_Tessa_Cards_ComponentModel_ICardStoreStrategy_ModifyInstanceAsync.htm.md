# ICardStoreStrategy.ModifyInstanceAsync - метод
Устанавливает информацию по дате и времени изменения карточки, и по
пользователю, который изменил карточку. Также увеличивает версию карточку,
если параметр incrementVersion равен true.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task ModifyInstanceAsync(
    	Guid cardID,
    	Guid userID,
    	string userName,
    	DateTime modified,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	bool incrementVersion,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ModifyInstanceAsync ( 
    	cardID As Guid,
    	userID As Guid,
    	userName As String,
    	modified As DateTime,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	incrementVersion As Boolean,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ ModifyInstanceAsync(
    	Guid cardID, 
    	Guid userID, 
    	String^ userName, 
    	DateTime modified, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	bool incrementVersion, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ModifyInstanceAsync : 
            cardID : Guid * 
            userID : Guid * 
            userName : string * 
            modified : DateTime * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            incrementVersion : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор изменяемой карточки.
userID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор пользователя, выполняющего изменение карточки.
userName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя пользователя, выполняющего изменение карточки.
modified [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата изменения карточки. Должна быть указана текущая дата в формате UTC.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, осуществляющий выполнение SQL-команд.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
incrementVersion
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что версию карточку надо увеличить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreStrategy - ](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
