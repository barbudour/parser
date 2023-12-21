# CardHelper.CreateDeletedAfterBeginTransactionAsync - метод
Метод, создающий карточку в корзине. Обычно вызывается в
[AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm)
до того, как карточка будет удалена, но уже внутри транзакции. Вызывается как
в платформенной расширении на удаление в корзину, также может быть вызван для
удаления в корзину виртуальных карточек. Возвращает признак того, что
удалённая карточка была создана.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> CreateDeletedAfterBeginTransactionAsync(
    	ICardDeleteExtensionContext context,
    	ICardContentStrategy contentStrategy,
    	ICardStoreStrategy storeStrategy,
    	ICardRepository extendedRepositoryToGetCard,
    	ICardRepository extendedRepositoryToGetDigest,
    	ICardRepository defaultRepositoryToCreateDeleted,
    	ICardRepository defaultRepositoryToStoreDeleted,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateDeletedAfterBeginTransactionAsync ( 
    	context As ICardDeleteExtensionContext,
    	contentStrategy As ICardContentStrategy,
    	storeStrategy As ICardStoreStrategy,
    	extendedRepositoryToGetCard As ICardRepository,
    	extendedRepositoryToGetDigest As ICardRepository,
    	defaultRepositoryToCreateDeleted As ICardRepository,
    	defaultRepositoryToStoreDeleted As ICardRepository,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    static Task<bool>^ CreateDeletedAfterBeginTransactionAsync(
    	ICardDeleteExtensionContext^ context, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardStoreStrategy^ storeStrategy, 
    	ICardRepository^ extendedRepositoryToGetCard, 
    	ICardRepository^ extendedRepositoryToGetDigest, 
    	ICardRepository^ defaultRepositoryToCreateDeleted, 
    	ICardRepository^ defaultRepositoryToStoreDeleted, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateDeletedAfterBeginTransactionAsync : 
            context : ICardDeleteExtensionContext * 
            contentStrategy : ICardContentStrategy * 
            storeStrategy : ICardStoreStrategy * 
            extendedRepositoryToGetCard : ICardRepository * 
            extendedRepositoryToGetDigest : ICardRepository * 
            defaultRepositoryToCreateDeleted : ICardRepository * 
            defaultRepositoryToStoreDeleted : ICardRepository * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст удаления основной карточки.
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия управления контентом файлов.
storeStrategy
[ICardStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
    Стратегия сохранения карточки. Используется для перемещения файлов.
extendedRepositoryToGetCard
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий на загрузку удаляемой карточки. Обычно это репозиторий с расширениями, но без транзакции. 
extendedRepositoryToGetDigest
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий на получение Digest для удаляемой карточки. Обычно это репозиторий с расширениями, но без транзакции. 
defaultRepositoryToCreateDeleted
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий на создание структуры карточки Deleted. Обычно это репозиторий без расширений и без транзакции. 
defaultRepositoryToStoreDeleted
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий на сохранение карточки Deleted. Обычно это репозиторий без расширений и без транзакции. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если удалённая карточка была создана; false, если карточка не создана
из-за ошибки, или потому что её создание не требуется.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
