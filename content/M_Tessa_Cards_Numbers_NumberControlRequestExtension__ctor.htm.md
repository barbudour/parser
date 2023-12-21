# NumberControlRequestExtension - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected NumberControlRequestExtension(
    	ICardTransactionStrategy transactionStrategy,
    	ICardGetStrategy getStrategy,
    	ICardNewStrategy newStrategy,
    	INumberDirectorContainer numberDirectorContainer
    )
VB __Копировать
     Protected Sub New ( 
    	transactionStrategy As ICardTransactionStrategy,
    	getStrategy As ICardGetStrategy,
    	newStrategy As ICardNewStrategy,
    	numberDirectorContainer As INumberDirectorContainer
    )
C++ __Копировать
     protected:
    NumberControlRequestExtension(
    	ICardTransactionStrategy^ transactionStrategy, 
    	ICardGetStrategy^ getStrategy, 
    	ICardNewStrategy^ newStrategy, 
    	INumberDirectorContainer^ numberDirectorContainer
    )
F# __Копировать
     new : 
            transactionStrategy : ICardTransactionStrategy * 
            getStrategy : ICardGetStrategy * 
            newStrategy : ICardNewStrategy * 
            numberDirectorContainer : INumberDirectorContainer -> NumberControlRequestExtension
#### Параметры
transactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
    Стратегия обеспечения блокировок для карточек.
getStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
    Стратегия загрузки карточки.
newStrategy
[ICardNewStrategy](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
    Стратегия создания карточки.
numberDirectorContainer
[INumberDirectorContainer](T_Tessa_Cards_Numbers_INumberDirectorContainer.htm)
    Объект, предоставляющий доступ к API номеров.
##  __См. также
#### Ссылки
[NumberControlRequestExtension -
](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
