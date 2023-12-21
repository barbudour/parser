# ICardStoreStrategy.TryGetCardTypeIDAsync - метод
Возвращает идентификатор типа карточки или null, если карточка с заданным
идентификатором уже существует.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<Guid?> TryGetCardTypeIDAsync(
    	Guid cardID,
    	DbManager db,
    	IQueryBuilderFactory builderFactory,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetCardTypeIDAsync ( 
    	cardID As Guid,
    	db As DbManager,
    	builderFactory As IQueryBuilderFactory,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Guid?)
C++ __Копировать
    Task<Nullable<Guid>>^ TryGetCardTypeIDAsync(
    	Guid cardID, 
    	DbManager^ db, 
    	IQueryBuilderFactory^ builderFactory, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetCardTypeIDAsync : 
            cardID : Guid * 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Nullable<Guid>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, наличие которой требуется проверить.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, посредством которого осуществляется взаимодействие с базой данных.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификатор типа карточки или null, если карточка с заданным идентификатором
уже существует.
## __См. также
#### Ссылки
[ICardStoreStrategy - ](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
