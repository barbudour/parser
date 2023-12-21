# INumberObject.IsSequential - метод
Возвращает признак того, что объект [Tessa.Cards.Numbers.INumberObject]
представляет из себя ссылку на номер из последовательности. Как правило, номер
считается взятым из последовательности, если его числовое представление, и имя
последовательности не равны null или пустой строке. Строка полного номера
может быть равна null или пустой строке. Т.о. пустой номер не является номером
из последовательности. Если номер не является номером из последовательности,
то его нельзя освободить, дерезервировать или выделить повторно.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsSequential()
VB __Копировать
     Function IsSequential As Boolean
C++ __Копировать
     bool IsSequential()
F# __Копировать
     abstract IsSequential : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объект [Tessa.Cards.Numbers.INumberObject] представляет из себя
ссылку на номер из последовательности; false в противном случае.
## __См. также
#### Ссылки
[INumberObject - ](T_Tessa_Cards_Numbers_INumberObject.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
