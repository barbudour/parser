# CardFileSourceOverride.FileExtensions - свойство
Список рекомендуемый расширений для использования совместно с этим источником
файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyList<string>? FileExtensions { get; set; }
VB __Копировать
     Public Property FileExtensions As IReadOnlyList(Of String)
    	Get
    	Set
C++ __Копировать
     public:
    virtual property IReadOnlyList<String^>^ FileExtensions {
    	IReadOnlyList<String^>^ get () sealed;
    	void set (IReadOnlyList<String^>^ value) sealed;
    }
F# __Копировать
     abstract FileExtensions : IReadOnlyList<string> with get, set
    override FileExtensions : IReadOnlyList<string> with get, set
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
#### Реализации
[ICardFileSourceOverride.FileExtensions](P_Tessa_Cards_ICardFileSourceOverride_FileExtensions.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardFileSourceOverride - ](T_Tessa_Cards_CardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
