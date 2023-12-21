# TaskSatelliteDeleteExtension - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected TaskSatelliteDeleteExtension(
    	ICardRepository extendedRepositoryWithoutTransaction,
    	ICardContentStrategy contentStrategy,
    	ICardStoreStrategy storeStrategy,
    	ISatelliteTypeRegistry satelliteTypeRegistry
    )
VB __Копировать
     Protected Sub New ( 
    	extendedRepositoryWithoutTransaction As ICardRepository,
    	contentStrategy As ICardContentStrategy,
    	storeStrategy As ICardStoreStrategy,
    	satelliteTypeRegistry As ISatelliteTypeRegistry
    )
C++ __Копировать
     protected:
    TaskSatelliteDeleteExtension(
    	ICardRepository^ extendedRepositoryWithoutTransaction, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardStoreStrategy^ storeStrategy, 
    	ISatelliteTypeRegistry^ satelliteTypeRegistry
    )
F# __Копировать
     new : 
            extendedRepositoryWithoutTransaction : ICardRepository * 
            contentStrategy : ICardContentStrategy * 
            storeStrategy : ICardStoreStrategy * 
            satelliteTypeRegistry : ISatelliteTypeRegistry -> TaskSatelliteDeleteExtension
#### Параметры
extendedRepositoryWithoutTransaction
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий для управления карточками с расширениями, но без транзакции. 
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия для управления контентом файлов.
storeStrategy
[ICardStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
    Стратегия по сохранению карточки.
satelliteTypeRegistry
[ISatelliteTypeRegistry](T_Tessa_Extensions_Platform_Server_Cards_Satellites_ISatelliteTypeRegistry.htm)
    Реестр зарегистрированных типов сателлитов.
##  __См. также
#### Ссылки
[TaskSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
