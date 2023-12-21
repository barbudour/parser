# NumberLocationTypes - класс
Стандартные типы местоположений номеров.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberLocationTypes
VB __Копировать
     Public NotInheritable Class NumberLocationTypes
C++ __Копировать
     public ref class NumberLocationTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberLocationTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberLocationTypes
##  __Методы
[IsKnown](M_Tessa_Cards_Numbers_NumberLocationTypes_IsKnown.htm)|  Возвращает
признак того, что тип местоположения номера является известным для
стандартного API.  
---|---  
## __Поля
[All](F_Tessa_Cards_Numbers_NumberLocationTypes_All.htm)|  Список всех типов
местоположений номеров, которые являются частью стандартного API.  
---|---  
[Card](F_Tessa_Cards_Numbers_NumberLocationTypes_Card.htm)|  Произвольное
местоположение для номера в карточке. Например, элемент управления номерами
может самостоятельно указать, где именно должен размещаться номер в карточке.  
[NotAssigned](F_Tessa_Cards_Numbers_NumberLocationTypes_NotAssigned.htm)|  Тип
местоположения номера не задан. Обычно этот тип указывается для действий,
которые не связаны с местоположением номера. Тип зарегистрирован в стандартном
API номеров, но по умолчанию считается, что местоположение неизвестно для
этого типа.  
[Primary](F_Tessa_Cards_Numbers_NumberLocationTypes_Primary.htm)|  Основное
местоположение для номера в карточке. Это местоположение используется для
вычисления Digest.  
[Secondary](F_Tessa_Cards_Numbers_NumberLocationTypes_Secondary.htm)|
Дополнительное местоположение для номера в карточке. Может содержать,
например, проектный номер документа.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
