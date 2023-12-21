# NumberObject.CompareTo - метод
Выполняет сравнение текущего объекта с заданным.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int CompareTo(
    	INumberObject other
    )
VB __Копировать
     Public Function CompareTo ( 
    	other As INumberObject
    ) As Integer
C++ __Копировать
     public:
    virtual int CompareTo(
    	INumberObject^ other
    ) sealed
F# __Копировать
     abstract CompareTo : 
            other : INumberObject -> int 
    override CompareTo : 
            other : INumberObject -> int 
#### Параметры
other [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
    Объект, с которым сравнивается текущий объект.
#### Возвращаемое значение
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)  
0, если объекты равны; отрицательное значение, если текущий объект меньше
заданного; положительное значение, если текущий объект больше заданного.
#### Реализации
[IComparable<T>.CompareTo(T)](https://learn.microsoft.com/dotnet/api/system.icomparable-1.compareto#system-
icomparable-1-compareto\(-0\))  
##  __Заметки
Сравнение выполняется по числовому номеру без учёта строкового представления.
## __См. также
#### Ссылки
[NumberObject - ](T_Tessa_Cards_Numbers_NumberObject.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
