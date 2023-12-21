# SequenceProvider - конструктор
Инициализирует новый экземпляр класса
[SequenceProvider](T_Tessa_Sequences_SequenceProvider.htm)
##  __Definition
 **Пространство имён:** [Tessa.Sequences](N_Tessa_Sequences.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SequenceProvider(
    	ICardRepository cardRepository,
    	ICardTransactionStrategy transactionStrategy,
    	ICardGetStrategy getStrategy,
    	ICardStoreStrategy storeStrategy,
    	ICardMetadata cardMetadata,
    	IActionHistoryStrategy actionHistoryStrategy,
    	ISession session,
    	IDbScope dbScope,
    	IDbmsErrorCodeProvider errorCodeProvider
    )
VB __Копировать
     Public Sub New ( 
    	cardRepository As ICardRepository,
    	transactionStrategy As ICardTransactionStrategy,
    	getStrategy As ICardGetStrategy,
    	storeStrategy As ICardStoreStrategy,
    	cardMetadata As ICardMetadata,
    	actionHistoryStrategy As IActionHistoryStrategy,
    	session As ISession,
    	dbScope As IDbScope,
    	errorCodeProvider As IDbmsErrorCodeProvider
    )
C++ __Копировать
     public:
    SequenceProvider(
    	ICardRepository^ cardRepository, 
    	ICardTransactionStrategy^ transactionStrategy, 
    	ICardGetStrategy^ getStrategy, 
    	ICardStoreStrategy^ storeStrategy, 
    	ICardMetadata^ cardMetadata, 
    	IActionHistoryStrategy^ actionHistoryStrategy, 
    	ISession^ session, 
    	IDbScope^ dbScope, 
    	IDbmsErrorCodeProvider^ errorCodeProvider
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            transactionStrategy : ICardTransactionStrategy * 
            getStrategy : ICardGetStrategy * 
            storeStrategy : ICardStoreStrategy * 
            cardMetadata : ICardMetadata * 
            actionHistoryStrategy : IActionHistoryStrategy * 
            session : ISession * 
            dbScope : IDbScope * 
            errorCodeProvider : IDbmsErrorCodeProvider -> SequenceProvider
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
transactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
getStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
storeStrategy
[ICardStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
actionHistoryStrategy
[IActionHistoryStrategy](T_Tessa_Platform_Runtime_IActionHistoryStrategy.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
errorCodeProvider
[IDbmsErrorCodeProvider](T_Tessa_Platform_Data_IDbmsErrorCodeProvider.htm)
## __См. также
#### Ссылки
[SequenceProvider - ](T_Tessa_Sequences_SequenceProvider.htm)
[Tessa.Sequences - пространство имён](N_Tessa_Sequences.htm)
