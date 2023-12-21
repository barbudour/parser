# CardTransactionExtendedStrategy - конструктор
Создаёт экземпляр класса с указанием декорируемой стратегии
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTransactionExtendedStrategy(
    	ICardTransactionStrategy transactionStrategy,
    	Func<ICardTransactionExtendedPolicy> transactionExtendedPolicyFunc
    )
VB __Копировать
     Public Sub New ( 
    	transactionStrategy As ICardTransactionStrategy,
    	transactionExtendedPolicyFunc As Func(Of ICardTransactionExtendedPolicy)
    )
C++ __Копировать
     public:
    CardTransactionExtendedStrategy(
    	ICardTransactionStrategy^ transactionStrategy, 
    	Func<ICardTransactionExtendedPolicy^>^ transactionExtendedPolicyFunc
    )
F# __Копировать
     new : 
            transactionStrategy : ICardTransactionStrategy * 
            transactionExtendedPolicyFunc : Func<ICardTransactionExtendedPolicy> -> CardTransactionExtendedStrategy
#### Параметры
transactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
    Стратегия, обеспечивающая транзакционность операций с карточкой.
transactionExtendedPolicyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardTransactionExtendedPolicy](T_Tessa_Cards_ComponentModel_ICardTransactionExtendedPolicy.htm)>
     Функция, которая создаёт политику, обеспечивающую выполнение расширений в транзакционных действиях с карточкой. 
## __См. также
#### Ссылки
[CardTransactionExtendedStrategy -
](T_Tessa_Cards_ComponentModel_CardTransactionExtendedStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
