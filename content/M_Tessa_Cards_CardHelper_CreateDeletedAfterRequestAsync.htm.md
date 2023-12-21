# CardHelper.CreateDeletedAfterRequestAsync - метод
Метод, выполняемый после создания карточки в корзине
[CreateDeletedAfterBeginTransactionAsync(ICardDeleteExtensionContext,
ICardContentStrategy, ICardStoreStrategy, ICardRepository, ICardRepository,
ICardRepository, ICardRepository,
CancellationToken)](M_Tessa_Cards_CardHelper_CreateDeletedAfterBeginTransactionAsync.htm)
снаружи транзакции. Обычно вызывается в
[AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm),
после того, как карточка будет удалена, но уже внутри транзакции. Вызывается
как в платформенной расширении на удаление в корзину, также может быть вызван
для удаления в корзину виртуальных карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task CreateDeletedAfterRequestAsync(
    	ICardDeleteExtensionContext context,
    	ICardContentStrategy contentStrategy,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateDeletedAfterRequestAsync ( 
    	context As ICardDeleteExtensionContext,
    	contentStrategy As ICardContentStrategy,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ CreateDeletedAfterRequestAsync(
    	ICardDeleteExtensionContext^ context, 
    	ICardContentStrategy^ contentStrategy, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateDeletedAfterRequestAsync : 
            context : ICardDeleteExtensionContext * 
            contentStrategy : ICardContentStrategy * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст удаления основной карточки.
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия управления контентом файлов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
