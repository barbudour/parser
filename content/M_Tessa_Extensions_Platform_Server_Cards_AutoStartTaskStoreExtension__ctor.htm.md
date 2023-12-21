# AutoStartTaskStoreExtension - конструктор
Инициализирует новый экземпляр класса
[AutoStartTaskStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskStoreExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AutoStartTaskStoreExtension(
    	ICardRepository defaultRepositoryWithoutTransaction,
    	ICardTransactionStrategy cardTransactionStrategy,
    	ICardTransactionStrategy cardWithoutTransactionStrategy
    )
VB __Копировать
     Public Sub New ( 
    	defaultRepositoryWithoutTransaction As ICardRepository,
    	cardTransactionStrategy As ICardTransactionStrategy,
    	cardWithoutTransactionStrategy As ICardTransactionStrategy
    )
C++ __Копировать
     public:
    AutoStartTaskStoreExtension(
    	ICardRepository^ defaultRepositoryWithoutTransaction, 
    	ICardTransactionStrategy^ cardTransactionStrategy, 
    	ICardTransactionStrategy^ cardWithoutTransactionStrategy
    )
F# __Копировать
     new : 
            defaultRepositoryWithoutTransaction : ICardRepository * 
            cardTransactionStrategy : ICardTransactionStrategy * 
            cardWithoutTransactionStrategy : ICardTransactionStrategy -> AutoStartTaskStoreExtension
#### Параметры
defaultRepositoryWithoutTransaction
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardTransactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
cardWithoutTransactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
## __См. также
#### Ссылки
[AutoStartTaskStoreExtension -
](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskStoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
