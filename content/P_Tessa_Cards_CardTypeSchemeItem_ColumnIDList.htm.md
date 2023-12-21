# CardTypeSchemeItem.ColumnIDList - свойство
Список идентификаторов физических и комплексных колонок секции
[SectionID](P_Tessa_Cards_CardTypeSchemeItem_SectionID.htm), которые
определяют, какие колонки будут загружаться для типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableList<Guid> ColumnIDList { get; set; }
VB __Копировать
     Public Property ColumnIDList As SealableList(Of Guid)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableList<Guid>^ ColumnIDList {
    	SealableList<Guid>^ get ();
    	void set (SealableList<Guid>^ value);
    }
F# __Копировать
     member ColumnIDList : SealableList<Guid> with get, set
#### Значение свойства
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeSchemeItem - ](T_Tessa_Cards_CardTypeSchemeItem.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
