# CardService - конструктор
Инициализирует новый экземпляр класса
[CardService](T_Tessa_Cards_CardService.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardService(
    	ICardRepository cardRepository,
    	ICardStreamServerRepository cardStreamServerRepository
    )
VB __Копировать
     Public Sub New ( 
    	cardRepository As ICardRepository,
    	cardStreamServerRepository As ICardStreamServerRepository
    )
C++ __Копировать
     public:
    CardService(
    	ICardRepository^ cardRepository, 
    	ICardStreamServerRepository^ cardStreamServerRepository
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            cardStreamServerRepository : ICardStreamServerRepository -> CardService
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий карточек.
cardStreamServerRepository
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)
    Репозиторий для потокового управления карточками.
##  __См. также
#### Ссылки
[CardService - ](T_Tessa_Cards_CardService.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
