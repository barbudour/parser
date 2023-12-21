# CardFile.AddNewVersionTag - метод
Добавляет заданный тег в список тегов, соответствующих новой версии файла
[NewVersionTags](P_Tessa_Cards_CardFile_NewVersionTags.htm). Возвращает
признак того, что тег отсутствовал и был добавлен.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool AddNewVersionTag(
    	string tag
    )
VB __Копировать
     Public Function AddNewVersionTag ( 
    	tag As String
    ) As Boolean
C++ __Копировать
     public:
    bool AddNewVersionTag(
    	String^ tag
    )
F# __Копировать
     member AddNewVersionTag : 
            tag : string -> bool 
#### Параметры
tag [String](https://learn.microsoft.com/dotnet/api/system.string)
    Добавляемый тег. Не должен быть равен null или пустой строке.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если тег отсутствовал и был добавлен; false, если тег уже присутствовал.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
