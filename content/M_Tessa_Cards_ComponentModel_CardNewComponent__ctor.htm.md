# CardNewComponent - конструктор
Создаёт экземпляр класса с указанием стратегии, используемой для создания
карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardNewComponent(
    	ICardNewStrategy newStrategy
    )
VB __Копировать
     Public Sub New ( 
    	newStrategy As ICardNewStrategy
    )
C++ __Копировать
     public:
    CardNewComponent(
    	ICardNewStrategy^ newStrategy
    )
F# __Копировать
     new : 
            newStrategy : ICardNewStrategy -> CardNewComponent
#### Параметры
newStrategy
[ICardNewStrategy](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
    Стратегия создания карточки.
##  __См. также
#### Ссылки
[CardNewComponent - ](T_Tessa_Cards_ComponentModel_CardNewComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
