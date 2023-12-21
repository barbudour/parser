# CardTypeExtension.EqualsByExtensionSettings - метод
Сравнивает сериализованные значения свойств
[ExtensionSettings](P_Tessa_Cards_CardTypeExtension_ExtensionSettings.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool EqualsByExtensionSettings(
    	CardTypeExtension extension
    )
VB __Копировать
     Public Function EqualsByExtensionSettings ( 
    	extension As CardTypeExtension
    ) As Boolean
C++ __Копировать
     public:
    bool EqualsByExtensionSettings(
    	CardTypeExtension^ extension
    )
F# __Копировать
     member EqualsByExtensionSettings : 
            extension : CardTypeExtension -> bool 
#### Параметры
extension [CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)
    Объект, описывающий информацию о расширении типа карточки, свойство [ExtensionSettings](P_Tessa_Cards_CardTypeExtension_ExtensionSettings.htm) которого требуется сравнить со свойством текущего объекта.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если свойства равны; false в противном случае.
##  __Заметки
При сравнении объектов этим методом производится сериализация свойства
[ExtensionSettings](P_Tessa_Cards_CardTypeExtension_ExtensionSettings.htm).
## __См. также
#### Ссылки
[CardTypeExtension - ](T_Tessa_Cards_CardTypeExtension.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
