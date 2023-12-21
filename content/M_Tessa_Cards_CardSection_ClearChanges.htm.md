# CardSection.ClearChanges - метод
Удаляет всю информацию об изменённых объектах.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSection ClearChanges()
VB __Копировать
     Public Function ClearChanges As CardSection
C++ __Копировать
     public:
    CardSection^ ClearChanges()
F# __Копировать
     member ClearChanges : unit -> CardSection 
#### Возвращаемое значение
[CardSection](T_Tessa_Cards_CardSection.htm)  
Текущий объект для цепочки вызовов.
##  __Заметки
После выполнения метода все поля строковой секции считаются неизменными.
## __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
Тип секции [Type](P_Tessa_Cards_CardSection_Type.htm) не равен
[Entry](T_Tessa_Cards_CardSectionType.htm). Метод доступен только для
строковых секций.  
---|---  
## __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
