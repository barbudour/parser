# CardStoreExtensionContext.TransactionStrategy - свойство
Текущие дата и время сохранения для использования в транзакции или null, если
код не выполняется в транзакции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardTransactionStrategy TransactionStrategy { get; }
VB __Копировать
     Public ReadOnly Property TransactionStrategy As ICardTransactionStrategy
    	Get
C++ __Копировать
     public:
    virtual property ICardTransactionStrategy^ TransactionStrategy {
    	ICardTransactionStrategy^ get () sealed;
    }
F# __Копировать
     abstract TransactionStrategy : ICardTransactionStrategy with get
    override TransactionStrategy : ICardTransactionStrategy with get
#### Значение свойства
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
#### Реализации
[ICardStoreExtensionContext.TransactionStrategy](P_Tessa_Cards_Extensions_ICardStoreExtensionContext_TransactionStrategy.htm)  
##  __См. также
#### Ссылки
[CardStoreExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
