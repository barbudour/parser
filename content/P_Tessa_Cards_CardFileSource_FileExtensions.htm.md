# CardFileSource.FileExtensions - свойство
Строка со списком расширений, которые рекомендуется использовать с этим
источником файлов. Расширения разделены пробелами и обычно без ведущей точки.
Строка может быть равна null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyList<string> FileExtensions { get; }
VB __Копировать
     Public ReadOnly Property FileExtensions As IReadOnlyList(Of String)
    	Get
C++ __Копировать
     public:
    virtual property IReadOnlyList<String^>^ FileExtensions {
    	IReadOnlyList<String^>^ get () sealed;
    }
F# __Копировать
     abstract FileExtensions : IReadOnlyList<string> with get
    override FileExtensions : IReadOnlyList<string> with get
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
#### Реализации
[ICardFileSource.FileExtensions](P_Tessa_Cards_ICardFileSource_FileExtensions.htm)  
##  __См. также
#### Ссылки
[CardFileSource - ](T_Tessa_Cards_CardFileSource.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
