# BackupCardDeleteExtension - конструктор
Инициализирует новый экземпляр класса
[BackupCardDeleteExtension](T_Tessa_Extensions_Platform_Server_Cards_BackupCardDeleteExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public BackupCardDeleteExtension(
    	ICardRepository extendedRepositoryWithoutTransaction,
    	ICardRepository defaultRepositoryWithoutTransaction,
    	ICardContentStrategy contentStrategy,
    	ICardStoreStrategy storeStrategy
    )
VB __Копировать
     Public Sub New ( 
    	extendedRepositoryWithoutTransaction As ICardRepository,
    	defaultRepositoryWithoutTransaction As ICardRepository,
    	contentStrategy As ICardContentStrategy,
    	storeStrategy As ICardStoreStrategy
    )
C++ __Копировать
     public:
    BackupCardDeleteExtension(
    	ICardRepository^ extendedRepositoryWithoutTransaction, 
    	ICardRepository^ defaultRepositoryWithoutTransaction, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardStoreStrategy^ storeStrategy
    )
F# __Копировать
     new : 
            extendedRepositoryWithoutTransaction : ICardRepository * 
            defaultRepositoryWithoutTransaction : ICardRepository * 
            contentStrategy : ICardContentStrategy * 
            storeStrategy : ICardStoreStrategy -> BackupCardDeleteExtension
#### Параметры
extendedRepositoryWithoutTransaction
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
defaultRepositoryWithoutTransaction
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
storeStrategy
[ICardStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
## __См. также
#### Ссылки
[BackupCardDeleteExtension -
](T_Tessa_Extensions_Platform_Server_Cards_BackupCardDeleteExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
