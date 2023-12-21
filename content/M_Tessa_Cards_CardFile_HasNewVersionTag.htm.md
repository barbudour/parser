# CardFile.HasNewVersionTag - метод
Возвращает признак того, что создаваемая версия будет содержать указанный тег
в свойстве [NewVersionTags](P_Tessa_Cards_CardFile_NewVersionTags.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasNewVersionTag(
    	string tag
    )
VB __Копировать
     Public Function HasNewVersionTag ( 
    	tag As String
    ) As Boolean
C++ __Копировать
     public:
    bool HasNewVersionTag(
    	String^ tag
    )
F# __Копировать
     member HasNewVersionTag : 
            tag : string -> bool 
#### Параметры
tag [String](https://learn.microsoft.com/dotnet/api/system.string)
    Тег, проверка наличия которого выполняется.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если текущая версия содержит указанный тег; false в противном случае.
## __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
