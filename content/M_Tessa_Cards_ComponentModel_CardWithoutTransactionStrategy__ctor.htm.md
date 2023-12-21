# CardWithoutTransactionStrategy - конструктор
Создаёт экземпляр класса с указанием области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardWithoutTransactionStrategy(
    	IDbScope dbScope,
    	ITransactionScope transactionScope,
    	CardWithoutLockingStrategy cardWithoutLockingStrategy
    )
VB __Копировать
     Public Sub New ( 
    	dbScope As IDbScope,
    	transactionScope As ITransactionScope,
    	cardWithoutLockingStrategy As CardWithoutLockingStrategy
    )
C++ __Копировать
     public:
    CardWithoutTransactionStrategy(
    	IDbScope^ dbScope, 
    	ITransactionScope^ transactionScope, 
    	CardWithoutLockingStrategy^ cardWithoutLockingStrategy
    )
F# __Копировать
     new : 
            dbScope : IDbScope * 
            transactionScope : ITransactionScope * 
            cardWithoutLockingStrategy : CardWithoutLockingStrategy -> CardWithoutTransactionStrategy
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Область видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm).
transactionScope
[ITransactionScope](T_Tessa_Platform_Data_ITransactionScope.htm)
Объект для управления областью выполнения транзакции.
cardWithoutLockingStrategy
[CardWithoutLockingStrategy](T_Tessa_Cards_CardWithoutLockingStrategy.htm)
     Стратегия по блокировкам карточек. Рекомендуется указать значение типа [CardWithoutLockingStrategy](P_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy_CardWithoutLockingStrategy.htm). 
## __См. также
#### Ссылки
[CardWithoutTransactionStrategy -
](T_Tessa_Cards_ComponentModel_CardWithoutTransactionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
