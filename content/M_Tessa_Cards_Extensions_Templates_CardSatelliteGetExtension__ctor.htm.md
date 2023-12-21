# CardSatelliteGetExtension - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CardSatelliteGetExtension(
    	ICardRepository cardRepository,
    	ICardTransactionStrategy cardTransactionStrategy,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Protected Sub New ( 
    	cardRepository As ICardRepository,
    	cardTransactionStrategy As ICardTransactionStrategy,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     protected:
    CardSatelliteGetExtension(
    	ICardRepository^ cardRepository, 
    	ICardTransactionStrategy^ cardTransactionStrategy, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            cardTransactionStrategy : ICardTransactionStrategy * 
            configurationInfoProvider : IConfigurationInfoProvider -> CardSatelliteGetExtension
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками с расширениями и транзакцией.
cardTransactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
    Стратегия обеспечения блокировок для взаимодействия с основной карточкой.
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Провайдер информации о конфигурации.
##  __См. также
#### Ссылки
[CardSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
