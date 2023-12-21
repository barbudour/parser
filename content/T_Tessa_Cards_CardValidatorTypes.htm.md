# CardValidatorTypes - класс
Типы валидаторов [CardValidatorType](T_Tessa_Cards_CardValidatorType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardValidatorTypes
VB __Копировать
     Public NotInheritable Class CardValidatorTypes
C++ __Копировать
     public ref class CardValidatorTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardValidatorTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardValidatorTypes
##  __Поля
[NotNullField](F_Tessa_Cards_CardValidatorTypes_NotNullField.htm)|  Валидатор
наличия значения в поле секции, отличного от null или пустой строки. Если
секция коллекционная или древовидная, то проверка выполняется для каждой
добавляемой или изменяемой строки.  
---|---  
[NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm)|  Валидатор
наличия строк в коллекционной или древовидной секции.  
[Unique](F_Tessa_Cards_CardValidatorTypes_Unique.htm)|  Валидатор уникальности
значения в поле секции относительно других карточек или других строк в той же
карточке. Если секция коллекционная или древовидная, то проверка выполняется
для каждой добавляемой или изменяемой строки.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
