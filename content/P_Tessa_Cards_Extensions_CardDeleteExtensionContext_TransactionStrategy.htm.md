# CardDeleteExtensionContext.TransactionStrategy - свойство
Стратегия обеспечения блокировок и выполнения транзакций, используемая
сервисом, или null, если стратегия не используется, например, на клиенте.
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
[ICardDeleteExtensionContext.TransactionStrategy](P_Tessa_Cards_Extensions_ICardDeleteExtensionContext_TransactionStrategy.htm)  
##  __См. также
#### Ссылки
[CardDeleteExtensionContext -
](T_Tessa_Cards_Extensions_CardDeleteExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
