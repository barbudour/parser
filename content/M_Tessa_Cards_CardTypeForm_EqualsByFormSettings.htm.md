# CardTypeForm.EqualsByFormSettings - метод
Сравнивает сериализованные значения свойств
[FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool EqualsByFormSettings(
    	CardTypeForm cardType
    )
VB __Копировать
     Public Function EqualsByFormSettings ( 
    	cardType As CardTypeForm
    ) As Boolean
C++ __Копировать
     public:
    bool EqualsByFormSettings(
    	CardTypeForm^ cardType
    )
F# __Копировать
     member EqualsByFormSettings : 
            cardType : CardTypeForm -> bool 
#### Параметры
cardType [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)
    Объект, описывающий информацию о типе карточки, свойство [FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm) которого требуется сравнить со свойством текущего объекта.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если свойства равны; false в противном случае.
##  __Заметки
При сравнении объектов этим методом производится сериализация свойства
[FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm).
## __См. также
#### Ссылки
[CardTypeForm - ](T_Tessa_Cards_CardTypeForm.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
