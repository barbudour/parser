# CardHelper.TemplateFileIsMatchForSource(CardFile, Guid) - метод
Возвращает признак того, что заданный файл, расположенный в шаблоне,
соответствует файлу в карточке с заданным идентификатором. Идентификатор
версии не проверяется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TemplateFileIsMatchForSource(
    	CardFile templateFile,
    	Guid sourceFileID
    )
VB __Копировать
     Public Shared Function TemplateFileIsMatchForSource ( 
    	templateFile As CardFile,
    	sourceFileID As Guid
    ) As Boolean
C++ __Копировать
     public:
    static bool TemplateFileIsMatchForSource(
    	CardFile^ templateFile, 
    	Guid sourceFileID
    )
F# __Копировать
     static member TemplateFileIsMatchForSource : 
            templateFile : CardFile * 
            sourceFileID : Guid -> bool 
#### Параметры
templateFile [CardFile](T_Tessa_Cards_CardFile.htm)
    Файл, расположенный в шаблоне.
sourceFileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла, с которым может быть связан файл шаблона.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный файл, расположенный в шаблоне, соответствует файлу в
карточке с заданным идентификатором и идентификатором версии; false в
противном случае.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[TemplateFileIsMatchForSource -
перегрузка](Overload_Tessa_Cards_CardHelper_TemplateFileIsMatchForSource.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
