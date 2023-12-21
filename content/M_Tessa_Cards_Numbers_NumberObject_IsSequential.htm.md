# NumberObject.IsSequential - метод
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
     public bool IsSequential()
VB __Копировать
     Public Function IsSequential As Boolean
C++ __Копировать
     public:
    virtual bool IsSequential() sealed
F# __Копировать
     abstract IsSequential : unit -> bool 
    override IsSequential : unit -> bool 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объект [Tessa.Cards.Numbers.INumberObject] представляет из себя
ссылку на номер из последовательности; false в противном случае.
#### Реализации
[INumberObject.IsSequential()](M_Tessa_Cards_Numbers_INumberObject_IsSequential.htm)  
##  __См. также
#### Ссылки
[NumberObject - ](T_Tessa_Cards_Numbers_NumberObject.htm)
[IsSequential -
перегрузка](Overload_Tessa_Cards_Numbers_NumberObject_IsSequential.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
