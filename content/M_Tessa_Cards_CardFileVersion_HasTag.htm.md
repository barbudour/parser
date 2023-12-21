# CardFileVersion.HasTag - метод
Возвращает признак того, что текущая версия содержит указанный тег в свойстве
[Tags](P_Tessa_Cards_CardFileVersion_Tags.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasTag(
    	string tag
    )
VB __Копировать
     Public Function HasTag ( 
    	tag As String
    ) As Boolean
C++ __Копировать
     public:
    bool HasTag(
    	String^ tag
    )
F# __Копировать
     member HasTag : 
            tag : string -> bool 
#### Параметры
tag [String](https://learn.microsoft.com/dotnet/api/system.string)
    Тег, проверка наличия которого выполняется.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если текущая версия содержит указанный тег; false в противном случае.
## __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
