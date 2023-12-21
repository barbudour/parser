# ICardFileSource.FileExtensions - свойство
Строка со списком расширений, которые рекомендуется использовать с этим
источником файлов. Расширения разделены пробелами и обычно без ведущей точки.
Строка может быть равна null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    IReadOnlyList<string> FileExtensions { get; }
VB __Копировать
     ReadOnly Property FileExtensions As IReadOnlyList(Of String)
    	Get
C++ __Копировать
    property IReadOnlyList<String^>^ FileExtensions {
    	IReadOnlyList<String^>^ get ();
    }
F# __Копировать
     abstract FileExtensions : IReadOnlyList<string> with get
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[ICardFileSource - ](T_Tessa_Cards_ICardFileSource.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
