# CardTypeValueComparer.Equals(CardType, CardType) - метод
Сравнивает типы карточек по всем свойствам.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Equals(
    	CardType x,
    	CardType y
    )
VB __Копировать
     Public Function Equals ( 
    	x As CardType,
    	y As CardType
    ) As Boolean
C++ __Копировать
     public:
    virtual bool Equals(
    	CardType^ x, 
    	CardType^ y
    ) sealed
F# __Копировать
     abstract Equals : 
            x : CardType * 
            y : CardType -> bool 
    override Equals : 
            x : CardType * 
            y : CardType -> bool 
#### Параметры
x [CardType](T_Tessa_Cards_CardType.htm)
    Первый тип карточки.
y [CardType](T_Tessa_Cards_CardType.htm)
    Второй тип карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если типы карточек идентичны; false в противном случае.
#### Реализации
[IEqualityComparer<T>.Equals(T,
T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1.equals#system-
collections-generic-iequalitycomparer-1-equals\(-0-0\))  
##  __Заметки
При сравнении объектов этим методом производится сериализация свойства
[FormSettings](P_Tessa_Cards_CardTypeForm_FormSettings.htm).
## __См. также
#### Ссылки
[CardTypeValueComparer - ](T_Tessa_Cards_CardTypeValueComparer.htm)
[Equals - перегрузка](Overload_Tessa_Cards_CardTypeValueComparer_Equals.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
