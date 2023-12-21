# TaskSatelliteRestoreExtension - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected TaskSatelliteRestoreExtension(
    	ICardRepository extendedRepositoryWithoutTransaction,
    	ICardMetadata cardMetadata,
    	ICardContentStrategy contentStrategy,
    	ICardGetStrategy getStrategy,
    	ICardStoreStrategy storeStrategy
    )
VB __Копировать
     Protected Sub New ( 
    	extendedRepositoryWithoutTransaction As ICardRepository,
    	cardMetadata As ICardMetadata,
    	contentStrategy As ICardContentStrategy,
    	getStrategy As ICardGetStrategy,
    	storeStrategy As ICardStoreStrategy
    )
C++ __Копировать
     protected:
    TaskSatelliteRestoreExtension(
    	ICardRepository^ extendedRepositoryWithoutTransaction, 
    	ICardMetadata^ cardMetadata, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardGetStrategy^ getStrategy, 
    	ICardStoreStrategy^ storeStrategy
    )
F# __Копировать
     new : 
            extendedRepositoryWithoutTransaction : ICardRepository * 
            cardMetadata : ICardMetadata * 
            contentStrategy : ICardContentStrategy * 
            getStrategy : ICardGetStrategy * 
            storeStrategy : ICardStoreStrategy -> TaskSatelliteRestoreExtension
#### Параметры
extendedRepositoryWithoutTransaction
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий для управления карточками с расширениями, но без транзакции. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаданные по типам карточек.
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия для управления контентом файлов.
getStrategy
[ICardGetStrategy](T_Tessa_Cards_ComponentModel_ICardGetStrategy.htm)
    Стратегия по загрузке карточки.
storeStrategy
[ICardStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
    Стратегия по сохранению карточки.
##  __См. также
#### Ссылки
[TaskSatelliteRestoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteRestoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
