# CardTypeRepositoryData.Equals(CardTypeRepositoryData) - метод
Сравнивает текущий объект с заданным.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Equals(
    	CardTypeRepositoryData other
    )
VB __Копировать
     Public Function Equals ( 
    	other As CardTypeRepositoryData
    ) As Boolean
C++ __Копировать
     public:
    virtual bool Equals(
    	CardTypeRepositoryData^ other
    ) sealed
F# __Копировать
     abstract Equals : 
            other : CardTypeRepositoryData -> bool 
    override Equals : 
            other : CardTypeRepositoryData -> bool 
#### Параметры
other [CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm)
    Объект, с которым сравнивается текущий объект.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если объекты равны; false в противном случае.
#### Реализации
[IEquatable<T>.Equals(T)](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))  
##  __Заметки
Объекты считаются равными, если их идентификаторы
[ID](P_Tessa_Cards_CardTypeRepositoryData_ID.htm) равны.
##  __См. также
#### Ссылки
[CardTypeRepositoryData - ](T_Tessa_Cards_CardTypeRepositoryData.htm)
[Equals - перегрузка](Overload_Tessa_Cards_CardTypeRepositoryData_Equals.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
