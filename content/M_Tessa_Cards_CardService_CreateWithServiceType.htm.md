# CardService.CreateWithServiceType - метод
Создаёт экземпляр класса с указанием его зависимостей и с типом веб-сервиса
[CardServiceType](T_Tessa_Cards_CardServiceType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardService CreateWithServiceType(
    	ICardRepository cardRepository,
    	ICardStreamServerRepository cardStreamServerRepository,
    	CardServiceType serviceType
    )
VB __Копировать
     Public Shared Function CreateWithServiceType ( 
    	cardRepository As ICardRepository,
    	cardStreamServerRepository As ICardStreamServerRepository,
    	serviceType As CardServiceType
    ) As CardService
C++ __Копировать
     public:
    static CardService^ CreateWithServiceType(
    	ICardRepository^ cardRepository, 
    	ICardStreamServerRepository^ cardStreamServerRepository, 
    	CardServiceType serviceType
    )
F# __Копировать
     static member CreateWithServiceType : 
            cardRepository : ICardRepository * 
            cardStreamServerRepository : ICardStreamServerRepository * 
            serviceType : CardServiceType -> CardService 
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий карточек.
cardStreamServerRepository
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)
    Репозиторий для потокового управления карточками.
serviceType [CardServiceType](T_Tessa_Cards_CardServiceType.htm)
    Тип сервиса, от которого был получен переданный объект запроса.
#### Возвращаемое значение
[CardService](T_Tessa_Cards_CardService.htm)  
Созданный объект.
##  __См. также
#### Ссылки
[CardService - ](T_Tessa_Cards_CardService.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
