# CardFile.RemoveNewVersionTag - метод
Удаляет заданный тег из списка тегов, соответствующих новой версии файла
[NewVersionTags](P_Tessa_Cards_CardFile_NewVersionTags.htm). Возвращает
признак того, что тег присутствовал и был удалён.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RemoveNewVersionTag(
    	string tag
    )
VB __Копировать
     Public Function RemoveNewVersionTag ( 
    	tag As String
    ) As Boolean
C++ __Копировать
     public:
    bool RemoveNewVersionTag(
    	String^ tag
    )
F# __Копировать
     member RemoveNewVersionTag : 
            tag : string -> bool 
#### Параметры
tag [String](https://learn.microsoft.com/dotnet/api/system.string)
    Удаляемый тег. Не должен быть равен null или пустой строке.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если тег присутствовал и был удалён; false, если тег уже отсутствовал.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
