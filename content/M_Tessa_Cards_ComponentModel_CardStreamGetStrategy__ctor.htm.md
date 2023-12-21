# CardStreamGetStrategy - конструктор
Создаёт экземпляр класса с указанием стратегий, используемых для потокового
получения контента файлов на сервере.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamGetStrategy(
    	ICardContentStrategy contentStrategy,
    	ICardFileVersionStrategy versionStrategy,
    	ICardGetStrategy getStrategy,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Public Sub New ( 
    	contentStrategy As ICardContentStrategy,
    	versionStrategy As ICardFileVersionStrategy,
    	getStrategy As ICardGetStrategy,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     public:
    CardStreamGetStrategy(
    	ICardContentStrategy^ contentStrategy, 
    	ICardFileVersionStrategy^ versionStrategy, 
    	ICardGetStrategy^ getStrategy, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            contentStrategy : ICardContentStrategy * 
            versionStrategy : ICardFileVersionStrategy * 
            getStrategy : ICardGetStrategy * 
            configurationInfoProvider : IConfigurationInfoProvider -> CardStreamGetStrategy
#### Параметры
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия управления контентом файла.
versionStrategy
[ICardFileVersionStrategy](T_Tessa_Cards_ComponentModel_ICardFileVersionStrategy.htm)
    Стратегия, загружающая информацию по версиям файла.
getStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
    Стратегия загрузки карточки. Используется для проверки типа карточки.
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Провайдер информации о конфигурации.
##  __См. также
#### Ссылки
[CardStreamGetStrategy -
](T_Tessa_Cards_ComponentModel_CardStreamGetStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
