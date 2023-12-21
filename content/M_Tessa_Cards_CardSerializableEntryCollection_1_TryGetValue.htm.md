# CardSerializableEntryCollection<T>.TryGetValue(Guid, T) - метод
Пытается вернуть элемент коллекции по его идентификатору.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool TryGetValue(
    	Guid id,
    	out T result
    )
VB __Копировать
     Public Function TryGetValue ( 
    	id As Guid,
    	<OutAttribute> ByRef result As T
    ) As Boolean
C++ __Копировать
     public:
    bool TryGetValue(
    	Guid id, 
    	[OutAttribute] T% result
    )
F# __Копировать
     member TryGetValue : 
            id : Guid * 
            result : 'T byref -> bool 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор элемента.
result [T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
    Элемент, полученный по заданному идентификатору.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если элемент с заданным идентификатором содержится в коллекции и был
возвращён в параметре result; false в противном случае.
## __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[TryGetValue -
перегрузка](Overload_Tessa_Cards_CardSerializableEntryCollection_1_TryGetValue.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
