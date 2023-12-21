# CardSatelliteExportExtension - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CardSatelliteExportExtension(
    	ICardRepository cardRepository,
    	ICardTransactionStrategy cardTransactionStrategy
    )
VB __Копировать
     Protected Sub New ( 
    	cardRepository As ICardRepository,
    	cardTransactionStrategy As ICardTransactionStrategy
    )
C++ __Копировать
     protected:
    CardSatelliteExportExtension(
    	ICardRepository^ cardRepository, 
    	ICardTransactionStrategy^ cardTransactionStrategy
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            cardTransactionStrategy : ICardTransactionStrategy -> CardSatelliteExportExtension
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками с расширениями и транзакцией.
cardTransactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
    Стратегия обеспечения блокировок для взаимодействия с основной карточкой.
##  __См. также
#### Ссылки
[CardSatelliteExportExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteExportExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
