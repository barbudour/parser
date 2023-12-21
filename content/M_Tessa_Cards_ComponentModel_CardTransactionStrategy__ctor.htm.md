# CardTransactionStrategy - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTransactionStrategy(
    	ICardLockingStrategy cardLockingStrategy,
    	IDbScope dbScope,
    	ITransactionScope transactionScope
    )
VB __Копировать
     Public Sub New ( 
    	cardLockingStrategy As ICardLockingStrategy,
    	dbScope As IDbScope,
    	transactionScope As ITransactionScope
    )
C++ __Копировать
     public:
    CardTransactionStrategy(
    	ICardLockingStrategy^ cardLockingStrategy, 
    	IDbScope^ dbScope, 
    	ITransactionScope^ transactionScope
    )
F# __Копировать
     new : 
            cardLockingStrategy : ICardLockingStrategy * 
            dbScope : IDbScope * 
            transactionScope : ITransactionScope -> CardTransactionStrategy
#### Параметры
cardLockingStrategy
[ICardLockingStrategy](T_Tessa_Cards_ICardLockingStrategy.htm)
    Стратегия по управлению блокировками на чтение и запись карточек.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий взаимодействие с базой данных.
transactionScope
[ITransactionScope](T_Tessa_Platform_Data_ITransactionScope.htm)
Объект для управления областью выполнения транзакции.
## __См. также
#### Ссылки
[CardTransactionStrategy -
](T_Tessa_Cards_ComponentModel_CardTransactionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
