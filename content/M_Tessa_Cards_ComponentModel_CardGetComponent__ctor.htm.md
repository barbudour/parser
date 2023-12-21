# CardGetComponent - конструктор
Создаёт экземпляр класса с указанием стратегий, требуемых для загрузки
карточки, и области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetComponent(
    	ICardGetStrategy getStrategy,
    	ICardTransactionStrategy transactionStrategy,
    	ICardNewStrategy newStrategy,
    	IDbScope dbScope,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Public Sub New ( 
    	getStrategy As ICardGetStrategy,
    	transactionStrategy As ICardTransactionStrategy,
    	newStrategy As ICardNewStrategy,
    	dbScope As IDbScope,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     public:
    CardGetComponent(
    	ICardGetStrategy^ getStrategy, 
    	ICardTransactionStrategy^ transactionStrategy, 
    	ICardNewStrategy^ newStrategy, 
    	IDbScope^ dbScope, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            getStrategy : ICardGetStrategy * 
            transactionStrategy : ICardTransactionStrategy * 
            newStrategy : ICardNewStrategy * 
            dbScope : IDbScope * 
            configurationInfoProvider : IConfigurationInfoProvider -> CardGetComponent
#### Параметры
getStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
    Стратегия загрузки карточки.
transactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
    Стратегия обеспечения блокировок reader/writer при выполнении операций с карточкой.
newStrategy
[ICardNewStrategy](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
    Стратегия создания карточки.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Область видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm).
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Провайдер информации о конфигурации.
##  __См. также
#### Ссылки
[CardGetComponent - ](T_Tessa_Cards_ComponentModel_CardGetComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
