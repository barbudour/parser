# TaskSatelliteGetExtension - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected TaskSatelliteGetExtension(
    	ICardRepository extendedRepository,
    	ICardRepository extendedRepositoryWithoutTransaction,
    	ICardTransactionStrategy cardTransactionStrategy,
    	ICardGetStrategy cardGetStrategy,
    	ICardNewStrategy cardNewStrategy
    )
VB __Копировать
     Protected Sub New ( 
    	extendedRepository As ICardRepository,
    	extendedRepositoryWithoutTransaction As ICardRepository,
    	cardTransactionStrategy As ICardTransactionStrategy,
    	cardGetStrategy As ICardGetStrategy,
    	cardNewStrategy As ICardNewStrategy
    )
C++ __Копировать
     protected:
    TaskSatelliteGetExtension(
    	ICardRepository^ extendedRepository, 
    	ICardRepository^ extendedRepositoryWithoutTransaction, 
    	ICardTransactionStrategy^ cardTransactionStrategy, 
    	ICardGetStrategy^ cardGetStrategy, 
    	ICardNewStrategy^ cardNewStrategy
    )
F# __Копировать
     new : 
            extendedRepository : ICardRepository * 
            extendedRepositoryWithoutTransaction : ICardRepository * 
            cardTransactionStrategy : ICardTransactionStrategy * 
            cardGetStrategy : ICardGetStrategy * 
            cardNewStrategy : ICardNewStrategy -> TaskSatelliteGetExtension
#### Параметры
extendedRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками с расширениями и транзакцией.
extendedRepositoryWithoutTransaction
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками с расширениями, но без транзакции.
cardTransactionStrategy
[ICardTransactionStrategy](T_Tessa_Cards_ComponentModel_ICardTransactionStrategy.htm)
    Стратегия обеспечения блокировок для взаимодействия с основной карточкой.
cardGetStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
    Стратегия низкоуровневой загрузки карточки, используемая при загрузке виртуального задания.
cardNewStrategy
[ICardNewStrategy](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
    Стратегия низкоуровневого создания структуры карточки, используемая при загрузке виртуального задания.
##  __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
