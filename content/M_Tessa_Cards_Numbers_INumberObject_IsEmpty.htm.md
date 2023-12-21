# INumberObject.IsEmpty - метод
Возвращает признак того, что объект [Tessa.Cards.Numbers.INumberObject]
представляет из себя ссылку на отсутствующий (или ещё не известный) номер. Как
правило, номер считается пустым, если его строка полного номера равна null или
пустой строке, а также либо отсутствует числовой номер, либо имя
последовательности равно null или пустой строке. Т.о. пустой номер не является
номером из последовательности.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsEmpty()
VB __Копировать
     Function IsEmpty As Boolean
C++ __Копировать
     bool IsEmpty()
F# __Копировать
     abstract IsEmpty : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объект [Tessa.Cards.Numbers.INumberObject] представляет из себя
ссылку на отсутствующий (или ещё не известный) номер; false в противном
случае.
## __См. также
#### Ссылки
[INumberObject - ](T_Tessa_Cards_Numbers_INumberObject.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
