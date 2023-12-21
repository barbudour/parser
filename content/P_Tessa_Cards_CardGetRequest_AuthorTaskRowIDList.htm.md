# CardGetRequest.AuthorTaskRowIDList - свойство
Список идентификаторов заданий, все данные которых будут полностью загружены,
если такие задания доступны от имени автора.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<Guid> AuthorTaskRowIDList { get; set; }
VB __Копировать
     Public Property AuthorTaskRowIDList As IList(Of Guid)
    	Get
    	Set
C++ __Копировать
     public:
    property IList<Guid>^ AuthorTaskRowIDList {
    	IList<Guid>^ get ();
    	void set (IList<Guid>^ value);
    }
F# __Копировать
     member AuthorTaskRowIDList : IList<Guid> with get, set
#### Значение свойства
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Свойству может быть присвоен только объект типа
[ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm) или null.
## __См. также
#### Ссылки
[CardGetRequest - ](T_Tessa_Cards_CardGetRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
