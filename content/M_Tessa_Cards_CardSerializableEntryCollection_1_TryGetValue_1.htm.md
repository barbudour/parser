# CardSerializableEntryCollection<T>.TryGetValue(String, T) - метод
Пытается вернуть элемент коллекции по его имени.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool TryGetValue(
    	string name,
    	out T result
    )
VB __Копировать
     Public Function TryGetValue ( 
    	name As String,
    	<OutAttribute> ByRef result As T
    ) As Boolean
C++ __Копировать
     public:
    bool TryGetValue(
    	String^ name, 
    	[OutAttribute] T% result
    )
F# __Копировать
     member TryGetValue : 
            name : string * 
            result : 'T byref -> bool 
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя элемента.
result [T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
    Элемент, полученный по заданному имени.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если элемент с заданным именем содержится в коллекции и был возвращён в
параметре result; false в противном случае.
## __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[TryGetValue -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_TryGetValue.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
