# CardRow.Set - метод
Создаёт полную копию хранилища заданной строки в текущей строке. При этом
удаляются все поля и служебная информация из текущей строки, после чего она
копируется из заданной. Подписчики на события и другая информация, не
являющаяся частью хранилища текущего объекта, остаётся неизменной.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void Set(
    	CardRow row
    )
VB __Копировать
     Public Sub Set ( 
    	row As CardRow
    )
C++ __Копировать
     public:
    void Set(
    	CardRow^ row
    )
F# __Копировать
     member Set : 
            row : CardRow -> unit 
#### Параметры
row [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка, из которой производится копирование полей и служебной информации.
##  __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
