# ICardFileSourceOverride.FileExtensions - свойство
Список рекомендуемый расширений для использования совместно с этим источником
файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    IReadOnlyList<string>? FileExtensions { get; set; }
VB __Копировать
     Property FileExtensions As IReadOnlyList(Of String)
    	Get
    	Set
C++ __Копировать
    property IReadOnlyList<String^>^ FileExtensions {
    	IReadOnlyList<String^>^ get ();
    	void set (IReadOnlyList<String^>^ value);
    }
F# __Копировать
     abstract FileExtensions : IReadOnlyList<string> with get, set
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardFileSourceOverride - ](T_Tessa_Cards_ICardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
