# CardDeleteStrategy - конструктор
Создаёт экземпляр класса с указанием стратегий, требуемых для удаления
карточки, и области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardDeleteStrategy(
    	ICardStoreDeletionStrategy storeDeletionStrategy,
    	ICardTransactionStrategy transactionStrategy,
    	ICardContentStrategy contentStrategy,
    	ICardFileVersionStrategy versionStrategy,
    	IDbScope dbScope,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Public Sub New ( 
    	storeDeletionStrategy As ICardStoreDeletionStrategy,
    	transactionStrategy As ICardTransactionStrategy,
    	contentStrategy As ICardContentStrategy,
    	versionStrategy As ICardFileVersionStrategy,
    	dbScope As IDbScope,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     public:
    CardDeleteStrategy(
    	ICardStoreDeletionStrategy^ storeDeletionStrategy, 
    	ICardTransactionStrategy^ transactionStrategy, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardFileVersionStrategy^ versionStrategy, 
    	IDbScope^ dbScope, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            storeDeletionStrategy : ICardStoreDeletionStrategy * 
            transactionStrategy : ICardTransactionStrategy * 
            contentStrategy : ICardContentStrategy * 
            versionStrategy : ICardFileVersionStrategy * 
            dbScope : IDbScope * 
            configurationInfoProvider : IConfigurationInfoProvider -> CardDeleteStrategy
#### Параметры
storeDeletionStrategy
[ICardStoreDeletionStrategy](T_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy.htm)
     Стратегия выполнения запросов на удаление элементов карточки при её изменении или удалении. 
transactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
     Стратегия обеспечения блокировок reader/writer при выполнении операций с карточкой. 
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия управления контентом файла.
versionStrategy
[ICardFileVersionStrategy](T_Tessa_Cards_ComponentModel_ICardFileVersionStrategy.htm)
    Стратегия, загружающая информацию по версиям файла.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Область видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm).
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Провайдер конфигурации.
##  __См. также
#### Ссылки
[CardDeleteStrategy - ](T_Tessa_Cards_ComponentModel_CardDeleteStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
