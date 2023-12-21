# CardFileVersion.RemoveTag - метод
Удаляет заданный тег из списка тегов, соответствующих текущей версии файла
[Tags](P_Tessa_Cards_CardFileVersion_Tags.htm). Возвращает признак того, что
тег присутствовал и был удалён.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RemoveTag(
    	string tag
    )
VB __Копировать
     Public Function RemoveTag ( 
    	tag As String
    ) As Boolean
C++ __Копировать
     public:
    bool RemoveTag(
    	String^ tag
    )
F# __Копировать
     member RemoveTag : 
            tag : string -> bool 
#### Параметры
tag [String](https://learn.microsoft.com/dotnet/api/system.string)
    Удаляемый тег. Не должен быть равен null или пустой строке.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если тег присутствовал и был удалён; false, если тег уже отсутствовал.
## __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
