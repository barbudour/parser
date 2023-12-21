# CardNewStrategy - конструктор
Создаёт экземпляр объекта с указанием стратегии кэширования.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardNewStrategy(
    	ICardNewCachingStrategy cachingStrategy
    )
VB __Копировать
     Public Sub New ( 
    	cachingStrategy As ICardNewCachingStrategy
    )
C++ __Копировать
     public:
    CardNewStrategy(
    	ICardNewCachingStrategy^ cachingStrategy
    )
F# __Копировать
     new : 
            cachingStrategy : ICardNewCachingStrategy -> CardNewStrategy
#### Параметры
cachingStrategy
[ICardNewCachingStrategy](T_Tessa_Cards_ComponentModel_ICardNewCachingStrategy.htm)
     Стратегия кэширования объектов для операции по созданию карточки. 
## __См. также
#### Ссылки
[CardNewStrategy - ](T_Tessa_Cards_ComponentModel_CardNewStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
