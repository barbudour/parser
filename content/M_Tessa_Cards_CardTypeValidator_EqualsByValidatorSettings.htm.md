# CardTypeValidator.EqualsByValidatorSettings - метод
Сравнивает сериализованные значения свойств
[ValidatorSettings](P_Tessa_Cards_CardTypeValidator_ValidatorSettings.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool EqualsByValidatorSettings(
    	CardTypeValidator validator
    )
VB __Копировать
     Public Function EqualsByValidatorSettings ( 
    	validator As CardTypeValidator
    ) As Boolean
C++ __Копировать
     public:
    bool EqualsByValidatorSettings(
    	CardTypeValidator^ validator
    )
F# __Копировать
     member EqualsByValidatorSettings : 
            validator : CardTypeValidator -> bool 
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, описывающий информацию о валидаторе типа карточки, свойство [ValidatorSettings](P_Tessa_Cards_CardTypeValidator_ValidatorSettings.htm) которого требуется сравнить со свойством текущего объекта.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если свойства равны; false в противном случае.
##  __Заметки
При сравнении объектов этим методом производится сериализация свойства
[ValidatorSettings](P_Tessa_Cards_CardTypeValidator_ValidatorSettings.htm).
## __См. также
#### Ссылки
[CardTypeValidator - ](T_Tessa_Cards_CardTypeValidator.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
