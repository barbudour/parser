# CardSerializableEntryCollection<T>.Remove(String) - метод
Удаляет элемент с заданным именем из коллекции.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Remove(
    	string name
    )
VB __Копировать
     Public Function Remove ( 
    	name As String
    ) As Boolean
C++ __Копировать
     public:
    bool Remove(
    	String^ name
    )
F# __Копировать
     member Remove : 
            name : string -> bool 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя удаляемого из коллекции элемента.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если элемент с заданным именем был удалён;
false, если такой элемент не был найден.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[Remove -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_Remove.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
