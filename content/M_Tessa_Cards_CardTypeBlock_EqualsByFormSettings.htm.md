# CardTypeBlock.EqualsByFormSettings - метод
Сравнивает сериализованные значения свойств
[FormSettings](P_Tessa_Cards_CardTypeBlock_FormSettings.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool EqualsByFormSettings(
    	CardTypeBlock block
    )
VB __Копировать
     Public Function EqualsByFormSettings ( 
    	block As CardTypeBlock
    ) As Boolean
C++ __Копировать
     public:
    bool EqualsByFormSettings(
    	CardTypeBlock^ block
    )
F# __Копировать
     member EqualsByFormSettings : 
            block : CardTypeBlock -> bool 
#### Параметры
block [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)
    Объект, описывающий блок типа карточки, свойство [FormSettings](P_Tessa_Cards_CardTypeBlock_FormSettings.htm) которого требуется сравнить со свойством текущего объекта.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если свойства равны; false в противном случае.
##  __Заметки
При сравнении объектов этим методом производится сериализация свойства
[BlockSettings](P_Tessa_Cards_CardTypeBlock_BlockSettings.htm).
## __См. также
#### Ссылки
[CardTypeBlock - ](T_Tessa_Cards_CardTypeBlock.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
