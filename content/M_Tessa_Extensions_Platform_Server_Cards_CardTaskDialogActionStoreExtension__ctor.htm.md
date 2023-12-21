# CardTaskDialogActionStoreExtension - конструктор
Инициализирует новый экземпляр класса
[CardTaskDialogActionStoreExtension](T_Tessa_Extensions_Platform_Server_Cards_CardTaskDialogActionStoreExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTaskDialogActionStoreExtension(
    	ICardRepository cardRepository,
    	[DependencyAttribute("ExtendedWithoutTransaction")] ICardRepository cardRepositoryEwt
    )
VB __Копировать
     Public Sub New ( 
    	cardRepository As ICardRepository,
    	<DependencyAttribute("ExtendedWithoutTransaction")> cardRepositoryEwt As ICardRepository
    )
C++ __Копировать
     public:
    CardTaskDialogActionStoreExtension(
    	ICardRepository^ cardRepository, 
    	[DependencyAttribute(L"ExtendedWithoutTransaction")] ICardRepository^ cardRepositoryEwt
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            [<DependencyAttribute("ExtendedWithoutTransaction")>] cardRepositoryEwt : ICardRepository -> CardTaskDialogActionStoreExtension
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardRepositoryEwt [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
## __См. также
#### Ссылки
[CardTaskDialogActionStoreExtension -
](T_Tessa_Extensions_Platform_Server_Cards_CardTaskDialogActionStoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
