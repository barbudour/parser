# CardStoreComponent - конструктор
Создаёт экземпляр класса с указанием стратегий, требуемых для сохранения
карточки, и области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreComponent(
    	ICardStoreStrategy storeStrategy,
    	ICardTransactionStrategy transactionStrategy,
    	ICardContentStrategy contentStrategy,
    	ICardFileVersionStrategy versionStrategy,
    	IDbScope dbScope,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Public Sub New ( 
    	storeStrategy As ICardStoreStrategy,
    	transactionStrategy As ICardTransactionStrategy,
    	contentStrategy As ICardContentStrategy,
    	versionStrategy As ICardFileVersionStrategy,
    	dbScope As IDbScope,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     public:
    CardStoreComponent(
    	ICardStoreStrategy^ storeStrategy, 
    	ICardTransactionStrategy^ transactionStrategy, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardFileVersionStrategy^ versionStrategy, 
    	IDbScope^ dbScope, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            storeStrategy : ICardStoreStrategy * 
            transactionStrategy : ICardTransactionStrategy * 
            contentStrategy : ICardContentStrategy * 
            versionStrategy : ICardFileVersionStrategy * 
            dbScope : IDbScope * 
            configurationInfoProvider : IConfigurationInfoProvider -> CardStoreComponent
#### Параметры
storeStrategy
[ICardStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
    Стратегия сохранения карточки.
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
    Провайдер информации о конфигурации.
##  __См. также
#### Ссылки
[CardStoreComponent - ](T_Tessa_Cards_ComponentModel_CardStoreComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
