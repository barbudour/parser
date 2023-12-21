# CardGetStrategy - конструктор
Создаёт экземпляр класса с указанием стратегий, используемых для загрузки
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetStrategy(
    	ICardGetCachingStrategy cachingStrategy,
    	ICardNewStrategy newStrategy,
    	IDbScope dbScope,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Public Sub New ( 
    	cachingStrategy As ICardGetCachingStrategy,
    	newStrategy As ICardNewStrategy,
    	dbScope As IDbScope,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     public:
    CardGetStrategy(
    	ICardGetCachingStrategy^ cachingStrategy, 
    	ICardNewStrategy^ newStrategy, 
    	IDbScope^ dbScope, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            cachingStrategy : ICardGetCachingStrategy * 
            newStrategy : ICardNewStrategy * 
            dbScope : IDbScope * 
            configurationInfoProvider : IConfigurationInfoProvider -> CardGetStrategy
#### Параметры
cachingStrategy
[ICardGetCachingStrategy](T_Tessa_Cards_ComponentModel_ICardGetCachingStrategy.htm)
    Стратегия кэширования объектов для операции по загрузке карточки.
newStrategy
[ICardNewStrategy](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
    Стратегия создания карточки.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий взаимодействие с базой данных.
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Провайдер информации о конфигурации.
##  __См. также
#### Ссылки
[CardGetStrategy - ](T_Tessa_Cards_ComponentModel_CardGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
