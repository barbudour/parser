# CardGetRequest.SectionsToExclude - свойство
Список имён физических секций, которые не следует загружать. Не влияет на
виртуальные секции.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<string> SectionsToExclude { get; set; }
VB __Копировать
     Public Property SectionsToExclude As IList(Of String)
    	Get
    	Set
C++ __Копировать
     public:
    property IList<String^>^ SectionsToExclude {
    	IList<String^>^ get ();
    	void set (IList<String^>^ value);
    }
F# __Копировать
     member SectionsToExclude : IList<string> with get, set
#### Значение свойства
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __Заметки
Свойству может быть присвоен только объект типа
[ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm) или null.
## __См. также
#### Ссылки
[CardGetRequest - ](T_Tessa_Cards_CardGetRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
