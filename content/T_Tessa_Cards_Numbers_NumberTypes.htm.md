# NumberTypes - класс
Стандартные типы номеров.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class NumberTypes
VB __Копировать
     Public NotInheritable Class NumberTypes
C++ __Копировать
     public ref class NumberTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type NumberTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberTypes
##  __Методы
[IsKnown](M_Tessa_Cards_Numbers_NumberTypes_IsKnown.htm)|  Возвращает признак
того, что тип номера является известным для стандартного API.  
---|---  
## __Поля
[All](F_Tessa_Cards_Numbers_NumberTypes_All.htm)|  Список всех типов номеров,
которые являются частью стандартного API.  
---|---  
[Custom](F_Tessa_Cards_Numbers_NumberTypes_Custom.htm)|  Произвольный номер в
документе, который не описывается остальными значениями перечисления. Для
этого типа по умолчанию не определено расположение в номере, но оно может быть
косвенно задано через настройки объекта
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm).  
[Primary](F_Tessa_Cards_Numbers_NumberTypes_Primary.htm)|  Основной номер
документа. До регистрации это внутренний номер документа, а после регистрации
- это регистрационный номер.  
[Secondary](F_Tessa_Cards_Numbers_NumberTypes_Secondary.htm)|  Дополнительный
(внутренний) номер документа. Не зависит от регистрации документа.  
## __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
