# FileConverterCache - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterCache(
    	ICardRepository extendedRepositoryWithoutTransaction,
    	ICardFileManager extendedFileManagerWithoutTransaction,
    	ICardTransactionStrategy cardTransactionStrategy,
    	ICardContentStrategy contentStrategy,
    	ICardGetStrategy cardGetStrategy,
    	ICardMetadata cardMetadata,
    	IDbScope dbScope
    )
VB __Копировать
     Public Sub New ( 
    	extendedRepositoryWithoutTransaction As ICardRepository,
    	extendedFileManagerWithoutTransaction As ICardFileManager,
    	cardTransactionStrategy As ICardTransactionStrategy,
    	contentStrategy As ICardContentStrategy,
    	cardGetStrategy As ICardGetStrategy,
    	cardMetadata As ICardMetadata,
    	dbScope As IDbScope
    )
C++ __Копировать
     public:
    FileConverterCache(
    	ICardRepository^ extendedRepositoryWithoutTransaction, 
    	ICardFileManager^ extendedFileManagerWithoutTransaction, 
    	ICardTransactionStrategy^ cardTransactionStrategy, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardGetStrategy^ cardGetStrategy, 
    	ICardMetadata^ cardMetadata, 
    	IDbScope^ dbScope
    )
F# __Копировать
     new : 
            extendedRepositoryWithoutTransaction : ICardRepository * 
            extendedFileManagerWithoutTransaction : ICardFileManager * 
            cardTransactionStrategy : ICardTransactionStrategy * 
            contentStrategy : ICardContentStrategy * 
            cardGetStrategy : ICardGetStrategy * 
            cardMetadata : ICardMetadata * 
            dbScope : IDbScope -> FileConverterCache
#### Параметры
extendedRepositoryWithoutTransaction
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий управления карточками с расширениями, но без транзакции [ExtendedWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_ExtendedWithoutTransaction.htm). 
extendedFileManagerWithoutTransaction
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm)
     Объект, обеспечивающий добавление файлов в кэш. Требуется реализация с расширениями, но без транзакции [ExtendedWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_ExtendedWithoutTransaction.htm). 
cardTransactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
    Стратегия обеспечения блокировки и открытия транзакции для карточки.
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия управления контентом файлов.
cardGetStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
    Стратегия загрузки карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий доступ к базе данных.
##  __См. также
#### Ссылки
[FileConverterCache - ](T_Tessa_FileConverters_FileConverterCache.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
